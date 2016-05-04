from datetime import date, timedelta, datetime

def add_gigasecond():
  return timedelta(0, 10**9)

now = datetime.now()
today = date.today()

print '%s/%s/%s' %(now.year,now.month,now.day)
print now + timedelta(0, 10**9)
