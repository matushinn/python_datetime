import datetime

now = datetime.datetime.now()

print(now)
print(now.isoformat())
print(now.strftime("%d/%m/%y-%H%M%S%F"))

today = datetime.date.today()
print(today)
print(now.isoformat())
print(now.strftime("%d/%m/%y"))

t = datetime.time(hour=1,minute=10,second=5,microsecond=100)
print(t)


print(now)
d = datetime.timedelta(weeks=1)
e = datetime.timedelta(days=1)
print(now-d+e)

import time
# print("#####")
# time.sleep(2)
# print("#####")
print(time.time())

import os
import shutil
file_name = "test.txt"

if os.path.exists(file_name):
    shutil.copy(file_name,f"{format(file_name)}")

with open(file_name,"w")as f:
    f.write("test")