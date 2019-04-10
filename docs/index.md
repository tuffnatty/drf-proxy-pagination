<div class="badges">
    <a href="http://travis-ci.org/tuffnatty/drf-proxy-pagination">
        <img src="https://travis-ci.org/tuffnatty/drf-proxy-pagination.svg?branch=master">
    </a>
    <a href="https://pypi.python.org/pypi/drf-proxy-pagination">
        <img src="https://img.shields.io/pypi/v/drf-proxy-pagination.svg">
    </a>
</div>

---

# drf-proxy-pagination

Pagination class for Django REST Framework to choose pagination class by query parameter

---

## Overview

Pagination class for Django REST Framework to choose pagination class by query parameter

## Requirements

* Python (2.7, 3.4+)
* Django (1.8+)
* Django REST Framework (3.1+)

## Installation

Install using `pip`...

```bash
$ pip install drf-proxy-pagination
```

In your `settings.py`, choose `ProxyPagination` as your default pagination class
and configure it:

```python
REST_FRAMEWORK = {
    ...
    DEFAULT_PAGINATION_CLASS = 'pagination_proxy.ProxyPagination',
}
PROXY_PAGINATION_PARAM = 'pager'
PROXY_PAGINATION_DEFAULT = 'rest_framework.pagination.LimitOffsetPagination'
PROXY_PAGINATION_MAPPING = {
    'cursor': 'rest_framework.pagination.CursorPagination',
}
```

## Example

http://api.example.org/accounts/ gives default pagination.
http://api.example.org/accounts/?pager=cursor gives CursorPagination for heavy queries.

## Testing

Install testing requirements.

```bash
$ pip install -r requirements.txt
```

Run with runtests.

```bash
$ ./runtests.py
```

You can also use the excellent [tox](http://tox.readthedocs.org/en/latest/) testing tool to run the tests against all supported versions of Python and Django. Install tox globally, and then simply run:

```bash
$ tox
```

## Documentation

To build the documentation, you'll need to install `mkdocs`.

```bash
$ pip install mkdocs
```

To preview the documentation:

```bash
$ mkdocs serve
Running at: http://127.0.0.1:8000/
```

To build the documentation:

```bash
$ mkdocs build
```
