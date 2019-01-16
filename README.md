# Steam Groups
 
[![Build status][build image]][build]
[![Updates][dependency image]][pyup]
[![Python 3][python3 image]][pyup]
[![Code coverage][codecov image]][codecov]

  [build]: https://travis-ci.org/woctezuma/steam-groups
  [build image]: https://travis-ci.org/woctezuma/steam-groups.svg?branch=master

  [pyup]: https://pyup.io/repos/github/woctezuma/steam-groups/
  [dependency image]: https://pyup.io/repos/github/woctezuma/steam-groups/shield.svg
  [python3 image]: https://pyup.io/repos/github/woctezuma/steam-groups/python-3-shield.svg

  [codecov]: https://codecov.io/gh/woctezuma/steam-groups
  [codecov image]: https://codecov.io/gh/woctezuma/steam-groups/branch/master/graph/badge.svg

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
