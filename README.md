# Steam Groups
 
[![Build status][Build image]][Build]
[![Updates][Dependency image]][PyUp]
[![Python 3][Python3 image]][PyUp]
[![Code coverage][Codecov image]][Codecov]

  [Build]: https://travis-ci.org/woctezuma/steam-groups
  [Build image]: https://travis-ci.org/woctezuma/steam-groups.svg?branch=master

  [PyUp]: https://pyup.io/repos/github/woctezuma/steam-groups/
  [Dependency image]: https://pyup.io/repos/github/woctezuma/steam-groups/shield.svg
  [Python3 image]: https://pyup.io/repos/github/woctezuma/steam-groups/python-3-shield.svg

  [Codecov]: https://codecov.io/gh/woctezuma/steam-groups
  [Codecov image]: https://codecov.io/gh/woctezuma/steam-groups/branch/master/graph/badge.svg

> Disclaimer: The Travis build fails because I cannot publicly share my own API key in `data/api_key.txt`.

This repository contains code to analyze the libraries of members of Steam groups.

## Requirements

-   Install the latest version of [Python 3.X](https://www.python.org/downloads/).

-   Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

-   Download the list of members of the Steam group of interest. (cf. `data/README.md`)

-   Download your private Steam API key (cf. `data/README.md`)

-   Call the Python script `steam_groups.py`

```bash
python steam_groups.py
```

-   Call the Python script `aggregate_stats.py`

```bash
python aggregate_stats.py
```
