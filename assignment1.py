#!/usr/bin/env python3

'''
OPS445 Assignment 1
Program: assignment1.py 
Author: "Sanjib Shrestha"
Semester: "Summer 2026"

The python code in this file (assignment1.py) is original work written by
"Student Name". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
''
#!/usr/bin/env python3

'''

import sys


def leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def mon_max(month: int, year: int) -> int:
    feb_max = 29 if  leap_year(year) else 28

    month_days = {
        1: 31, 2: feb_max, 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31,
        9: 30, 10: 31, 11: 30, 12: 31
    }

    return month_days[month]


def after(date: str) -> str:
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)

    tmp_day = day + 1

    if tmp_day > mon_max(month, year):
        to_day = 1
        tmp_month = month + 1
    else:
        to_day = tmp_day
        tmp_month = month

    if tmp_month > 12:
        to_month = 1
        year += 1
    else:
        to_month = tmp_month

    return f"{year}-{to_month:02}-{to_day:02}"


def day_of_week(date: str) -> str:
    # FIXED: correct order is year-month-day
    year, month, day = date.split('-')
    year = int(year)
    month = int(month)
    day = int(day)

    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    offset = {
        1: 0, 2: 3, 3: 2, 4: 5,
        5: 0, 6: 3, 7: 5, 8: 1,
        9: 4, 10: 6, 11: 2, 12: 4
    }

    if month < 3:
        year -= 1

    return days[(year + year // 4 - year // 100 + year // 400 + offset[month] + day) % 7]


def valid_date(date: str) -> bool:
    parts = date.split('-')

    if len(parts) != 3:
        return False

    year, month, day = parts

    # must be numeric
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return False

    # MUST be 4-digit year (THIS FIXES YOUR ERROR)
    if len(year) != 4:
        return False

    year = int(year)
    month = int(month)
    day = int(day)

    if month < 1 or month > 12:
        return False

    if day < 1 or day > mon_max(month, year):
        return False

    return True
def day_count(start_date: str, end_date: str) -> int:
    weekend_count = 0
    current_date = start_date

    while current_date <= end_date:
        dow = day_of_week(current_date)
        if dow in ('sat', 'sun'):
            weekend_count += 1
        current_date = after(current_date)

    return weekend_count


def usage():
    print(f"Usage: {sys.argv[0]} YYYY-MM-DD YYYY-MM-DD")
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()

    date1 = sys.argv[1]
    date2 = sys.argv[2]

    if not valid_date(date1) or not valid_date(date2):
        usage()

    if date1 <= date2:
        start_date = date1
        end_date = date2
    else:
        start_date = date2
        end_date = date1

    count = day_count(start_date, end_date)

    print(f"The period between {start_date} and {end_date} includes {count} weekend days.")
