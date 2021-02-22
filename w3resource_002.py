import sys
import datetime
from math import pi
now = datetime.datetime.now()
print("Current date and time :")
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print("Python version")
print(sys.version)
print("Version info")
print(sys.version_info)

r = float(input("Input the radius of the circle :"))
print("The area of the circle with radius " + str(r) + " is: " + str(pi * r **2))

fname = input("Input your First Name : ")
lname = input("Input  your Last Name : ")
print ("Hello " + lname + " " + fname)