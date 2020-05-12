# Copyright 2020 Alvaro Bartolome del Canto
# See LICENSE for details.

import requests
from lxml.html import fromstring

import pandas as pd
import json

import numpy as np

from .auxiliar import is_visible


def overview(as_json=False):
    """
    This function will retrieve the coronavirus data overview from all the available countries 
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
        ConnectionError: raised if connection with Worldometer failed

    """

    if not isinstance(as_json, bool):
        raise ValueError("as_json parameter value can just be either True or False.")

    url = "https://www.worldometers.info/coronavirus"

    req = requests.get(url)

    if req.status_code != 200:
        raise ConnectionError("Connection to Worldometer.info did not succeed, error code: " + str(req.status_code))

    root = fromstring(req.text)
    table = root.xpath(".//table[@id='main_table_countries_today'][1]")[0]

    thead = table.xpath(".//thead/tr/th")

    columns = list()

    for th in thead:
        if is_visible(th) is True:
            columns.append(th.text_content().replace('\n', '').replace(u'\xa0', u'').strip())

    tbody = table.xpath(".//tbody/tr")

    rows = list()

    for tr in tbody:
        if is_visible(tr) is True:
            rows.append([value.text_content().strip() for value in tr.xpath(".//td") if is_visible(value) is True])

    data = pd.DataFrame(rows, columns=columns)

    data.replace('', np.nan, inplace=True)

    if as_json is False:
        return data
    elif as_json is True:
        return json.loads(json.dumps(data.to_dict(orient='records')))
