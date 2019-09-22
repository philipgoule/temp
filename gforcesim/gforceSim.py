#pylint:disable=C0325
#!/usr/bin/python3
# coding: utf-8
import math
import pygame_sdl2
pygame_sdl2.import_as_pygame()
import sys
import pygame
from pygame.locals import *
import random


G = 100000
WIDTH  = 1080
HEIGHT = 2340
PI = math.pi
STARTBODYCOUNT = 50
STARTBODYSPEED = 50
BLACK = 0,0,0
WHITE = 255,255,255
stars = list()
framerate = 60
force = []
direct = []
forcePower = 0
MAXPATH = 300


pygame.init()
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
myfont = pygame.font.SysFont("DejaVuSans", 64)
clock = pygame.time.Clock()



class Body():
	def __init__(self,id=-1,r=1,mass=3,pos=[500,500],vel=[100,100],col=[255,255,255]):
		self.id = id
		self.mass = mass
		self.r = math.pow(mass/PI*(3.0/4.0),1.0/3.0)
		#self.r = self.calr(self.mass)
		self.pos = pos
		self.vel = vel
		self.col= col
		#self.path = list()
		self.path = [[self.pos[0],self.pos[1]]]
		#self.path.append([100,200])    #for testing
	
	def calr(self):
		'''if not max1:
			max1 = self
		if max1.mass <= self.mass:
			max1 = self
		'''
		#print(math.pow(self.mass/PI*(3.0/4.0),1.0/3.0))
		self.r = math.pow(self.mass/PI*(3.0/4.0),1.0/3.0)
		return self.r
		
	def show(self):
		global SCREEN
		pygame.draw.circle(SCREEN,self.col,self.pos,self.r,self.r)
			
	def update(self):
		self.pos[0] = self.pos[0] + self.vel[0]
		self.pos[1] = self.pos[1] + self.vel[1]
		self.path.append(self.pos)
		
		if((len(self.path) > MAXPATH) and (len(stars) > 10)):
			del self.path[0]
		if(len(self.path) > (MAXPATH*3)):
			del self.path[0]
		
		 #下面反弹效果这部分给注释了.留着或者能挽救下跑出屏幕的可怜星星
		if(self.pos[0] <= -WIDTH*2) or (self.pos[0] >= WIDTH*2):
			self.vel[0] *= -1
		if(self.pos[1] <= -HEIGHT*2) or (self.pos[1] >= HEIGHT*2):
			self.vel[1] *= -1
			
	def showPath(self):
		closed = False
		global SCREEN
		pygame.draw.aalines(SCREEN,self.col,closed,self.path,1)

other = Body()

def attract(body):
	global other
	global direct
	global force
	global forcePower
	for i in range(0,len(stars)-1):
		other = stars[i]
		if other.id == body.id:
			continue
		direct = [body.pos[0] - other.pos[0] ,body.pos[1] - other.pos[1]]
		if(math.sqrt(direct[0]**2+direct[1]**2) <= (body.r+other.r)):
			if(body.mass>=other.mass):
				body.vel[0] =  (body.vel[0] * body.mass + other.vel[0] * other.mass)/(body.mass + other.mass)
				body.vel[1] =  (body.vel[1] * body.mass + other.vel[1] * other.mass)/(body.mass + other.mass)
				body.mass = body.mass + other.mass
				body.r = body.calr()
				del stars[i]
			continue

		forcePower = G * (body.mass + other.mass)/(direct[0] ** 2 + direct[1] ** 2)
		force = [forcePower * direct[0]/math.sqrt(direct[0]**2+direct[1]**2),forcePower * direct[1]/math.sqrt(direct[0]**2+direct[1]**2)]
		other.vel = [(other.vel[0]+force[0])/other.mass*(1/framerate),(other.vel[1]+force[1])/other.mass*(1/framerate)]

def setup():
	startBodyMass = [500,10000]
	for i in range(0,STARTBODYCOUNT-1):
    #stars[i] = Body(id=i,r=1,mass=random.uniform(startBodyMass[0],startBodyMass[1]),pos=[random.uniform(100,1500),random.uniform(100,800)],vel=[random.uniform(0,STARTBODYSPEED),random.uniform(0,STARTBODYSPEED)],col=[random.randint(0,255),random.randint(0,255),random.randint(0,255)])
		stars.append(Body(id=i,r=1,mass=random.uniform(startBodyMass[0],startBodyMass[1]),pos=[random.uniform(100,WIDTH),random.uniform(100,HEIGHT)],vel=[random.uniform(-1*STARTBODYSPEED,STARTBODYSPEED),random.uniform(-1*STARTBODYSPEED,STARTBODYSPEED)],col=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]))
    
	stars.append(Body(id=STARTBODYCOUNT-1,r=1,mass=500000,pos=[500,500],vel=[0,0],col=[255,255,255]))
	

def draw1():
    for i in range(0,len(stars)):
        closed = False
        pygame.draw.circle(SCREEN,stars[i].col,[int(stars[i].pos[0]),int(stars[i].pos[1])],int(stars[i].r),int(stars[i].r))
        #stars[i].show()
        stars[i].update()
        attract(stars[i])
        #pygame.draw.aalines(screen,stars[i].col,closed,stars[i].path,1)
        #pygame.draw.aalines(SCREEN,stars[i].col,closed,stars[i].path,1)
        #stars[i].showPath()
        for j in range(0,len(stars[i].path)-1):
        	pygame.draw.line(SCREEN,stars[i].col,stars[i].path[j],stars[i].path[j+1],width=1)
        
        
def main():

	max1 = Body()
	max1.calr()
	max1.r = 1
	print(max1.calr())
	print(max1.r)
	setup()
	print(stars[49].id)
	print(stars[49].mass)
	print()
	while True:
		clock.tick(framerate)
		SCREEN.fill((0, 0, 0))
		#max1.show()
		draw1()
		#print(max1.path)
		
		#pygame.draw.circle(SCREEN,max1.col,max1.pos,max1.r,max1.r)
		pygame.display.flip()
		#max1.show()
	#print(math.pow(2.0/PI*(3.0/4.0),1.0/3.0))
	
main()