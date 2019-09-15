#！/usr/bin/python3

#id0=0
#r0=1
#mass0=1
#pos0=[500,500]
#vel0=[100,100]
#col=[255,255,255]
class Body():
#class Body(id0=0,r0=1,mass0=1,pos0=[500,500],vel0=[100,100],col=[255,255,255]):
    
    def __init__(self,id=0,r=1,mass=1,pos=[500,500],vel=[100,100],col=[255,255,255]):
        self.id=id
        self.mass=mass
        self.r=r
        self.pos=pos
        self.vel=vel
        self.col=col



