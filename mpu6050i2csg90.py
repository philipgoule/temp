#!/usr/bin/python
import smbus
import math
import os
import time
import time
import RPi.GPIO as GPIO
import signal
import atexit
import numpy as np
# Power management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val

def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def dist(a,b):
    return math.sqrt((a*a)+(b*b))

def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)


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
	bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards
	address = 0x69       # This is the address value read via the i2cdetect command

# Now wake the 6050 up as it starts in sleep mode
#bus.write_byte_data(address, power_mgmt_1, 0)
#S = [0]*2
#Y = [0]*2
#K = [0]*2
#P = [0]*2

#S[0] = read_word_2c(0x43)
#Y[0] = 1
#K[0] = 1
#P[0] = 1
#Noise_std_ = 1  #np.square(np.var(Noise_std))  
#Noise_     = 1   #np.square(np.var(Noise))

#while 1:
	i=os.system('clear')
	print "gyro data"
	print "---------"
	
	#gyro_xout = read_word_2c(0x43)
#	P[1] =  np.square(P[0]) + 0.1*Noise_
# 	K[1] =  0.1*np.sqrt( P[1]/( Noise_std_ + P[1]))
# 	Y[1] =  Y[0] + K[1] * (S[1] - Y[0])
# 	P[1] =  np.sqrt((1-K[1])*P[1])
	gyro_xout = read_word_2c(0x43)
	gyro_yout = read_word_2c(0x45)
	gyro_zout = read_word_2c(0x47)
	
	print "gyro_xout: ", gyro_xout, " scaled: ", (gyro_xout / 131)
	print "gyro_yout: ", gyro_yout, " scaled: ", (gyro_yout / 131)
	print "gyro_zout: ", gyro_zout, " scaled: ", (gyro_zout / 131)
#	P[0] = P[1]
#	K[0] = K[0]
#	Y[0] = Y[1]
#	S[0] = S[1]
	print
	print "accelerometer data"
	print "------------------"
	
	accel_xout = read_word_2c(0x3b)
	accel_yout = read_word_2c(0x3d)
	accel_zout = read_word_2c(0x3f)
		
	accel_xout_scaled = accel_xout / 16384.0
	accel_yout_scaled = accel_yout / 16384.0
	accel_zout_scaled = accel_zout / 16384.0
	
	print "accel_xout: ", accel_xout, " scaled: ", accel_xout_scaled
	print "accel_yout: ", accel_yout, " scaled: ", accel_yout_scaled
	print "accel_zout: ", accel_zout, " scaled: ", accel_zout_scaled
	
	print "x rotation: " , get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)
	print "y rotation: " , get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)

    	gx = -1.0 * accel_xout / 100.0
    	gy = -1.0 * accel_yout / 100.0
    	gz = accel_zout / 100.0
    	gxy = ((gx**2) + (gy**2))**0.5
    	gxyz = ((gx ** 2) + (gy ** 2) + (gz ** 2)) ** 0.5
    	if gy >= 0.0:
    	    sg901 = math.acos(gx/gxy) 
    	    sg902 = math.asin(gxy/gxyz) + (0.5*math.pi)
    	if gy < 0.0:
    	    sg901 = math.acos(-gx / gxy) 
    	    sg902 = -math.asin(gxy / gxyz) + (0.5 * math.pi)
    	
    	
    	    if sg902 <(math.pi * 40.0 / 180.0):
    	        sg902 = (math.pi * 40.0 / 180.0)
    	print(sg901)
        print(sg902)
	sg901 = sg901 / math.pi * 180
        sg902 = sg902 / math.pi * 180
    	print(sg901)
    	print(sg902)
    	p1.ChangeDutyCycle(2.5 + (10.0 * sg901 / 180.0))
    	p2.ChangeDutyCycle(2.5 + (10.0 * sg902 / 180.0))
    	time.sleep(0.1)
