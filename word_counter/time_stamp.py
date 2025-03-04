#Samuel Andelin, Word Counter

#importing datetime
import datetime

#timestamp function
def time_stamp():
    now = datetime.datetime.now()
    if now.hour > 12:
        am_pm = "PM"
        newhour = str(int(now.hour)-12)
    else:
        am_pm = "AM"
        if now.hour == "0":
            newhour = str(int(now.hour) + 12)

    return f"{newhour}:{now.minute} {am_pm}"