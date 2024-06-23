import datetime
from datetime import timedelta


def get_located_week_start_date(a_date: datetime.date) -> datetime.date:
    """
    get the start date of week which input date located
    """
    date_index = a_date.weekday()
    return a_date - timedelta(days=date_index)


def get_week_anchor_date(a_date: datetime.date) -> datetime.date:
    """
    The fourth day of week determine the year and month that week located
    """
    assert isinstance(a_date, datetime.date)
    start_date = get_located_week_start_date(a_date)
    return start_date + timedelta(days=3)


def get_weeks_offset_between_dates(
    prev_date: datetime.date,
    cur_date: datetime.date,
) -> int:
    """
    Count of week offset from
    the week that prev_date belonging
    to the week that cur_date belonging to
    """
    assert isinstance(prev_date, datetime.date)
    assert isinstance(cur_date, datetime.date)
    assert cur_date >= prev_date
    cur_week_key_date = get_week_anchor_date(cur_date)
    prev_week_key_date = get_week_anchor_date(prev_date)
    return ((cur_week_key_date - prev_week_key_date).days + 1) // 7


def get_start_date_of_monthly_start_week(year: int, month: int) -> datetime.date:
    """
    get the start date of week
    which is the first week of given month
    """
    assert isinstance(year, int)
    assert isinstance(month, int)
    assert year > 0
    assert 1 <= month <= 12
    belonging_month_first_date = datetime.date(year, month, 1)
    first_date_weekday = belonging_month_first_date.weekday()
    if first_date_weekday <= 3:
        date_delta = 3 - first_date_weekday
    else:
        date_delta = 10 - first_date_weekday
    first_week_start_date = belonging_month_first_date + timedelta(days=date_delta) - timedelta(days=3)
    return first_week_start_date


def get_daily_start_date_of_located_daily(a_date: datetime.date) -> datetime.date:
    return a_date


def get_daily_period_idx_of_located_daily(a_date: datetime.date) -> int:
    located_start_date = get_daily_start_date_of_located_daily(a_date)
    return (a_date - located_start_date).days


def get_prev_daily_start_date_from_daily_located(a_date: datetime.date, span_count: int) -> datetime.date:
    cur_start_date = a_date
    return cur_start_date - timedelta(days=span_count)


def get_daily_start_date_of_located_weekly(a_date: datetime.date) -> datetime.date:
    return get_located_week_start_date(a_date)


def get_daily_period_idx_of_located_weekly(a_date: datetime.date) -> int:
    located_start_date = get_daily_start_date_of_located_weekly(a_date)
    return (a_date - located_start_date).days


def get_prev_weekly_start_date_from_daily_located(a_date: datetime.date, span_count: int) -> datetime.date:
    cur_start_date = get_daily_start_date_of_located_weekly(a_date)
    return cur_start_date - timedelta(weeks=span_count)


def get_daily_start_date_of_located_monthly(a_date: datetime.date) -> datetime.date:
    return datetime.date(a_date.year, a_date.month, 1)


def get_daily_period_idx_of_located_monthly(a_date: datetime.date) -> int:
    located_start_date = get_daily_start_date_of_located_monthly(a_date)
    return (a_date - located_start_date).days


def get_prev_monthly_start_date_from_daily_located(a_date: datetime.date, span_count: int) -> datetime.date:
    cur_start_date = get_daily_start_date_of_located_monthly(a_date)
    located_year, located_month = cur_start_date.year, cur_start_date.month

    total_months = (located_year * 12 + located_month) - span_count
    another_year = total_months // 12
    another_month = total_months % 12
    if another_month == 0:
        another_year -= 1
        another_month = 12
    return datetime.date(another_year, another_month, 1)


def get_daily_start_date_of_located_yearly(a_date: datetime.date) -> datetime.date:
    return datetime.date(a_date.year, 1, 1)


def get_daily_period_idx_of_located_yearly(a_date: datetime.date) -> int:
    located_start_date = get_daily_start_date_of_located_yearly(a_date)
    return (a_date - located_start_date).days


def get_prev_yearly_start_date_from_daily_located(a_date: datetime.date, span_count: int) -> datetime.date:
    cur_start_date = get_daily_start_date_of_located_yearly(a_date)
    return datetime.date(cur_start_date.year - span_count, 1, 1)


def get_weekly_start_date_of_located_weekly(a_date: datetime.date) -> datetime.date:
    """
    a_date is the start date of a weekly period
    """
    return a_date


