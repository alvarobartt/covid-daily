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


def test_data():
    data = covid_daily.data(
        country='france',
        chart='graph-deaths-daily',
        as_json=False
    )

    print(data.tail())


if __name__ == "__main__":
    test_overview()
    test_data()
