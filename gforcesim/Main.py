#!/usr/bin/python3
# coding: utf-8
import pygame
import math
import random
import sys
from Body import *
startBodyCount = 100
startBodySpeed =2.0
black = 0, 0, 0
white = 255, 255, 255
stars = []
#stars[startBodyCount] = []

def sign(a):
   return (a > 0) - (a < 0)

k = 1e7            # 距离缩放参数
m = 5.9742e24      # 地球质量
M = 1898.7e27      # 木星质量
G = 0.5    # 万有引力常量
t = 1e5            # 时间缩放参数
max1 = Body()
pos_x= 100           # 地球坐标
pos_y= 400
earth = pos_x, pos_y
vel_x= 80          # 地球速度
vel_y= 60
jupiter = 700, 300 # 木星坐标
v_j = 3            # 木星速度

width=2400

height=1800
e1 = Body(pos=[100,400])
j1 = Body(pos=[700,300])
#print(e1.mass)
e1.pri
pygame.init()  # 初始化
screen = pygame.display.set_mode((width,height))  # 创建窗口
font = pygame.font.Font('./zhaozi.ttf', 30)  # 显示中文需要字体，否则可略过
text = font.render("木星引力弹弓 - Crossin的编程教室", 1, white)
pygame.display.set_caption("引力弹弓模拟")
startBodyMass = [500,1000]
e = pygame.image.load("earth.png").convert_alpha()  # 地球图片
j = pygame.image.load("jupiter.png").convert_alpha()  # 木星图片
#path1=[[100,200],[300,300],[800,900]]
clock = pygame.time.Clock()
frameRate = 60

def setup():
    width=2400
    height=1800
    for i in range(0,startBodyCount-1):
        #stars[i] = Body(id=i,r=1,mass=random.uniform(startBodyMass[0],startBodyMass[1]),pos=[random.uniform(100,1500),random.uniform(100,800)],vel=[random.uniform(0,startBodySpeed),random.uniform(0,startBodySpeed)],col=[random.randint(0,255),random.randint(0,255),random.randint(0,255)])
        stars.append(Body(id=i,r=1,mass=random.uniform(startBodyMass[0],startBodyMass[1]),pos=[random.uniform(100,1500),random.uniform(100,800)],vel=[random.uniform(0,startBodySpeed),random.uniform(0,startBodySpeed)],col=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]))
    
    stars.append(Body(id=startBodyCount-1,r=1,mass=5000,pos=[2400/2,1800/2],vel=[0,0],col=[255,255,255]))

def draw1():
    for i in range(len(stars)):
        closed = False
        pygame.draw.circle(screen,stars[i].col,[int(stars[i].pos[0]),int(stars[i].pos[1])],int(stars[i].r),int(stars[i].r))
        stars[i].update()
        stars[i].attract()
        pygame.draw.aalines(screen,stars[i].col,closed,stars[i].path,1)
        #stars[i].showPath()


while True:  # 主循环
    for event in pygame.event.get():
        if event.type in (pygame.QUIT, pygame.KEYDOWN):
            sys.exit()  # 按键响应，按键后退出
    
    clock.tick(frameRate)
    screen.fill(black)  # 刷新背景
    j1.pos= j1.pos[0] - v_j, j1.pos[1]  # 木星位移
    #screen.blit(j, j1.pos)  # 画木星
    setup()
    # 地木坐标差
    delta_x = (j1.pos[0] - earth[0]) * k
    delta_y = (j1.pos[1] - earth[1]) * k
    # 地木距离平方
    r2 = delta_x ** 2 + delta_y ** 2
    # 地木间引力，万有引力定律
    F = G * m * M / r2
    # 地木夹角
    theta = math.acos(delta_x / r2 ** 0.5)
    # x、y 轴引力分量
    fx = abs(F * math.cos(theta)) * sign(delta_x)
    fy = abs(F * math.sin(theta)) * sign(delta_y)
    # x、y 轴加速度，牛顿第二定律
    ax = fx / m
    ay = fy / m
    # 速度变化，vt = v0 + at
    vel_x += ax * t
    vel_y += ay * t
    # 位移变化，st = s0 + vt
    pos_x += vel_x * t / k
    pos_y += vel_y * t / k
    earth = int(pos_x), int(pos_y)
    pygame.draw.circle(screen, white, j1.pos, 30, 30)#画圆
    #closed = False
    #pygame.draw.aalines(screen,white,closed,path1,1)
    
    #screen.blit(e, earth)  # 画地球

    draw1()
    v = '地球速度 %.2f km/s' % ((vel_x ** 2 + vel_y ** 2) ** 0.5)  # 速度大小
    speed = font.render(v, 1, white)
    screen.blit(text, (150, 100))
    screen.blit(speed, (200, 50))
    pygame.display.update()  # 刷新

