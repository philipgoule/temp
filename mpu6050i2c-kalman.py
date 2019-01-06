#!/usr/bin/python
import smbus
import math
import os
import time
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



#while 1:
bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards
address = 0x69       # This is the address value read via the i2cdetect command

# Now wake the 6050 up as it starts in sleep mode
bus.write_byte_data(address, power_mgmt_1, 0)
S = [0]*2
Y = [0]*2
K = [0]*2
P = [0]*2
N = [0]*3
Y[0] = 1
K[0] = 1
P[0] = 1


Noise_std_ = 1  #np.square(np.var(Noise_std))  
Noise_ = 1   #np.square(np.var(Noise))

while 1:
	i=os.system('clear')
	print "gyro data"
	print "---------"
	#for k in range(1,3):
	N[0] = read_word_2c(0x43)
	N[1] = read_word_2c(0x43)
	N[2] = read_word_2c(0x43)
	Noise_std_ = np.square(np.var(N))  
	Noise_ = np.square(np.var(N))


	#gyro_xout = read_word_2c(0x43)
	S[1] =  read_word_2c(0x43)
	P[1] =  np.square(P[0]) + 0.3*Noise_
 	K[1] =  0.1*np.sqrt( P[1]/( Noise_std_ + P[1]))
 	Y[1] =  Y[0] + K[1] * (S[1] - Y[0])
 	P[1] =  np.sqrt((1-K[1])*P[1])
	gyro_xout = P[1]
	gyro_yout = read_word_2c(0x45)
	gyro_zout = read_word_2c(0x47)
	
	print "gyro_xout: ", gyro_xout, " scaled: ", (gyro_xout / 131)
	print "gyro_yout: ", gyro_yout, " scaled: ", (gyro_yout / 131)
	print "gyro_zout: ", gyro_zout, " scaled: ", (gyro_zout / 131)
	P[0] = P[1]
	K[0] = K[1]
	Y[0] = Y[1]
	S[0] = S[1]
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
	time.sleep(0.3)
