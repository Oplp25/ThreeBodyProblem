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
        if self.x==0 and self.y==0:
            return polarVect2d(0,0)
        elif self.x>0 and self.y>0:
            return polarVect2d(math.sqrt(self.x**2+self.y**2),math.degrees(math.atan(self.y/self.x)))#problem is here, math.atan finds the closest value of atan, not the one we want
        elif self.x>0 and self.y<0:
            return polarVect2d(math.sqrt(self.x**2+self.y**2),-math.degrees(math.atan(self.y/self.x)))
        elif self.x<0 and self.y<0:
            print('HELLO',self,polarVect2d(math.sqrt(self.x**2+self.y**2),-(180-math.degrees(math.atan(self.y/self.x)))))
            return polarVect2d(math.sqrt(self.x**2+self.y**2),-(180-math.degrees(math.atan(self.y/self.x))))
        elif self.x<0 and self.y>0:
            return polarVect2d(math.sqrt(self.x**2+self.y**2),180-math.degrees(math.atan(self.y/self.x)))
        elif self.x==0:
            if self.y<0:
                return polarVect2d(-self.y,-90)
            else:
                return polarVect2d(self.y,90)
        elif self.y==0:
            if self.x<0:
                return polarVect2d(-self.x,180)
            else:
                return polarVect2d(self.x,0)
        else:
            raise TypeError(self)
class polarVect2d(object):
    def __init__(self,r,theta,x=0,y=0):
        self.poleX=x
        self.poleY=y
        self.theta=theta
        self.r=r
    def __add__(self,p2):
        tempSelf=self.convert()
        tempP2=p2.convert()
        addition=tempSelf+tempP2
        return addition.convert2d()
    def __sub__(self,p2):
        tempSelf=self.convert()
        tempP2=p2.convert()
        addition=tempSelf-tempP2
    def __str__(self):
        return '('+str(self.r)+','+str(self.theta)+')'
    def convert(self):
        return vector((self.r*math.cos(math.radians(self.theta)))+self.poleX,(self.r*math.sin(math.radians(self.theta)))+self.poleY)