# Copyright 2020 Alvaro Bartolome del Canto
# See LICENSE for details.

import pytest

import coronavirus_daily_data


def sample_tests():
    params = [
        {
            'value': True
        },
        {
            'value': False
        }
    ]

    for param in params:
        assert coronavirus_daily_data.sample_function(value=param['value'])


if __name__ == "__main__":
    sample_tests()
