# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 09:46:24 2021

@author: binzd
"""

# Importing Libraries
import serial
import time
arduino = serial.Serial(port='COM9', baudrate=115200, timeout=.1)
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data
while True:
    num = input("Enter a number: ") # Taking input from user
    value = write_read(num)
    print(value) # printing the value