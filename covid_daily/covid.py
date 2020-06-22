# Copyright 2020 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.

import requests
from lxml.html import fromstring

import pandas as pd
import json

from unidecode import unidecode

from datetime import datetime

import numpy as np

from .utils import is_visible, highcharts_parser
from .constants import AVAILABLE_COUNTRIES, AVAILABLE_CHARTS


def overview(as_json=False):
    """
    This function retrieves the coronavirus data overview from all the available countries 
    from worldometers.info/coronavirus/, which contains real time data and statistics from multiple
    features realted to the virus. For more information, please visit: https://www.worldometers.info/coronavirus/

    Args:
        as_json (:obj:`bool`):
            set to `True` if overview wants to be retrieved as :obj:`json`, if not, 
            leave default value (`False`).

    Returns:
        :obj:`pandas.DataFrame` - overview
            This function returns a :obj:`pandas.DataFrame` by default (if `as_json` parameter
            is set to `False`, if `True` a :obj:`json` is returned), containing the world
            overview coronavirus data.

    Raises:
        ValueError: raised if any of the introduced parameters is not valid
        ConnectionError: raised if connection with Worldometers failed

    """

    if not isinstance(as_json, bool):
        raise ValueError("as_json parameter value can just be either True or False.")

    url = "https://www.worldometers.info/coronavirus"

    req = requests.get(url)

    if req.status_code != 200:
        raise ConnectionError("Connection to Worldometers.info did not succeed, error code: " + str(req.status_code))

    root = fromstring(req.text)
    table = root.xpath(".//table[@id='main_table_countries_today'][1]")[0]

    thead = table.xpath(".//thead/tr/th")

    columns = list()

    for th in thead:
        if is_visible(th) is True:
            column = th.text_content().replace('\n', '').replace(u'\xa0', u'').strip()
            columns.append(column)

    tbody = table.xpath(".//tbody/tr")

    rows = list()

    for tr in tbody:
        if is_visible(tr) is True:
            rows.append([value.text_content().strip() for value in tr.xpath(".//td") if is_visible(value) is True])

    data = pd.DataFrame(rows, columns=columns)

    data.drop(columns=['#'], inplace=True)

    data["Country,Other"] = data['Country,Other'].str.replace(':', '')

    cols = list(set(data.columns) - set(['Country,Other']))

    data.replace('', '0', inplace=True)
    data.replace('N/A', '0', inplace=True)

    for col in cols:
        data[col] = data[col].str.replace('+', '').str.replace(',', '').astype(float).astype(int)

    if as_json is False:
        return data
    elif as_json is True:
        return json.loads(json.dumps(data.to_dict(orient='records')))


def data(country, chart, as_json=False):
    """
    This function will retrieve the coronavirus data overview from all the available countries 
    from worldometers.info/coronavirus/, which contains real time data and statistics from multiple
    features realted to the virus. For more information, please visit: https://www.worldometers.info/coronavirus/

    Args:
        chart (:obj:`str`):
            name of the country to retrieve the COVID data from (available values at: 
            `covid_daily.constants.AVAILABLE_COUNTRIES`)
        chart (:obj:`str`):
            name of the chart to retrieve the COVID data from (available values at: 
            `covid_daily.constants.AVAILABLE_CHARTS`)
        as_json (:obj:`bool`):
            set to `True` if overview wants to be retrieved as :obj:`json`, if not, 
            leave default value (`False`).

    Returns:
        :obj:`pandas.DataFrame` - data
            This function returns a :obj:`pandas.DataFrame` by default (if `as_json` parameter
            is set to `False`, if `True` a :obj:`json` is returned), containing the COVID data 
            of the introduced chart from the introduced country.

    Raises:
        ValueError: raised if any of the introduced parameters is not valid
        ConnectionError: raised if connection with Worldometers failed

    """

    if not isinstance(country, str):
        raise ValueError("country must be a valid str.")

    country = unidecode(country.strip().lower().replace(' ', '-'))

    if country not in AVAILABLE_COUNTRIES:
        raise ValueError("Introduced country is a valid value, but not a valid country.")

    if not isinstance(chart, str):
        raise ValueError("chart must be a valid str.")

    if chart not in AVAILABLE_CHARTS:
        raise ValueError("Introduced chart is a valid value, but not a valid chart.")

    url = "https://www.worldometers.info/coronavirus/country/" + country + "/"
    
    req = requests.get(url)
    
    if req.status_code != 200:
        raise ConnectionError("Connection to Worldometers.info did not succeed, error code: " + str(req.status_code))
        
    root = fromstring(req.text)
    scripts = root.xpath(".//script")
    
    flag = False

    for script in scripts:
        if not script.text_content().strip().__contains__("Highcharts.chart"):
            continue

        chart_title = highcharts_parser(highchart_script=script, just_title=True)

        if chart_title != chart:
            continue

        chart = highcharts_parser(highchart_script=script)

        x = chart['series'][0]['data']
        y = [datetime.strptime(value + ', 2020', '%b %d, %Y') for value in chart['xAxis']['categories']]

        data = pd.DataFrame({'Date': y, chart['column']: x})
        data.set_index('Date', inplace=True)

        flag = True

    if not flag:
        raise RuntimeError("Information could not be retrieved since it is not available at Worldometers.info!")

    return data
