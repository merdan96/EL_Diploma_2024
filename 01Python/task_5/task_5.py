#! /usr/bin/python
import calendar

tc= calendar.TextCalendar(firstweekday=5)

year = int(input("Please Enter a Year : "))
month = int(input("Please Enter a Month : "))

tc.prmonth(year,month,3,2)