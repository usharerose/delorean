# DeLorean

**DeLorean** is a simple library, providing compared date range according to your scenario

```python
>>> import datetime
>>> import delorean
>>> kwargs = {
...     'start_date': datetime.date(2024, 6, 10)
...     'end_date': datetime.date(2024, 6, 10)
...     'date_granularity': 'daily',
...     'span_count': 1,
...     'span_granularity': 'daily',
... }
>>> compared_start_date, compared_end_date = delorean.get(**kwargs)
>>> compared_start_date
datetime.date(2024, 6, 9)
>>> compared_end_date
datetime.date(2024, 6, 9)
```

## Development Environment
### Docker (Recommended)
Execute the following commands, which sets up a service with development dependencies and enter into it.
```shell
> make run && make ssh
```
### Poetry
As a precondition, please [install Poetry](https://python-poetry.org/docs/1.7/#installation) which is a tool for dependency management and packaging in Python.

Then update and active the environment.
```shell
> poetry update && poetry shell
```