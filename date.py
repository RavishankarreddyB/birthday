import datetime

today = datetime.date.today()
print(today)
tomorrow = today + datetime.timedelta(days = 1)
print(tomorrow)