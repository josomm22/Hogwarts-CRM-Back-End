import datetime

def makeTimeStamp():
    now = datetime.datetime.now()
    date = now.strftime("%d/%m/%Y %H:%M:%S")
    return date
