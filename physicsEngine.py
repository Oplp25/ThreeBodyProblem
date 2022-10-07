import math,vector,pygame
from turtle import width# need to switch to pygame
class body(object):
    def __init__(self,pos,direction,mass,speed,acceleration,radius):
        self.direction=direction
        if self.direction==vector.vector(0,0,0):
            self.direction=self.pos
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
        print(str(self.num),'Before: pos',self.pos,'Pygame Modified Pos',str(self.pos+vector.vector(WIDTH/2,HEIGHT/2)),'dir',str(self.direction),' Pygame Modified Dir',str(self.direction+vector.vector(WIDTH/2,HEIGHT/2)))#,'mass ',str(self.mass),'speed ',str(self.speed),'acceleration ',str(self.acceleration),'radius ',str(self.radius))
        ratio=(self.direction.y-self.pos.y)/(self.direction.x-self.pos.x) # finds the ratio between the y and the x
        theta=math.degrees(math.atan(ratio)) # finds the arctan for the polar coordinates conversion. math.atan returns a value in radians, so need to convert to degrees
        radius=math.sqrt((self.direction.x-self.pos.x)**2+(self.direction.y-self.pos.y)**2)# Pythagoras to find the r for the polar coordinatees conversion
        #self.directionVector=vector.polarVect2d(radius,theta,self.pos.x,self.pos.y)# creates a polar cordinate with a pole of your current position, going to the destination
        self.pos=vector.polarVect2d(self.speed,theta,self.pos.x,self.pos.y).convert()# creates a polar cordinate with a pole of your current position, going to the destination, with an r=your speed, so you travel speed units in the correct direction
        print(theta)
        self.draw(win,WIDTH,HEIGHT)
    def draw(self,win,WIDTH,HEIGHT):
        pygame.draw.circle(win,(255,0,0),(self.pos.x+WIDTH/2,self.pos.y+HEIGHT/2),self.radius)