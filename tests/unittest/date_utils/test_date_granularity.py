import datetime
from unittest import TestCase

from delorean.date_utils.date_granularity import (
    Daily,
    Weekly,
    Monthly,
    Yearly,
)


class DateGranularityDailyTestCase(TestCase):

    def setUp(self):
        self.granularity = Daily()

    def test_name(self):
        self.assertEqual(self.granularity.name, 'daily')

    def test_validate_date_completion(self):
        start_date = datetime.date(2024, 6, 15)
        end_date = datetime.date(2024, 6, 17)
        self.assertTrue(self.granularity.validate_date_completion(start_date, end_date))

    def test_get_date_range_size(self):
        start_date = datetime.date(2024, 6, 15)
        end_date = datetime.date(2024, 6, 17)
        self.assertEqual(
            self.granularity.get_date_range_size(start_date, end_date),
            3,
        )

    def test_get_date_range_size_cross_year(self):
        start_date = datetime.date(2022, 12, 23)
        end_date = datetime.date(2023, 3, 12)
        self.assertEqual(
            self.granularity.get_date_range_size(start_date, end_date),
            80,
        )

    def test_get_date_range_size_with_leap_year(self):
        start_date = datetime.date(2023, 12, 23)
        end_date = datetime.date(2025, 1, 12)
        self.assertEqual(
            self.granularity.get_date_range_size(start_date, end_date),
            387,
        )


class DateGranularityWeeklyTestCase(TestCase):

    def setUp(self):
        self.granularity = Weekly()

    def test_name(self):
        self.assertEqual(self.granularity.name, 'weekly')

    def test_validate_full_weeks(self):
        start_date = datetime.date(2024, 5, 27)
        end_date = datetime.date(2024, 6, 23)
        self.assertTrue(self.granularity.validate_date_completion(start_date, end_date))

    def test_validate_partial_weeks(self):
        start_date = datetime.date(2024, 5, 30)
        end_date = datetime.date(2024, 6, 23)
        self.assertFalse(self.granularity.validate_date_completion(start_date, end_date))

    def test_get_date_range_size(self):
        start_date = datetime.date(2024, 5, 27)
        end_date = datetime.date(2024, 6, 23)
        self.assertEqual(
            self.granularity.get_date_range_size(start_date, end_date),
            4,
        )

    def test_get_date_range_size_cross_year(self):
        start_date = datetime.date(2023, 12, 25)
        end_date = datetime.date(2024, 3, 31)
        self.assertEqual(
            self.granularity.get_date_range_size(start_date, end_date),
            14,
        )


class DateGranularityMonthlyTestCase(TestCase):

    def setUp(self):
        self.granularity = Monthly()

    def test_name(self):
        self.assertEqual(self.granularity.name, 'monthly')

    def test_validate_full_months(self):
        start_date = datetime.date(2024, 1, 1)
        end_date = datetime.date(2024, 6, 30)
        self.assertTrue(self.granularity.validate_date_completion(start_date, end_date))

    def test_validate_full_months_cross_year(self):
        start_date = datetime.date(2023, 2, 1)
        end_date = datetime.date(2024, 2, 29)
        self.assertTrue(self.granularity.validate_date_completion(start_date, end_date))

    def test_validate_partial_months_in_leap_year(self):
        start_date = datetime.date(2023, 12, 1)
        end_date = datetime.date(2024, 2, 28)
        self.assertFalse(self.granularity.validate_date_completion(start_date, end_date))

    def test_get_date_range_size(self):
        start_date = datetime.date(2024, 3, 1)
        end_date = datetime.date(2024, 6, 30)
        self.assertEqual(
            self.granularity.get_date_range_size(start_date, end_date),
            4,
        )

    def test_get_date_range_size_cross_year(self):
        start_date = datetime.date(2022, 11, 1)
        end_date = datetime.date(2023, 3, 31)
        self.assertEqual(
            self.granularity.get_date_range_size(start_date, end_date),
            5,
        )

    def test_get_date_range_size_cross_multiple_years(self):
        start_date = datetime.date(2022, 11, 1)
        end_date = datetime.date(2024, 5, 31)
        self.assertEqual(
            self.granularity.get_date_range_size(start_date, end_date),
            19,
        )


class DateGranularityYearlyTestCase(TestCase):

    def setUp(self):
        self.granularity = Yearly()

    def test_name(self):
        self.assertEqual(self.granularity.name, 'yearly')

    def test_validate_date_completion(self):
        start_date = datetime.date(2023, 1, 1)
        end_date = datetime.date(2024, 12, 31)
        self.assertTrue(self.granularity.validate_date_completion(start_date, end_date))

    def test_validate_partial_years(self):
        start_date = datetime.date(2023, 2, 1)
        end_date = datetime.date(2024, 2, 29)
        self.assertFalse(self.granularity.validate_date_completion(start_date, end_date))

    def test_get_date_range_size(self):
        start_date = datetime.date(2022, 1, 1)
        end_date = datetime.date(2024, 12, 31)
        self.assertEqual(
            self.granularity.get_date_range_size(start_date, end_date),
            3,
        )