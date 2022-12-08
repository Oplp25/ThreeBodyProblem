import startWindow,physicsEngine, panda3d, time, math,os
from vector import posVector

#distance 1 pixel = 1,000,000 km = 1 GM
#time 1 tick = 1 day
#speed measured in km/s
#mass measured in kg
#Acceleration measured in km/s^2
#radii measured in km, but drawn to a scale of 1:1000, otherwise they would not be seen. Sun drawn to 1:100000
earthX=-150*math.sqrt(2)/2
earthY=-150*math.sqrt(2)/2
earthAngle=135
mechanicsType,numbBodies,dimensions,  x1,y1,z1,  theta1,mass1,speed1,accel1,radius1,x2,y2,z2,theta2,mass2,speed2,accel2,radius2,  x3,y3,z3,  theta3,  mass3,speed3,accel3,radius3  ='N',2,2, 0,0,0, 0, 2*(10**30),0,0, 6957,    earthX, earthY,0, earthAngle, 6*(10**24),29.8,0, 6371 ,0,0,0,0,0,0,0,0 #sun,earth, nothing #startWindow.runStartWindow()
bodyList=[]
if dimensions==3:
    bodyList.append(physicsEngine.body3d(posVector(x1,y1,z1),theta1,mass1,speed1,accel1,radius1))
    if numbBodies>=2:
        bodyList.append(physicsEngine.body3d(posVector(x2,y2,z2),theta2,mass2,speed2,accel2,radius2))
    if numbBodies==3:
        bodyList.append(physicsEngine.body3d(posVector(x3,y3,z3),theta3,mass3,speed3,accel3,radius3))
else:
    import pygame
    pygame.init()
    win=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    WIDTH=pygame.display.Info().current_w
    HEIGHT=pygame.display.Info().current_h
    clock=pygame.time.Clock()
    bodyList.append(physicsEngine.body2d(posVector(x1,y1),theta1,mass1,speed1,accel1,radius1,1))
    if numbBodies>=2:
        bodyList.append(physicsEngine.body2d(posVector(x2,y2),theta2,mass2,speed2,accel2,radius2,2))
    if numbBodies==3:
        bodyList.append(physicsEngine.body2d(posVector(x3,y3),theta3,mass3,speed3,accel3,radius3))
run=True
os.system('cls')
bodyList[0].draw(win,WIDTH,HEIGHT)
bodyList[1].draw(win,WIDTH,HEIGHT)
pygame.display.update()
step=1
#for i in range(1):
while run:
    if dimensions==2:
        #time.sleep(0.5)
        print('\nStep ',step)
        print('\n')
        clock.tick(60)
        #win.fill((0,0,0))
        for i in bodyList:
            if i.num==2:
                i.update(win,WIDTH,HEIGHT,bodyList)
        bodyList[0].draw(win,WIDTH,HEIGHT)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT or event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                pygame.quit()
                exit()
        step+=1
    else:
        for i in bodyList:
            i.update()