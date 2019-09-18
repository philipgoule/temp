#！/usr/bin/python3
import math
import pygame
#id0=0
#r0=1
#mass0=1
#pos0=[500,500]
#vel0=[100,100]
#col=[255,255,255]
PI = math.pi


class Body():
#class Body(id0=0,r0=1,mass0=1,pos0=[500,500],vel0=[100,100],col=[255,255,255]):
    
    def __init__(self,id=0,r=1,mass=1,pos=[500,500],vel=[100,100],col=[255,255,255]):
        self.id=id
        self.mass=mass
        self.r=self.calR(self.mass)
        self.pos=pos
        self.vel=vel
        self.col=col
        
      
        self.path = []
        self.MAXPATH = 300
       
    #print(cls.mass)
    def pri(self):
        print('123')
   
    def calR(self,mass):
        max1 = self
        if not max1 :
            
            max1 = self
        if max1.mass <= self.mass:
            max1 = self
        return math.pow(self.mass/PI*(3.0/4.0),1.0/3.0)
   
    def show(self):
        global screen
        #screen = pygame.display.set_mode((2400, 1800))
        #pygame.draw.circle(screen,self.col,self.pos,self.r,self.r)

    def update(self):
        global stars
        width=2400
        height=1800
        self.pos[0] = self.pos[0] + self.vel[0]
        self.pos[1] = self.pos[1] + self.vel[1]
        self.path.append(self.pos)
        if(len(self.path) > self.MAXPATH and len(star) > 10):
            del self.path[0]
        if(len(self.path) > (self.MAXPATH*3)):
            del self.path[0]
        #下面反弹效果这部分up主给注释了.留着或者能挽救下跑出屏幕的可怜星星
        if(self.pos[0] <= -width*2) or (self.pos[0] >= width*2):
            self.vel[0] *= -1
        if(self.pos[1] <= -height*2) or (self.pos[1] >= height*2):
            self.vel[1] *= -1

    def showPath(self):
        closed = False
        global screen
        #pygame.draw.aalines(screen,self.col,closed,self.path,1)

    def attract(self):
        global stars
        dir = []
        force = []
        forcePower = 0
        global G
        global frameRate
        for i in range(len(stars)):
            other = stars[i]
            if(other == self):
                continue
            dir = [self.pos[0] - other.pos[0] ,self.pos[1] - other.pos[1]]
            if(math.sqrt(dir[0]**2+dir[1]**2) <= (self.r+other.r)):
                self.vel[0] =  (self.vel[0] * self.mass + other.vel[0] * other.mass)/(self.mass + other.mass)
                self.vel[1] =  (self.vel[1] * self.mass + other.vel[1] * other.mass)/(self.mass + other.mass)
                self.mass = self.mass + other.mass
                self.r = self.calR(self.mass)
                del stars[i]
            continue

        forcePower = G * (self.mass + other.mass)/(dir[0] ** 2 + dir[1] ** 2)
        force = [forcePower * dir[0]/math.sqrt(dir[0]**2+dir[1]**2),forcePower * dir[1]/math.sqrt(dir[0]**2+dir[1]**2)]
        other.vel = [(other.vel[0]+force[0])/other.mass*(1/frameRate),(other.vel[1]+force[1])/other.mass*(1/frameRate)]


