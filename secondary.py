import datetime as datetime

def makeTimeStamp():
    now = datetime.now()
    date = now.strftime("%d/%m/%Y %H:%M:%S")
    return date
