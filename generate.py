import time
import datetime
import re

def update():
    date = datetime.date(2019, 5, 7)
    diff_date = datetime.timedelta(days=1)
    another_date = date + diff_date
    return another_date

# print(update())

def readFile():
    with open("generate.py") as f:
        return f.read()

string = readFile()

newStr = re.sub(r'datetime\.date\([0-9]+, [0-9]+, [0-9]+\)', repr(update()), string)
# print(newStr)

def writeFile():
    with open("generate.py", "w") as f:
        f.write(newStr)

writeFile()