import math,vector,pygame
from turtle import width# need to switch to pygame
GRAVITATIONALCONSTANT=0.0000000006674
class body(object):
    def __init__(self,pos,direction,mass,speed,acceleration,radius):
        self.direction=-direction
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
        self.acceleration=vector.polarVect2d(acceleration,self.direction,self.pos.x,self.pos.y)
        print(self.acceleration)
        self.num=num
    def update(self,win,WIDTH,HEIGHT,bodyList):
        if self.acceleration.theta>=360:
            self.acceleration.theta-=360
        if self.acceleration.theta<=360:
            self.acceleration.theta+=360
        #print(str(self.num),'pos',self.pos,'Acceleration',str(self.acceleration),'speed',str(self.speed))#'Pygame Modified Pos',str(self.pos+vector.vector(WIDTH/2,HEIGHT/2))#,'mass ',str(self.mass),'speed ',str(self.speed),'acceleration ',str(self.acceleration),'radius ',str(self.radius))
        aList=[]
        for i in bodyList:
            if i!=self:
                distance=math.sqrt((self.pos.x-i.pos.x)**2+(self.pos.y-i.pos.y)**2)#find the distance between the centers of the two bodies
                accel=((GRAVITATIONALCONSTANT*i.mass)/(distance**2))
                aList.append(vector.polarVect2d(accel,math.degrees(math.atan((i.pos.y-self.pos.y)/(i.pos.x-self.pos.x)))))#use newtoms 2nd law of motion, F=ma, and his law of universal gravitation, to calculate acceleration towards the other mass
        for i in aList:
            '''if i.theta<=360:
                i.theta+=360
            if i.theta>=360:
                i.theta-=360'''
            if i.theta==90 or i.theta==270:
                continue
            elif(270<i.theta or i.theta<90):
                self.acceleration+=vector.polarVect2d(i.r,i.theta-180)
                #print('270<i<90')
            elif 90<i.theta<270:
                self.acceleration-=vector.polarVect2d(i.r,180-i.theta)
                #print('270>i>90')
        if self.num==2:
            print('aList: ', aList[0])
            print('Acceleration: ',self.acceleration)
        '''if self.num==1:
            pygame.draw.line(win,(255,0,0),(self.pos.x+WIDTH/2,self.pos.y+HEIGHT/2),(self.acceleration.convert().x+WIDTH/2,self.acceleration.convert().y+HEIGHT/2))
        else:
            pygame.draw.line(win,(0,0,255),(self.pos.x+WIDTH/2,self.pos.y+HEIGHT/2),(self.acceleration.convert().x+WIDTH/2,self.acceleration.convert().y+HEIGHT/2))'''
        #self.speed+=self.acceleration.r
        self.pos=vector.polarVect2d(self.speed,-self.acceleration.theta,self.pos.x,self.pos.y).convert()# creates a polar cordinate with a pole of your current position, going to the destination, with an r=your speed, so you travel speed units in the correct direction
        self.draw(win,WIDTH,HEIGHT)
    def draw(self,win,WIDTH,HEIGHT):
        if self.num==1:
            pygame.draw.circle(win,(255,0,0),(self.pos.x+WIDTH/2,self.pos.y+HEIGHT/2),self.radius)
        else:
            pygame.draw.circle(win,(0,0,255),(self.pos.x+WIDTH/2,self.pos.y+HEIGHT/2),self.radius)