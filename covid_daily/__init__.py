# Copyright 2020 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.

__author__ = 'Alvaro Bartolome del Canto'
__version__ = '1.1'

__functions__ = [
    'overview(as_json)',
    'data(country, chart, as_json)'
]

from .covid import overview, data
