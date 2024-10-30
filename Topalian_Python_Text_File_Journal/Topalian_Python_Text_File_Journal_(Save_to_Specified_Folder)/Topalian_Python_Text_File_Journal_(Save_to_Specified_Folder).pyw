# Topalian_Python_Text_File_Journal_(Save_to_Specified_Folder).pyw

from datetime import datetime
import calendar
import os

def makeCalendar(year, month):
    # create a text calendar
    # with Monday as first day of week
    cal = calendar.TextCalendar(calendar.MONDAY)
    # format specified month as text
    return cal.formatmonth(year, month)

####

def makeFileWithData():
    # get current date and time
    now = datetime.now()

    # format date and time strings
    dateString = now.strftime("%Y-%m-%d")
    timeAmPm = now.strftime("%I:%M %p")
    timeMilitary = now.strftime("%H:%M")
    timeForTxtName = now.strftime("%I-%M-(%S) %p")
    nameOfFile = dateString + ' ' + timeForTxtName

    # create path to text folder
    textFolder = os.path.join(os.path.dirname(__file__), 'text')

    # make sure that text folder exists
    os.makedirs(textFolder, exist_ok = True)

    # define full path for file inside text folder
    filePath = os.path.join(textFolder, nameOfFile + ".txt")

    # open main output file
    with open(filePath, "w") as file:
        # write date, time, and calendar information to file
        file.write(dateString + "\n")
        file.write("----------------\n")
        file.write(timeAmPm + " Am/Pm\n")
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
Shows a Calendar for October 2024
----------------
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2024
# Topalian_Python_Text_File_Journal_(Save_to_Specified_Folder).pyw
# Version 001 - (2024-10-30)
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

