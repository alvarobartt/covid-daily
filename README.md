# Coronavirus (COVID-19) Daily Data

This repository contains a complete Python Web Scraper which retrieves all the data provided by [Worldometer](https://www.worldometers.info/coronavirus/) related to the Coronavirus (COVID-19) pandemic. So on, all the data available from every country is retrieved and transformed into CSV files using a simple Python script.

## TODO

- Create a simple Python package so as to let every user retrieve the data they need from Worldometer related to the virus.
- Check README.md and explain package usage
- Include real time data on the package so as to let the users keep a real time tracking of the virus such as the website does.
- ~~Retrieve a complete list of all the affected countries as indexed at Worldometer and store their data on separate directories.~~
- Open call to Data Scientists to use the data and provide daily useful reports which will be included in the README.md or in the Wiki, will be described in the Contribute Section of the README.
- ~~Generate the coronavirus overview as presented at: https://www.worldometers.info/coronavirus/~~
- Include a "Latest Updates" section on the README which will be updated daily too
- Also so as to provide the data in a more generic way, a simple Flask RESTX API will be created using [restx-cookie](https://github.com/alvarobartt/restx-cookie), after developing the Python package so that the API endpoints will just be calls to the package functions
- Include some simple stats in the README so as to provide useful information for the Github users that visit this repository
- and much more to come...

## Features

- Detailed data from every country available at Worldometer, which is indeed every country affected by the pandemic.
- Data is updated daily so you can track its evolution day by day.

## Installation

In order to get this package working you will need to **install it via pip** (with a Python3.5 version or higher) on the terminal by typing:

``$ pip install coronavirus_daily_data``

## Documentation

You can find the **complete developer documentation** at: https://coronavirus_daily_data.readthedocs.io/, hosted on [Read the Docs](https://readthedocs.org/) and generated using [sphinx](https://www.sphinx-doc.org/en/master/) with the theme [sphinx_rtd_theme](https://github.com/readthedocs/sphinx_rtd_theme) which is the standard Read the Docs theme for sphinx.

## Usage

So as to use this Python package, a sample piece of code is presented below:

```python
import coronavirus_daily_data

coronavirus_daily_data.sample_function()
```

So on, the previous piece of code outputs the following line:

```{r, engine='python', count_lines}
"This is a sample function"
```

## Contribute

As this is an open source project it is **open to contributions, bug reports, bug fixes, documentation improvements, enhancements and ideas**. There is an open tab of [issues](https://github.com/alvarobartt/coronavirus_daily_data/issues) where anyone can open new issues if needed or navigate through them in order to solve them or contribute to its solving. Remember that **issues are not threads to describe multiple problems**, this does not mean that issues can't be discussed, but so to keep a structured project management, the same issue should not describe different problems, just the main one and some nested/related errors that may be found.

## Citation

When citing this repository on your publications please use the following **BibTeX** citation:

```
@misc{
    coronavirus_daily_data,
    author = { Alvaro Bartolome del Canto },
    title = { coronavirus_daily_data - Coronavirus (COVID-19) Daily Data from Worldometer with Python },
    year = { 2020 },
    publisher = {GitHub},
    journal = {GitHub Repository},
    howpublished = {\url{https://github.com/alvarobartt/coronavirus_daily_data}}
}
```

### All the data contained in this repository is updated once a day until the Coronavirus pandemic ends

---

<p align="center"><img src="https://i.ibb.co/zhFrbZm/made-with-love.png" width="550" hspace="50"/></p>