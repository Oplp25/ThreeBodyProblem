import math
from vector import vector
class body(object):
    def __init__(self,pos,direction,mass,speed,acceleration):
        self.pos=pos
        self.direction=direction
        self.mass=mass
        self.speed=speed
        self.acceleration=acceleration
    
    def update(self):
        self.pos=self.pos+(self.direction*self.speed)