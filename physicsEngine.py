import math,vector,turtle# need to switch to pygame
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
        self.turtle=turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.hideturtle()
        self.num=num
    def update(self):
        print(str(self.num),'Before: pos',self.pos,'dir ',str(self.direction))#,'mass ',str(self.mass),'speed ',str(self.speed),'acceleration ',str(self.acceleration),'radius ',str(self.radius))
        ratio=(self.direction.y-self.pos.y)/(self.direction.x-self.pos.x) # finds the ratio between the y and the x
        theta=math.degrees(math.atan(ratio)) # finds the arctan for the polar coordinates conversion. math.atan returns a value in radians, so need to convert to degrees
        radius=math.sqrt((self.direction.x-self.pos.x)**2+(self.direction.y-self.pos.y)**2)# Pythagoras to find the r for the polar coordinatees conversion
        #self.directionVector=vector.polarVect2d(radius,theta,self.pos.x,self.pos.y)# creates a polar cordinate with a pole of your current position, going to the destination
        self.pos=vector.polarVect2d(self.speed,theta,self.pos.x,self.pos.y).convert()# creates a polar cordinate with a pole of your current position, going to the destination, with an r=your speed, so you travel speed units in the correct direction
        print(str(self.num),'After: ',self.pos)
        self.draw()
    def draw(self):
        self.turtle.penup()#switch to pygame
        self.turtle.goto(self.pos.x,self.pos.y)
        self.turtle.pendown()
        self.turtle.begin_fill()
        self.turtle.circle(self.radius)
        self.turtle.end_fill()
        #self.turtle.clear()