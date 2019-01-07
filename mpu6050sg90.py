#! /usr/bin/env python
import os
import time
import RPi.GPIO as GPIO
import signal
import atexit
import math
from mpu6050 import mpu6050
sensor = mpu6050(0x69)
atexit.register(GPIO.cleanup)  
servopin1 = 20
servopin2 = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(servopin1, GPIO.OUT, initial=False)
GPIO.setup(servopin2, GPIO.OUT, initial=False)
p1 = GPIO.PWM(servopin1,50) #50HZ
p2 = GPIO.PWM(servopin2,50) #50HZ
p1.start(0)
p2.start(0)
sg901 = 0.0
sg902 = 0.0
while 1:
    i=os.system('clear')
    accel_data = sensor.get_accel_data()
    print(accel_data['x'])
    print(accel_data['y'])
    print(accel_data['z'])
    gyro_data = sensor.get_gyro_data()
    print(gyro_data['x'])
    print(gyro_data['y'])
    print(gyro_data['z'])
    gx = gyro_data['x']
    gy = gyro_data['y']
    gz = gyro_data['z']
    gxy = ((gx ** 2) + (gy ** 2)) ** 0.5
    gxyz = ((gx ** 2) + (gy ** 2) + (gz ** 2)) ** 0.5
    if gy >= 0.0:
        sg901 = math.acos(gx / gxy) 
        sg902 = math.asin(gxy / gxyz) + (0.5 * math.pi())
    if gy < 0.0:
        sg901 = math.acos(-gx / gxy) 
        sg902 = -math.asin(gxy / gxyz) + (0.5 * math.pi())
        sg901 = sg901 / math.pi() * 180
        sg902 = sg902 / math.pi() * 180
        if sg902 <40.0:
            sg902 = 40.0
    print(sg901)
    print(sg902)
    p1.ChangeDutyCycle(2.5 + 10 * sg901 / 180)
    p2.ChangeDutyCycle(2.5 + 10 * sg902 / 180)
    time.sleep(0.2)
