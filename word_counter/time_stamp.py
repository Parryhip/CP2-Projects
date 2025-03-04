#Samuel Andelin, Word Counter

#importing datetime
import datetime

#timestamp function
def time_stamp():
    #gets the info about now
    now = datetime.datetime.now()
    #if the hour is greater than 12, change it from military time to standard time with pm
    if now.hour > 12:
        am_pm = "PM"
        newhour = str(int(now.hour)-12)
    #if the hour is less than 1 set the type of time to am
    else:
        am_pm = "AM"
        #if the hour is 0, change it to 12 am to make it more easy to understand
        if now.hour == "0":
            newhour = str(int(now.hour) + 12)

    #returns the hour, minute, and am/pm
    return f"{newhour}:{now.minute} {am_pm}"