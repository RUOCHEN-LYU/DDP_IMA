"""
Date Scheduler Function

Objective:
Write a function named 'date_passed' to determine the relationship between two dates.

Function Parameters:
1. todays_date (string): The current date in the format 'day Month'.
2. scheduled_date (string): The scheduled date to compare, in the same format.

Instructions:
- The function should compare todays_date and scheduled_date and print whether the scheduled date has passed, is yet to pass, or is today.
- Assume the dates are in the same year.
- The dates are in a format like '26th March'. Consider how to convert these for comparison.
- https://www.w3schools.com/python/python_datetime.asp

Example Test Cases:
1. date_passed('26th March', '25th March') should indicate that the scheduled date has passed.
2. date_passed('26th March', '26th March') should indicate that the scheduled date is today.
3. date_passed('26th March', '27th March') should indicate that the scheduled date is yet to pass.
"""

from datetime import datetime

def date_passed(todays_date, scheduled_date):
    """
    Determines the relationship between today's date and a scheduled date.

    Parameters:
    todays_date (str): The current date in the format 'day Month' (e.g., '26 March').
    scheduled_date (str): The scheduled date to compare, in the same format.

    Returns:
    str: A message indicating whether the scheduled date has passed, is yet to pass, or is today.
    """

    # Helper function to convert date from 'dayth Month' format to 'day Month'
    def convert_date(date_str):
        # Splitting the date into day and month parts
        day, month = date_str.split(' ')
        # Removing any ordinal suffix (st, nd, rd, th) from the day part
        day = ''.join(filter(str.isdigit, day))
        # Reassembling the date
        return f"{day} {month}"

    # Converting dates
    todays_date = convert_date(todays_date)
    scheduled_date = convert_date(scheduled_date)

    # Formatting dates for comparison
    date_format = "%d %B"
    todays_date_formatted = datetime.strptime(todays_date, date_format)
    scheduled_date_formatted = datetime.strptime(scheduled_date, date_format)

    # Comparing dates
    if todays_date_formatted < scheduled_date_formatted:
        return "The scheduled date is yet to pass."
    elif todays_date_formatted > scheduled_date_formatted:
        return "The scheduled date has passed."
    else:
        return "The scheduled date is today."

# Test cases
date_passed("26 March", "25 March")  # Past date
date_passed("26 March", "26 March")  # Today's date
date_passed("26 March", "27 March")  # Future date

print(date_passed("26 March", "25 March"))
print(date_passed("26 March", "26 March"))
print(date_passed("26 March", "27 March"))


