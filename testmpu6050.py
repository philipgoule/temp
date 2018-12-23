#! /usr/bin/env python
import os
import time
from mpu6050 import mpu6050
sensor = mpu6050(0x69)
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
	time.sleep(0.3)
