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
        if not self.x==0:
            return polarVect2d(math.sqrt(self.x**2+self.y**2),math.degrees(math.atan(self.y/self.x)))#doesn't work
        else:
            return polarVect2d(math.sqrt(self.x**2+self.y**2),math.degrees(math.atan(0)))#doesn't work
class polarVect2d(object):
    def __init__(self,r,theta,x=0,y=0):
        self.poleX=x
        self.poleY=y
        self.theta=theta
        self.r=r
    def __str__(self):
        return '('+str(self.r)+','+str(self.theta)+')'
    def convert(self):
        return vector(self.r*math.cos(math.radians(self.theta))+self.poleX,self.r*math.sin(math.radians(self.theta))+self.poleY)#doesn't work
print(vector(3,4).convert2d())
print(polarVect2d(5,67.5).convert())
