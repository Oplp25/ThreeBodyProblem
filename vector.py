import math
class vector(object):
    def __init__(self,x,y,z=0):
        self.x=x
        self.y=y
        self.z=z
        self.pol=self.convert2d()
    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+','+str(self.z)+')'
    
    def __add__(self,v2):
        return vector(self.x+v2.y,self.y+v2.y,self.z+v2.z)
    
    def convert2d(self):
        return polarVect(math.sqrt(self.x**2+self.y**2),math.degrees(math.atan(self.y/self.x)))

class polarVect(object):
    def __init__(self,r,theta):
        self.theta=theta
        self.r=r
    def __str__(self):
        return '('+str(self.r)+','+str(self.theta)+')'
    def convert2d(self):
        return vector(self.r*math.cos(math.radians(self.theta)),self.r*math.sin(math.radians(self.theta)))
