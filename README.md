# stock-exchange-graphs

[![Build Status](https://travis-ci.org/wiiitek/stock-exchange-graphs.svg?branch=master)](https://travis-ci.org/github/wiiitek/stock-exchange-graphs)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=wiiitek_stock-exchange-graphs&metric=alert_status)](https://sonarcloud.io/dashboard?id=wiiitek_stock-exchange-graphs)
[![codecov](https://codecov.io/gh/wiiitek/stock-exchange-graphs/branch/master/graph/badge.svg)](https://codecov.io/gh/wiiitek/stock-exchange-graphs)

[![Creative Commons License](https://i.creativecommons.org/l/by-nc/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc/4.0/)  

## Build

Create and activate [venv] for the project (see also [venv on Windows]).

Linux instructions:

```bash
python -m venv ./virtualenv
source ./virtualenv/bin/activate
```

Windows instructions:

```
python -m venv virtualenv
virtualenv\Scripts\activate.bat
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Validate

First ensure you have *venv* activated. Then install [pylint] and run analysis:

```bash
pip install pylint
pylint src tests
```

To run unit tests:

```bash
pip install -U pytest
pytest
```

[venv]: https://www.techcoil.com/blog/how-to-install-python3-venv-on-ubuntu-16-04/
[venv on Windows]: https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html
[pylint]: https://www.pylint.org/
