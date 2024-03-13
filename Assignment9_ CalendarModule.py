"""
Problem Statement : -
Task

You are given a date. Your task is to find what the day is on that date.

Input Format

A single line of input containing the space separated month, day and year, respectively, in    format.

Constraints

Output Format

Output the correct day in capital letters.
"""
"""
Sample Output :-
Enter the date in format (month day year): 01 22 2024
Day: MONDAY
"""
import datetime
def find_day(month, day, year):
    # Convert input to datetime object
    date_obj = datetime.datetime(year, month, day)
    # Get the weekday as a number (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
    weekday_num = date_obj.weekday()
    # List of weekday names
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    # Return the corresponding weekday in capital letters
    return weekdays[weekday_num].upper()

# Input format: month, day, year separated by spaces
date_input = input("Enter the date in format (month day year): ").split()
month, day, year = map(int, date_input)

# Find the day corresponding to the input date
day_of_week = find_day(month, day, year)
print("Day:", day_of_week)