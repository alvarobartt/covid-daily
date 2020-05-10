# 🦠 :earth_africa: Coronavirus (COVID-19) Daily Data 🦠 :earth_africa:

This repository contains a complete Python Web Scraper which retrieves all the data provided by [Worldometer](https://www.worldometers.info/coronavirus/) related to the Coronavirus (COVID-19) pandemic. So on, all the data available from every country is retrieved and transformed into CSV files using a simple Python script.

## TODO

- Check README.md and explain package usage
- Include real time data on the package so as to let the users keep a real time tracking of the virus such as the website does.
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

coronavirus_daily_data.overview()
```

So on, the previous piece of code outputs the following line:

```{r, engine='python', count_lines}
    Country,Other TotalCases NewCases TotalDeaths NewDeaths  ... Serious,Critical TotCases/1M pop Deaths/1M pop TotalTests Tests/1M pop
0           World  4,125,046  +26,758     280,957      +733  ...           47,637             529          36.0        NaN          NaN
1             USA  1,347,325      +16      80,041        +4  ...           16,816           4,070           242  8,918,345       26,943
2           Spain    264,663   +1,880      26,621      +143  ...            1,741           5,661           569  2,467,761       52,781
3           Italy    218,268      NaN      30,395       NaN  ...            1,034           3,610           503  2,514,234       41,584
4              UK    215,260      NaN      31,587       NaN  ...            1,559           3,171           465  1,728,443       25,461
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