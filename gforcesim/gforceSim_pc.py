#pylint:disable=C0325
#!/usr/bin/python3
# coding: utf-8
import math
#import pygame_sdl2					#此行为手机上pydorid3软件上运行所需引入的模块,pc上注释掉既可
#pygame_sdl2.import_as_pygame()			#此行为手机上pydorid3软件上运行所需引入的模块,pc上注释掉既可
import sys
import pygame
from pygame.locals import *
import random


G = 1000   #引力常数
WIDTH  = 2500
HEIGHT = 1600
PI = math.pi
STARTBODYCOUNT = 100    #初始化星星数量
STARTBODYSPEED = 100		#初始化星星速度范围
BLACK = 0,0,0
WHITE = 255,255,255
stars = list()
framerate = 60
force = []
direct = []
forcePower = 0
MAXPATH = 300				#轨迹长度参数
max_pos = [0,0]
max_mass = 0
x_low =0
x_high = 0
y_low = 0
y_high = 0
scale = 1				#画面缩放系数


pygame.init()
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
myfont = pygame.font.SysFont("DejaVuSans", 20)		#设置字体

clock = pygame.time.Clock()



class Body():
	def __init__(self,id=-1,r=1,mass=3,pos=[500,500],vel=[100,100],col=[255,255,255]):
		self.id = id
		self.mass = mass
		self.r = math.pow(mass/PI*(3.0/4.0),1.0/3.0)
		
		self.pos = pos
		self.vel = vel
		self.col= col
		self.path = []
		
	
	def calr(self):
		
		self.r = math.pow(self.mass/PI*(3.0/4.0),1.0/3.0)
		return self.r
		
	def show(self):
		global SCREEN
		global MAXPATH
		global max_pos
		global scale
		
		
		
		pygame.draw.circle(SCREEN,self.col,[int(scale*(self.pos[0]-max_pos[0])),int(scale*(self.pos[1]-max_pos[1]))],int(scale*self.r),int(scale*self.r))
		
		
	
		
		
	def update(self):
		self.pos[0] = self.pos[0] + self.vel[0]/framerate
		self.pos[1] = self.pos[1] + self.vel[1]/framerate
		self.path.append([self.pos[0],self.pos[1]])
		
		#if((len(self.path) > MAXPATH) and (len(stars) > 10)):
			#del self.path[0]
		if(len(self.path) > ((20/len(stars))*MAXPATH)):#确定轨迹长度
			del self.path[0]		#删除多余多余轨迹0m
		
		 #下面反弹效果这部分给注释了.留着或者能挽救下跑出屏幕的可怜星星
		if(self.pos[0] <= -WIDTH*1.1) or (self.pos[0] >= WIDTH*2):
			self.vel[0] *= -1
		if(self.pos[1] <= -HEIGHT*1.1) or (self.pos[1] >= HEIGHT*2):
			self.vel[1] *= -1
			
	def showPath(self):
		closed = False
		path_int = []
		global SCREEN
		for j in range(0,len(self.path)):
			path_int.append([int(scale*(self.path[j][0]-max_pos[0])),int(scale*(self.path[j][1]-max_pos[1]))])
		if len(path_int)>1:
			pygame.draw.lines(SCREEN,self.col,0,path_int,1)
		


def attract(body):
	global direct
	global scale
	global max_pos
	global forcePower
	force_all = [0,0]
	
	for i in range(0,len(stars)):
		if i >= len(stars):
			break
		
		if stars[i].id == body.id:
			continue
		
		#pygame.draw.line(SCREEN,body.col,[scale*(body.pos[0]-max_pos[0]),scale*(body.pos[1]-max_pos[1])],[scale*(stars[i].pos[0]-max_pos[0]),scale*(stars[i].pos[1]-max_pos[1])],1)  #绘制星球间直线  可解除注释看效果
		direct = [body.pos[0] - stars[i].pos[0] ,body.pos[1] - stars[i].pos[1]]
		if(math.sqrt(direct[0]**2+direct[1]**2) <= (body.r+stars[i].r)):
			if(body.mass>=stars[i].mass):
				body.vel[0] =  (body.vel[0] * body.mass + stars[i].vel[0] * stars[i].mass)/(body.mass + stars[i].mass)
				body.vel[1] =  (body.vel[1] * body.mass + stars[i].vel[1] * stars[i].mass)/(body.mass + stars[i].mass)
				body.mass = body.mass + stars[i].mass
				body.r = body.calr()
				del stars[i]
			continue

		forcePower = G * (body.mass + stars[i].mass)/(direct[0] ** 2 + direct[1] ** 2)
		force = [forcePower * direct[0]/math.sqrt(direct[0]**2+direct[1]**2),forcePower * direct[1]/math.sqrt(direct[0]**2+direct[1]**2)]
		
		force_all[0] = force_all[0] + force[0]
		force_all[1] = force_all[1] + force[1]
	body.vel = [(body.vel[0]-force_all[0]/body.mass*(10/framerate)),(body.vel[1]-force_all[1]/body.mass*(10/framerate))]




