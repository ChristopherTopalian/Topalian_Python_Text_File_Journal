# Topalian_Python_Text_File_Journal.pyw

from datetime import datetime
import calendar
import os

def makeCalendar(year, month):
    # create a text calendar
    # with Monday as first day of week
    cal = calendar.TextCalendar(calendar.MONDAY)

    # format specified month as text
    calendarText = cal.formatmonth(year, month)

    return calendarText

####

def makeFileWithData():
    # get current date and time
    now = datetime.now()

    # format date YYYY-MM-DD (2024-10-27)
    dateString = now.strftime("%Y-%m-%d")

    # format time AM/PM (02:30 PM)
    timeAmPm = now.strftime("%I:%M %p")

    # format time military (14:30)
    timeMilitary = now.strftime("%H:%M")

    timeForTxtName = now.strftime("%I-%M-(%S) %p")
    nameOfFile = dateString + ', ' + timeForTxtName

    # open main output file
    with open(nameOfFile + ".txt", "w") as file:
        # write date, time, and calendar information to file
        file.write(dateString + "\n")
        file.write("----------------\n")
        file.write(timeAmPm + "\n")
        file.write("----------------\n")
        file.write(timeMilitary + " Military\n")
        file.write("----------------\n")
        file.write(makeCalendar(now.year, now.month))
        file.write("----------------")

####

makeFileWithData()

####

'''
2024-10-27
----------------
02:02 PM
----------------
14:02 Military
----------------
    October 2024
Mo Tu We Th  Fr  Sa  Su
       1    2    3    4    5    6
 7    8    9   10  11  12  13
14  15  16  17  18  19  20
21  22  23  24  25  26  27
28  29  30  31
----------------
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2024
# Topalian_Python_Text_File_Journal.pyw
# Version 001 - (2024-10-30)
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

