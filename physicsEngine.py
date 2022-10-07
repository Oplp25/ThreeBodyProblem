import math,vector,pygame
from turtle import width# need to switch to pygame
class body(object):
    def __init__(self,pos,direction,mass,speed,acceleration,radius):
        self.direction=-direction
        self.pos=pos
        self.mass=mass
        self.speed=speed
        self.acceleration=acceleration
        self.radius=radius
    
    def update(self):
       pass

class body2d(body):
    def __init__(self,pos,direction,mass,speed,acceleration,radius,num):
        super().__init__(pos,direction,mass,speed,acceleration,radius)
        self.num=num
    def update(self,win,WIDTH,HEIGHT):
        print(str(self.num),'Before: pos',self.pos,'Pygame Modified Pos',str(self.pos+vector.vector(WIDTH/2,HEIGHT/2)))#,'mass ',str(self.mass),'speed ',str(self.speed),'acceleration ',str(self.acceleration),'radius ',str(self.radius))
        self.pos=vector.polarVect2d(self.speed,self.direction,self.pos.x,self.pos.y).convert()# creates a polar cordinate with a pole of your current position, going to the destination, with an r=your speed, so you travel speed units in the correct direction
        print(self.direction)
        self.draw(win,WIDTH,HEIGHT)
    def draw(self,win,WIDTH,HEIGHT):
        pygame.draw.circle(win,(255,0,0),(self.pos.x+WIDTH/2,self.pos.y+HEIGHT/2),self.radius)