def get_weekly_period_idx_of_located_weekly(a_date: datetime.date) -> int:
    """
    a_date is the start date of a weekly period
    """
    located_start_date = get_weekly_start_date_of_located_weekly(a_date)
    return (a_date - located_start_date).days // 7


def get_prev_weekly_start_date_from_weekly_located(a_date: datetime.date, span_count: int) -> datetime.date:
    cur_start_date = get_weekly_start_date_of_located_weekly(a_date)
    return cur_start_date - timedelta(weeks=span_count)


def get_weekly_start_date_of_located_monthly(a_date: datetime.date) -> datetime.date:
    """
    a_date is the start date of a monthly period
    """
    key_date = get_week_anchor_date(a_date)
    anchor_date = get_start_date_of_monthly_start_week(key_date.year, key_date.month)
    return anchor_date


def get_weekly_period_idx_of_located_monthly(a_date: datetime.date) -> int:
    """
    get the week's index of the month which located
    a_date is the start date of a weekly period
    """
    located_start_date = get_weekly_start_date_of_located_monthly(a_date)
    return (a_date - located_start_date).days // 7


def get_prev_monthly_start_date_from_weekly_located(a_date: datetime.date, span_count: int) -> datetime.date:
    anchor_date = get_week_anchor_date(a_date)
    prev_month_first_day = get_prev_monthly_start_date_from_daily_located(anchor_date, span_count)
    return get_start_date_of_monthly_start_week(prev_month_first_day.year, prev_month_first_day.month)


def get_weekly_start_date_of_located_yearly(a_date: datetime.date) -> datetime.date:
    """
    a_date is the start date of a weekly period
    """
    key_date = get_week_anchor_date(a_date)
    anchor_date = get_start_date_of_monthly_start_week(key_date.year, 1)
    return anchor_date


def get_weekly_period_idx_of_located_yearly(a_date: datetime.date) -> int:
    """
    get the week's index of the year which located
    a_date is the start date of a weekly period
    """
    located_start_date = get_weekly_start_date_of_located_yearly(a_date)
    return (a_date - located_start_date).days // 7


def get_prev_yearly_start_date_from_weekly_located(a_date: datetime.date, span_count: int) -> datetime.date:
    anchor_date = get_week_anchor_date(a_date)
    prev_year_first_day = get_prev_yearly_start_date_from_daily_located(anchor_date, span_count)
    return get_start_date_of_monthly_start_week(prev_year_first_day.year, 1)


def get_monthly_start_date_of_located_monthly(a_date: datetime.date) -> datetime.date:
    """
    a_date is the start date of a monthly period
    """
    return a_date


def get_monthly_period_idx_of_located_monthly(a_date: datetime.date) -> int:  # NOQA
    """
    a_date is the start date of a monthly period
    """
    located_start_date = get_monthly_start_date_of_located_monthly(a_date)
    return a_date.month - located_start_date.month


def get_prev_monthly_start_date_from_monthly_located(a_date: datetime.date, span_count: int) -> datetime.date:
    cur_start_date = get_monthly_start_date_of_located_monthly(a_date)
    return get_prev_monthly_start_date_from_daily_located(cur_start_date, span_count)


def get_monthly_start_date_of_located_yearly(a_date: datetime.date) -> datetime.date:
    """
    a_date is the start date of a monthly period
    """
    return datetime.date(a_date.year, 1, 1)


def get_monthly_period_idx_of_located_yearly(a_date: datetime.date) -> int:
    """
    get the month's index of the year which located
    a_date is the start date of a monthly period
    """
    located_start_date = get_monthly_start_date_of_located_yearly(a_date)
    return a_date.month - located_start_date.month


def get_prev_yearly_start_date_from_monthly_located(a_date: datetime.date, span_count: int) -> datetime.date:
    cur_start_date = get_monthly_start_date_of_located_monthly(a_date)
    return datetime.date(cur_start_date.year - span_count, 1, 1)


def get_yearly_start_date_of_located_yearly(a_date: datetime.date) -> datetime.date:
    """
    a_date is the start date of a yearly period
    """
    return a_date


def get_yearly_period_idx_of_located_yearly(a_date: datetime.date) -> int:  # NOQA
    """
    a_date is the start date of a yearly period
    """
    located_start_date = get_yearly_start_date_of_located_yearly(a_date)
    return a_date.year - located_start_date.year


def get_prev_yearly_start_date_from_yearly_located(a_date: datetime.date, span_count: int) -> datetime.date:
    return datetime.date(a_date.year - span_count, 1, 1)
