import datetime

a=datetime.datetime(2026,11,25,22,28,10)

print(a.strftime("%dth %B,%Y"))
print(a)
print(a.date())
print(a.time())
print(a.year)
print(a.month)

print(datetime.datetime.now())
