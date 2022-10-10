import math,random
class vector(object):
    def __init__(self,x,y,z=0):
        self.x=x
        self.y=y
        self.z=z
    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+','+str(self.z)+')'
    
    def __add__(self,v2):
        return vector(self.x+v2.x,self.y+v2.y,self.z+v2.z)
    
    def __sub__(self,v2):
        return vector(self.x-v2.x,self.y-v2.y,self.z-v2.z)
    
    def convert2d(self):
        if not self.x==0:
            return polarVect2d(math.sqrt(self.x**2+self.y**2),math.degrees(math.atan(self.y/self.x)))
        else:
            return polarVect2d(math.sqrt(self.x**2+self.y**2),math.degrees(math.atan(0)))
class polarVect2d(object):
    def __init__(self,r,theta,x=0,y=0):
        self.poleX=x
        self.poleY=y
        self.theta=theta
        self.r=r
    def __add__(self,p2):
        tempSelf=self.convert()
        tempP2=p2.convert()
        addition=tempSelf+tempP2#-vector(self.poleX,self.poleY)-vector(p2.poleX,p2.poleY)
        return addition.convert2d()
    def __sub__(self,p2):
        tempSelf=self.convert()
        tempP2=p2.convert()
        addition=tempSelf-tempP2-vector(self.poleX,self.poleY)-vector(p2.poleX,p2.poleY)
    def __str__(self):
        return '('+str(self.r)+','+str(self.theta)+')'
    def convert(self):
        return vector((self.r*math.cos(math.radians(self.theta)))+self.poleX,(self.r*math.sin(math.radians(self.theta)))+self.poleY)

vect=polarVect2d(2,60)
v2=polarVect2d(4,30)

print((vect-v2))