def setup():
	startBodyMass = [500,5000]
	for i in range(0,STARTBODYCOUNT-1):
    
		stars.append(Body(i,r=1,mass=random.uniform(startBodyMass[0],startBodyMass[1]),pos=[random.uniform(0,WIDTH),random.uniform(0,HEIGHT)],vel=[random.uniform(-1*STARTBODYSPEED,STARTBODYSPEED),random.uniform(-1*STARTBODYSPEED,STARTBODYSPEED)],col=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]))
    
	stars.append(Body(id=STARTBODYCOUNT-1,r=1,mass=250000,pos=[WIDTH*0.5,HEIGHT*0.5],vel=[0,0],col=[255,0,0]))
	


	
			
			
def main():
	global max_mass
	global max_pos
	global x_low
	global x_high
	global y_low
	global y_high
	global scale
	global WIDTH
	global HEIGHT
	max1 = Body()
	max1.calr()
	max1.r = 1
	print(max1.calr())
	print(max1.r)
	setup()
	print(stars[0].id)
	print(stars[0].path)
	x = 1
	
	while True:
		for event in pygame.event.get():
			if event.type in (pygame.QUIT, pygame.KEYDOWN):
				sys.exit()  # 按键响应，按键后退出
		clock.tick(framerate)
		SCREEN.fill((0, 0, 0))
		
		x_low = 0
		x_high = 0
		y_low = 0
		y_high = 0
		scale = 1
		
		for i in range(0,len(stars)):
			
			if i >= len(stars):
				break
			
			if stars[i].pos[0] <= x_low:
				x_low = stars[i].pos[0]
			if stars[i].pos[0] >= x_high:
				x_high = stars[i].pos[0]
			if stars[i].pos[1] <= y_low:
				y_low = stars[i].pos[1]
			if stars[i].pos[1] >= y_high:
				y_high = stars[i].pos[1]
			x_scale = (1*WIDTH/(x_high - x_low))
			y_scale = (1*HEIGHT/(y_high - y_low))
			if ((x_scale <= 1)or (y_scale <= 1)):
				if x_scale >= y_scale:
					scale = y_scale
				else:scale = x_scale
			else:scale = 1
			
		
		
		for i in range(0,len(stars)):
			
			if i >= len(stars):
				break
			
			
			
			if stars[i].mass >= max_mass:	#此段代码为了将质量最大的星星为中心并设置到画面指定坐标
				max_mass = stars[i].mass
				#以下两行代码将最大星星显示到像素坐标500,500
				max_pos[0] = stars[i].pos[0] - 0.5*WIDTH/scale
				max_pos[1] = stars[i].pos[1] - 0.5*HEIGHT/scale
				#max_pos = [0,0]
				#max_pos[0] = max_pos[0]*scale
				#max_pos[1] = max_pos[1]*scale
			#stars[i].pos[0] = stars[i].pos[0] - max_pos[0]
			#stars[i].pos[1] = stars[i].pos[1] - max_pos[1]
			
			stars[i].update()
			stars[i].show()
			stars[i].showPath()
			attract(stars[i])
			
			if i >= len(stars):
				break
			
			
			
		x = x + 1
	
		#for i in range(0,len(stars)):
			#SCREEN.blit(myfont.render(str(stars[i].id),1,stars[i].col),(100,100+50*i))
			#SCREEN.blit(myfont.render('v      '+str(stars[i].vel),1,stars[i].col),(150,100+50*i))
			#SCREEN.blit(myfont.render('pos  '+str([stars[i].pos[0],stars[i].pos[1]]),1,stars[i].col),(150,125+50*i))
			#SCREEN.blit(myfont.render('path'+str(len(stars[0].path)),1,[255,255,255]),(100,100+50*len(stars)+25))
			#SCREEN.blit(myfont.render('scale='+str(scale),1,[255,255,255]),(100,150+50*len(stars)))
			#SCREEN.blit(myfont.render(str(x),1,[255,255,255]),(100,100+50*len(stars)))
		SCREEN.blit(myfont.render('scale='+str(scale),1,[255,255,255]),(100,150))
		SCREEN.blit(myfont.render(str(x),1,[255,255,255]),(100,175))
		SCREEN.blit(myfont.render('path'+str(len(stars[0].path)),1,[255,255,255]),(100,200))
		SCREEN.blit(myfont.render('stars ='+str(len(stars)),1,[255,255,255]),(100,225))
		pygame.display.flip()
		
	
main()
