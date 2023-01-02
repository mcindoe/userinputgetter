from enum import Enum
import re

day_regex_str = "(0[1-9]|[12][0-9]|3[01])"
month_regex_str = "(0[1-9]|1[012])"
year_regex_str = "[0-9]{4}"


class _DateFormat(Enum):
    def __init__(self, fmt, regex):
        self.fmt = fmt
        self.regex = regex

    YearDashMonthDashDay = (
        "%Y-%m-%d",
        re.compile(f"^{year_regex_str}-{month_regex_str}-{day_regex_str}$")
    )
    YearSlashMonthSlashDay = (
        "%Y/%m/%d",
        re.compile(f"^{year_regex_str}/{month_regex_str}/{day_regex_str}$")
    )
    DayDashMonthDashYear = (
        "%d-%m-%Y",
        re.compile(f"^{day_regex_str}-{month_regex_str}-{year_regex_str}$")
    )
    DaySlashMonthSlashYear = (
        "%d/%m/%Y",
        re.compile(f"^{day_regex_str}/{month_regex_str}/{year_regex_str}$")
    )
    DayMonthYear = (
        "%d%m%Y",
        re.compile(f"^{day_regex_str}{month_regex_str}{year_regex_str}$")
    )
    DaySlashMonth = (
        "%d-%m",
        re.compile(f"^{day_regex_str}-{month_regex_str}$")
    )
