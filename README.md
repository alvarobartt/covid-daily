# 🦠 COVID-19 Daily Data 🦠

[![Python Version](https://img.shields.io/pypi/pyversions/covid_daily.svg)](https://pypi.org/project/covid_daily/)
[![PyPi Version](https://img.shields.io/pypi/v/covid_daily.svg)](https://pypi.org/project/covid_daily/)
[![Package Status](https://img.shields.io/pypi/status/covid_daily.svg)](https://pypi.org/project/covid_daily/)
[![Build Status](https://github.com/alvarobartt/covid-daily/workflows/covid_daily/badge.svg)](https://github.com/alvarobartt/covid-daily)
[![Documentation Status](https://readthedocs.org/projects/covid_daily/badge/?version=latest)](https://covid_daily.readthedocs.io/)

This repository allows any user to easily download COVID-19 daily data from [Worldometers](https://www.worldometers.info/coronavirus/). Data is disaggregated per country, so you can retrieve COVID real time daily data from your own country and analyze it.

## Contents

* `scraper/`: contains the Jupyter Notebooks where the Web Scraper was developed and the "scripts" so as to download all the data by yourself.
* `covid_daily/`: this is the Python Package directory, which contains the previously developed functions integrated into a simple Python package so that any user can easily access the data by themselves.
* `data/`: contains a folder per country with all the available data as provided by Worldometers.
* `tests/`: contains the tests using pytest to ensure that after each commit the package is still working properly.
* `docs/`: contains the generated sphinx documentation, but you can see it at https://covid_daily.readthedocs.io

## Features

- Detailed data from every country available at worldometers.info/coronavirus, which is indeed every country affected by the pandemic.
- Data is updated daily so you can track its evolution day by day.
- A general overview on how the pandemic is affecting every country (real-time).

## Installation

In order to get this package working you will need to **install it via pip** (with a Python3.5 version or higher) on the terminal by typing:

``$ pip install covid_daily``

## Documentation

You can find the **complete developer documentation** at: https://covid_daily.readthedocs.io/, hosted on [Read the Docs](https://readthedocs.org/) and generated using [sphinx](https://www.sphinx-doc.org/en/master/) with the theme [sphinx_rtd_theme](https://github.com/readthedocs/sphinx_rtd_theme) which is the standard Read the Docs theme for sphinx.

## Kaggle

You can find a Kaggle Notebook explaining all the features on detail and providing some useful plots at: https://www.kaggle.com/alvarob96/covid-daily-data-retrieval-plot. Make sure to upvote the Kaggle Notebook and follow me at Kaggle so as to stay tuned for all the updates: https://www.kaggle.com/alvarob96

## Usage

### Retrieve the World's overview

```python
import covid_daily

overview = covid_daily.overview(as_json=False)

print(overview.head())
```

As already mentioned, this function retrieves an overview of the COVID-19 from all the available countries as indexed in Worldometers.info/coronavirus

```{r, engine='python', count_lines}
  Country,Other  TotalCases  NewCases  TotalDeaths  NewDeaths  TotalRecovered  \
0         World     6282377     23127       374232        535         2854425   
1           USA     1837170         0       106195          0          599867   
2        Brazil      514992       143        29341         27          206555   
3        Russia      414878      9035         4855        162          175877   
4         Spain      286509         0        27127          0          196958   

   ActiveCases  Serious,Critical  TotCases/1M pop  Deaths/1M pop  TotalTests  \
0      3053720             53397              806             48           0   
1      1131108             17075             5553            321    17672567   
2       279096              8318             2424            138      930013   
3       234146              2300             2843             33    10923108   
4        62424               617             6128            580     4063843   

   Tests/1M pop  Population  
0             0           0  
1         53417   330843477  
2          4378   212434518  
3         74852   145929507  
4         86921    46753345  
```

### Retrieve chart's data from every country

```python
import covid_daily

data = covid_daily.data(country='spain', chart='total-currently-infected-linear', as_json=False)

print(data.head())
```

Which returns a `pandas.DataFrame` containing all the information provided by Worldometers related to the total amoun of infected people because of the COVID-19 in Spain, in this case.

```{r, engine='python', count_lines}
            Currently Infected
Date                          
2020-05-09               63148
2020-05-10               61603
2020-05-11               63553
2020-05-12               62130
2020-05-13               60764
```

Note that this functions lets the user change the country and the chart type from which data will be retrieved, containing different statistics. All the available countries can be found at [AVAILABLE_COUNTRIES](https://github.com/alvarobartt/covid-daily/blob/7400dce5157e562858a9eff9dffea6694d198d32/covid_daily/constants.py#L1) and all the available chart types at [AVAILABLE_CHARTS](https://github.com/alvarobartt/covid-daily/blob/7400dce5157e562858a9eff9dffea6694d198d32/covid_daily/constants.py#L41).

### Retrieve & Plot all the available charts for any country

```python
import covid_daily
from covid_daily.constants import AVAILABLE_CHARTS

import matplotplib.pyplot as plt

fig, axs = plt.subplots(3, 3, figsize=(20,15))

from itertools import product

pairs = list(product((range(3)), (range(3))))

for idx, available_chart in enumerate(AVAILABLE_CHARTS):
    data = covid_daily.data(country='spain', chart=available_chart, as_json=False)
    data.plot(ax=axs[pairs[idx]], title=available_chart)

fig.tight_layout()
fig.show()
```

The resulting figure containing all the data (charts) from Spain, as previously retrieved, is shown below, generated after the previous code block.

<p align="center">
  <img src="https://raw.githubusercontent.com/alvarobartt/covid-daily/master/docs/_static/covid-daily-plot.png"/>
</p>


## Contribute

As this is an open source project it is **open to contributions, bug reports, bug fixes, documentation improvements, enhancements and ideas**. There is an open tab of [issues](https://github.com/alvarobartt/covid-daily/issues) where anyone can open new issues if needed or navigate through them in order to solve them or contribute to its solving. Remember that **issues are not threads to describe multiple problems**, this does not mean that issues can't be discussed, but so to keep a structured project management, the same issue should not describe different problems, just the main one and some nested/related errors that may be found.

## Citation

When citing this repository on your publications please use the following **BibTeX** citation:

```
@misc{
    covid_daily,
    author = { Alvaro Bartolome del Canto },
    title = { covid_daily - COVID-19 Daily Data from Worldometers with Python },
    year = { 2020 },
    publisher = {GitHub},
    journal = {GitHub Repository},
    howpublished = {\url{https://github.com/alvarobartt/covid-daily}}
}
```

### All the data contained in this repository is updated once a day until the COVID-19 pandemic ends.