# Copyright 2020 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.

import re

# Basic text-cleaning regular expressions 
LINES = re.compile(r'[\n\t]')
COMMENTS = re.compile(r'\/\*(.*?)\*\/')
SPACES = re.compile(r'[ ]{2,}')

# HighchartsJS applied regular expressions
CHART = re.compile(r'(Highcharts\.chart\(\"[a-zA-z\-]*\"\, )(.*?)(\}\)\;)')
CHART_TITLE = re.compile(r'(Highcharts\.chart\(\"[a-zA-z\-]*\"\, )')
CHART_END = re.compile(r'\)\;')
CHART_OPTIONS = re.compile(r' [\w]+\: ')
CHART_XAXIS = re.compile(r'(\"xAxis\"\: \{)(.*?)(\}\,)')
CHART_YAXIS = re.compile(r'(\"yAxis\"\: \{ \"title\"\: \{ \"text\"\: \")(.*?)(\")')
CHART_SERIES = re.compile(r'(\"series\"\: \[\{)(.*?)(\}( ){0,}\]\,)')