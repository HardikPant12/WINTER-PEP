# Math
"""
import math as m

print(m.sqrt(9))                #sqaure root
print(m.pow(2,5))         #Power
print(m.factorial(5))           # print factorial of number
print(m.ceil(10.33))            #print next whole number
print(m.floor(10.33))           #print before whole number
print(m.fabs(-10.2))            #it will give positive number
print(m.pi)                     # gives pi value
"""

# Random Function :
import random
from calendar import month

# Picking number from dice
"""
x = random.randint(1,6)
print(x)
"""

#choosing random from list
"""
student = ["rahul","rohit","shubham","hardik"]

x = random.choice(student)
print(x)
"""

# otp generator
"""
otp = random.randint(1000,9999)
print("Otp =",otp)
"""


import datetime
"""
current = datetime.datetime.now()
print(current)
print(current.date())
print(current.month)
print(current.year)
print(current.time())
print(current.second)

"""

#diffrence b/w two dates:
"""
date1 = datetime.date(2026,1,1)
date2 = datetime.date(2026,1,28)
diff = date2-date1
print(diff)

"""

#no. of days on earth
"""
x = datetime.datetime.now()

d1 = x.date()
d2 = datetime.date(2006,5,3)

b = d1-d2
print("Hardik =",b)
"""
"""
d1 = x.date()
d2 = datetime.date(2006,8,19)

b = d1-d2
print("Charan =",b)
"""

#--------------------------------------------------------------------------------------------------------------------------#

#Counter in Python :

# from collections import Counter
"""
lst = [2,1,2,2,3,4,5,1,2]
print(Counter(lst))
"""

# Counter in List:
"""
lst2 = ["apple","banana","apple","grapes","banana","mango","apple","banana"]
print(Counter(lst2))

"""

# Counter in String:
"""
txt = "Hello"
print(Counter(txt))
"""

# Counter after using split
"""
x = "python is easy and python is powerful"
y = x.split(" ")                    #Converting string to list
print(Counter(y))
"""

import os
"""
current_path = os.getcwd()                          #Shows current working directory
print(current_path)
"""

"""
item = os.listdir()                                 # list all the item present in current folder
print(item)
"""

# TO create folder in current directory
"""
folder_name = "myFolder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("folder created successfully")
else:
    print("folder already exists")

"""

# we have a file  notes.py if this is present in cd or not

file = "python.py"

if not os.path.exists(file):
    print("File doesn't exist")
else:
    print("File already exists")
