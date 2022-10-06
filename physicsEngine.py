import math,vector,turtle
class body(object):
    def __init__(self,pos,direction,mass,speed,acceleration,radius):
        self.pos=pos
        self.direction=direction
        self.mass=mass
        self.speed=speed
        self.acceleration=acceleration
        self.radius=radius
    
    def update(self):
       pass

class body2d(body):
    def __init__(self,pos,direction,mass,speed,acceleration):
        super().__init__()
    def update(self):
        ratio=self.direction.y-self.pos.y/self.direction.x-self.pos.x
        theta=math.atan(ratio)
        radius=math.sqrt((self.direction.x-self.pos.x)**2,(self.direction.y-self.pos.y)**2)
        self.directionVector=vector.polarVect(radius,theta)
        self.turtle=turtle.Turtle()
        self.turtle.hideturtle()
    def draw(self):
        turtle.goto(self.pos.x,self.pos.y)
        turtle.circle(self.radius)
