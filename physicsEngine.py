import math,vector,pygame
GRAVITATIONALCONSTANT=0.00000000006743#6.674*10^-11
class body(object):
    def __init__(self,pos,direction,mass,speed,acceleration,radius):
        self.direction=direction
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
        self.velocity=vector.polarVect2d(self.speed,self.direction,self.pos.x,self.pos.y)
        self.num=num
    def update(self,win,WIDTH,HEIGHT,bodyList):
        self.velocity=vector.polarVect2d(self.velocity.r,self.velocity.theta,self.pos.x,self.pos.y)
        newAccel=vector.polarVect2d(0,0,self.pos.x,self.pos.y)
        for i in bodyList:#for every other body in the simulation
            if i!=self:#not this body, although this line is unnecessary as the r value would be 0
                if self.pos.x==i.pos.x and self.pos.y==i.pos.y:#if they are on top of each other
                    continue
                else:

                    distance=math.sqrt((self.pos.x-i.pos.x)**2+(self.pos.y-i.pos.y)**2)#Use Pythagoras' thereom to find the scalar distance between the centers of the two bodies
                    distance=distance*(10**9)#convert to m
                    print('distance',str(distance)[0:3],str(distance)[3:6],str(distance)[6:9],str(distance)[9:],'m')
                    accelerationScalar=((GRAVITATIONALCONSTANT*i.mass)/(distance**2))#using Newton's second law of motion, F=ma, and his law of universal gravitation, F=(Gm1m2)/(d^2), rearrange to get a=(Gm2)/(d^2)
                    accelerationScalar=accelerationScalar/1000#convert to km/s^2
                    print('Acceleration towards body 1',accelerationScalar)

                    #angle
                    if self.pos.x>i.pos.x and self.pos.y<i.pos.y:
                        angleBetween=math.atan((i.pos.y-self.pos.y)/(self.pos.x-i.pos.x))#finds the angle between the two bodies in radians. Order of subtraction is so that the distances are both positive
                        angleBetween=180-math.degrees(angleBetween)

                    elif self.pos.x<i.pos.x and self.pos.y<i.pos.y:
                        angleBetween=math.atan((i.pos.y-self.pos.y)/(i.pos.x-self.pos.x))#finds the angle between the two bodies in radians. Order of subtraction is so that the distances are both positive
                        angleBetween=math.degrees(angleBetween)

                    elif self.pos.x<i.pos.x and i.pos.y<self.pos.y:
                        angleBetween=math.atan((self.pos.y-i.pos.y)/(i.pos.x-self.pos.x))#finds the angle between the two bodies in radians. Order of subtraction is so that the distances are both positive
                        angleBetween=-math.degrees(angleBetween)

                    elif i.pos.x<self.pos.x and i.pos.y<self.pos.y:
                        angleBetween=math.atan((self.pos.y-i.pos.y)/(self.pos.x-i.pos.x))#finds the angle between the two bodies in radians. Order of subtraction is so that the distances are both positive
                        angleBetween=-(180-math.degrees(angleBetween))
                    
                    #if one of the values is equal

                    elif self.pos.x==i.pos.x:
                        if self.pos.y<i.pos.y:
                            angleBetween==90
                        else:
                            angleBetween=-90
                    elif self.pos.y==i.pos.y:
                        if self.pos.x<i.pos.x:
                            angleBetween=180
                        else:
                            angleBetween=0
                    newAccel=newAccel+vector.polarVect2d(accelerationScalar,angleBetween,self.pos.x,self.pos.y)
        print('Acceleration Before:',self.acceleration)
        self.acceleration=newAccel
        print('Acceleration After',self.acceleration)
        print('Velocity', self.velocity)
        self.velocity+=self.acceleration
        print('New velocity: ',self.velocity,'Position Before',self.pos)
        self.velocity.r=(self.velocity.r/(10**6))*86400#convert velocity to gigameters per day
        self.pos=self.velocity.convertToPos()#pos is in gigameters
        self.velocity.r=self.velocity.r*(10**6)/86400#convert back to km/s
        print('Position after', self.pos)
        #print('Accel angle: ',self.acceleration.theta,'     Velocity angle: ',self.velocity.theta)
        self.draw(win,WIDTH,HEIGHT)
    def draw(self,win,WIDTH,HEIGHT):
        if self.num==1:
            pygame.draw.circle(win,(255,0,0),(self.pos.x+WIDTH/2,HEIGHT/2-self.pos.y),self.radius/1000)
        else:
            pygame.draw.circle(win,(0,0,255),(self.pos.x+WIDTH/2,HEIGHT/2-self.pos.y),self.radius/1000)