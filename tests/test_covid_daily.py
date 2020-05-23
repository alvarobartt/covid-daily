# Copyright 2020 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.

import pytest

import covid_daily


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
        covid_daily.overview(as_json=param['as_json'])


if __name__ == "__main__":
    test_overview()
