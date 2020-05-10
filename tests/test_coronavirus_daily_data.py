# Copyright 2020 Alvaro Bartolome del Canto
# See LICENSE for details.

import pytest

import coronavirus_daily_data


def test_overview():
    params = [
        {
            'as_json': True
        },
        {
            'as_json': False
        }
    ]

    for param in params:
        coronavirus_daily_data.overview(as_json=param['as_json'])


if __name__ == "__main__":
    test_overview()
