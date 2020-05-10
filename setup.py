# Copyright 2020 Alvaro Bartolome del Canto
# See LICENSE for details.

from setuptools import setup, find_packages
import io


def readme():
    with io.open('README.md', encoding='utf-8') as f:
        return f.read()

def requirements(filename):
    reqs = list()
    with io.open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            reqs.append(line.strip())
    return reqs


setup(
    name='coronavirus_daily_data',
    version='1',
    packages=find_packages(),
    url="https://www.github.com/alvarobartt/coronavirus_daily_data",
    download_url='https://github.com/alvarobartt/coronavirus_daily_data/archive/1.tar.gz',
    license='MIT License',
    author='Alvaro Bartolome del Canto',
    author_email='alvarob96@usal.es',
    description='coronavirus_daily_data — Coronavirus (COVID-19) Daily Data from Worldometer with Python',
    long_description=readme(),
    long_description_content_type='text/markdown',
    install_requires=requirements(filename='requirements.txt'),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries"
    ],
    extras_require={
        "docs": requirements(filename='docs/requirements.txt'),
        "tests": requirements(filename='tests/requirements.txt'),
    },
    python_requires='>=3',
    project_urls={
        'Bug Reports': 'https://github.com/alvarobartt/coronavirus_daily_data/issues',
        'Source': 'https://github.com/alvarobartt/coronavirus_daily_data',
        'Documentation': 'https://coronavirus_daily_data.readthedocs.io/'
    },
)