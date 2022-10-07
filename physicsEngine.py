import math,vector,pygame
from turtle import width# need to switch to pygame
GRAVITATIONALCONSTANT=0.0000000006674
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
    def update(self,win,WIDTH,HEIGHT,bodyList):
        self.direction+=1
        if self.direction>=360:
            self.direction-=360
        print(str(self.num),'pos',self.pos,'Acceleration',str(self.acceleration),'speed',str(self.speed))#'Pygame Modified Pos',str(self.pos+vector.vector(WIDTH/2,HEIGHT/2))#,'mass ',str(self.mass),'speed ',str(self.speed),'acceleration ',str(self.acceleration),'radius ',str(self.radius))
        for i in bodyList:
            if i!=self and self.num!=2:
                distance=math.sqrt((self.pos.x-i.pos.x)**2+(self.pos.y-i.pos.y)**2)#find the distance between the centers of the two bodies
                self.acceleration=(GRAVITATIONALCONSTANT*i.mass)/(distance**2)#use newtoms 2nd law of motion, F=ma, and his law of universal gravitation, to calculate acceleration towards the other mass
        self.speed+=self.acceleration
        self.pos=vector.polarVect2d(self.speed,self.direction,self.pos.x,self.pos.y).convert()# creates a polar cordinate with a pole of your current position, going to the destination, with an r=your speed, so you travel speed units in the correct direction
        print(self.direction)
        self.draw(win,WIDTH,HEIGHT)
    def draw(self,win,WIDTH,HEIGHT):
        pygame.draw.circle(win,(255,0,0),(self.pos.x+WIDTH/2,self.pos.y+HEIGHT/2),self.radius)