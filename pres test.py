# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 23:49:46 2021

@author: binzd
"""

# Importing Libraries
import serial
import time
#import matplotlib.pyplot as plt
arduino = serial.Serial(port='COM9', baudrate=9600, timeout=.1)
speed = str(255) # Taking input from user
distance = str(15)
message = bytes("p," + speed + ',d,' + distance + '\n', "utf-8")
arduino.write(message)
dictionary1 = {}
xlist = []
ylist = []
list1 = []
originaltime = time.time()
currenttime = originaltime
while currenttime < (originaltime + 5):
    value = arduino.readline()
    str_value = value.decode("utf-8")
    list1.append(str_value.split())
    #splitList = value.split(' ')
    print(str_value) # printing the value
    #xlist.append(splitList(0))
    #ylist.append(splitList(1))
    currenttime = time.time()
#plt.plot(xlist, ylist)