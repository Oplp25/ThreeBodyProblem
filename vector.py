import math,random
class vector(object):
    def __init__(self,x,y,z=0):
        self.x=x
        self.y=y
        self.z=z
    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+','+str(self.z)+')'
    
    def __add__(self,v2):
        return posVector(self.x+v2.x,self.y+v2.y,self.z+v2.z)
    
    def __sub__(self,v2):
        return posVector(self.x-v2.x,self.y-v2.y,self.z-v2.z)
    
    def convert2d(self):
        pass

class posVector(vector):
    def __init__(self,x,y,z=0):
        super().__init__(x,y,z)
    def convert2d(self):
        if self.x==0 and self.y==0:
            return polarVect2d(0,0,self.poleX)
        elif self.x>0 and self.y>0:
            return polarVect2d(math.sqrt(self.x**2+self.y**2),math.degrees(math.atan(self.y/self.x)))
        elif self.x>0 and self.y<0:
            return polarVect2d(math.sqrt(self.x**2+self.y**2),-math.degrees(math.atan(self.y/self.x)))
        elif self.x<0 and self.y<0:
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

class motVector(vector):
    def __init__(self, x, y, z=0,pX=0,pY=0,pZ=0):
        super().__init__(x, y, z)
        self.poleX=pX
        self.poleY=pY
        self.poleZ=pZ
    def __add__(self,v2):
        return motVector(self.x+v2.x,self.y+v2.y,self.z+v2.z,self.poleX,self.poleY,self.poleZ)

    def convert2d(self):
        if self.x==0 and self.y==0:
            return polarVect2d(0,0,self.poleX,self.poleY)
        elif self.x>0 and self.y>0:
            return polarVect2d(math.sqrt(self.x**2+self.y**2),math.degrees(math.atan(self.y/self.x)),self.poleX,self.poleY)
        elif self.x>0 and self.y<0:
            return polarVect2d(math.sqrt(self.x**2+self.y**2),-abs(math.degrees(math.atan(self.y/self.x))),self.poleX,self.poleY)
        elif self.x<0 and self.y<0:
            return polarVect2d(math.sqrt(self.x**2+self.y**2),-abs(180-math.degrees(math.atan(self.y/self.x))),self.poleX,self.poleY)
        elif self.x<0 and self.y>0:
            return polarVect2d(math.sqrt(self.x**2+self.y**2),180-math.degrees(math.atan(self.y/self.x)),self.poleX,self.poleY)
        elif self.x==0:
            if self.y<0:
                return polarVect2d(-self.y,-90,self.poleX,self.poleY)
            else:
                return polarVect2d(self.y,90,self.poleX,self.poleY)
        elif self.y==0:
            if self.x<0:
                return polarVect2d(-self.x,180,self.poleX,self.poleY)
            else:
                return polarVect2d(self.x,0,self.poleX,self.poleY)
        else:
            raise TypeError(self)
class polarVect2d(object):
    def __init__(self,r,theta,x=0,y=0):
        self.poleX=x
        self.poleY=y
        self.theta=theta
        self.r=r
    def __add__(self,p2):
        tempSelf=self.convertToMot()
        tempP2=p2.convertToMot()
        addition=tempSelf+tempP2
        return addition.convert2d()
    def __str__(self):
        return '('+str(self.r)+','+str(self.theta)+')'
    def convertToPos(self):
        newX=self.r*math.cos(math.radians(self.theta))#wrong
        newY=self.r*math.sin(math.radians(self.theta))#wrong
        return posVector(newX+self.poleX,newY+self.poleY)
    def convertToMot(self):
        newX=self.r*math.cos(math.radians(self.theta))#wrong
        newY=self.r*math.sin(math.radians(self.theta))#wrong
        return motVector(newX,newY,0,self.poleX,self.poleY,0)
if __name__=='__main__':
    vect=polarVect2d(0.13348,-135.0,50,50)
    newVect=polarVect2d(1,0,50,50)
    print(vect.convertToMot())
    print(vect.convertToPos())
    print(newVect.convertToMot())
    print(newVect.convertToPos())
    x=vect+newVect
    print(x,x.poleX,x.poleY)
