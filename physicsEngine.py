import math,vector,turtle
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
    def __init__(self,pos,direction,mass,speed,acceleration,radius):
        super().__init__(pos,direction,mass,speed,acceleration,radius)
        self.turtle=turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.hideturtle()
    def update(self):
        ratio=self.direction.y-self.pos.y/self.direction.x-self.pos.x
        theta=math.atan(ratio)
        radius=math.sqrt((self.direction.x-self.pos.x)**2+(self.direction.y-self.pos.y)**2)
        self.directionVector=vector.polarVect2d(radius,theta,self.pos.x,self.pos.y)
        self.pos=vector.polarVect2d(self.speed,self.directionVector.theta,self.pos.x,self.pos.y).convert()
        print(self.pos)
        self.draw()
    def draw(self):
        self.turtle.clear()
        self.turtle.penup()
        self.turtle.goto(self.pos.x,self.pos.y)
        self.turtle.pendown()
        self.turtle.begin_fill()
        self.turtle.circle(self.radius)
        self.turtle.end_fill()