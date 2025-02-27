#Samuel Andelin, Word Counter

#importing datetime
import datetime

#timestamp function
def time_stamp():
    now = datetime.datetime.now()
    return f"{now.hour}:{now.minute}"