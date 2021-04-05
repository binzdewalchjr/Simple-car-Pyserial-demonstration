# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 09:48:41 2021

@author: binzd
"""

# Importing Libraries
import serial
import time
#import matplotlib.pyplot as plt
arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data
speed = input("Enter a motor speed: ") # Taking input from user
distance = input("Enter a distance: ")
message = speed + ',' + distance + '\n'
arduino.write(message)
dictionary1 = {}
xlist = []
ylist = []
time.clock_gettime()
while True:
    value = arduino.read()
    splitList = value.split(' ')
    print(splitList) # printing the value
    xlist.append(splitList(0))
    ylist.append(splitList(1))

#plt.plot(xlist, ylist)

    
    