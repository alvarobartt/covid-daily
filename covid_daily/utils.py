# Copyright 2020 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.

import json

from .regex import (LINES, COMMENTS, SPACES, CHART,
                    CHART_TITLE, CHART_OPTIONS, CHART_SERIES, 
                    CHART_XAXIS,CHART_YAXIS, CHART_END)


def is_visible(attr):
    """
    This function checks whether an HTML element attribute is visible or hidden based on
    the style of that HTML element. The purpose of this function in this package is to avoid
    including data that is useless, such as inner code markers, non-sense data, etc. So this
    function will ensure that we just retrieve useful data.

    Args:
        attr (:obj:`lxml.html.HtmlElement`): HTML element

    Returns:
        :obj:`bool` - flag
            This function returns either `True` or `False` depending on the style of the HTML element
            received from parameter, whether if it is visible or not, respectively.
    """

    if 'style' in attr.attrib:
        style = attr.get('style')
        if style.__contains__("display:none") or style.__contains__("display: none"):
            return False

    return True


def highcharts_parser(highchart_script, just_title=False):
    """
    This function parses a HighchartJS Script, which contains all the information from the specified
    chart, based on its title. So on, the given JS script will be parsed if the chart's title matches 
    the introduced one; and the most relevant information from the chart towards the :obj:`pd.DataFrame`
    generation will be returned as a :obj:`JSON`, which is indeed a Python :obj:`dict`.

    Args:
        highchart_script (:obj:`lxml.html.HTMLElement`): is the JS script retrieved from the original HTML
        just_title (:obj:`bool`, optional):
            if `True` this function will just return the chart title. Default value is `False`, which 
            means that the chart data will be parsed and returned.

    Returns:
        :obj:`dict` - chart
            This function returns a :obj:`dict`, with the most relevant fields and values towards the creation
            of a dataset from the chart values. Unless the paramter `just_title` is set to `False`, so that the
            title will be returned, which is a :obj:`str`.

    """

    chart = highchart_script.text_content().strip()

    chart = LINES.sub('', chart)
    chart = COMMENTS.sub('', chart)
    chart = SPACES.sub(' ', chart)
    
    chart = chart.replace('\'', '\"')
    chart = CHART.search(chart).group(0)

    if just_title:
        title = CHART_TITLE.search(chart).group(0)
        title = title.replace('Highcharts.chart(\"', '').replace('\", ', '')
        
        return title

    chart = CHART_TITLE.sub('', chart)
    chart = CHART_END.sub('', chart)

    options = CHART_OPTIONS.findall(chart)
    options = list(set(options))

    for option in options:
        chart = chart.replace(option, ' \"' + option.replace(' ', '').replace(':', '') + '\": ')

    column = CHART_YAXIS.search(chart).group(0)
    column = column.replace('"yAxis": { "title": { "text": "', '').replace('"', '')

    chart = '{' + ', '.join([
        CHART_XAXIS.search(chart).group(0).replace('},', '}'),
        CHART_SERIES.search(chart).group(0)[::-1].replace(',]', ']', 1)[::-1].replace(', }', ' }')
    ]) + '}'

    chart = json.loads(chart)

    chart['column'] = column

    return chart