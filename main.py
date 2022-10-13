import startWindow,physicsEngine, panda3d, time
from vector import vector
speed=0.0001
mechanicsType,numbBodies,dimensions,  x1,y1,z1,  theta1,mass1,speed1,accel1,radius1,x2,y2,z2,theta2,mass2,speed2,accel2,radius2,  x3,y3,z3,  theta3,  mass3,speed3,accel3,radius3  ='N',2,2,   0,0,0,  0,   10,0,0,10,  50,50,0,  0,  1,speed,0,10,  0,0,0,0,0,0,0,0#startWindow.runStartWindow()
bodyList=[]
if dimensions==3:
    bodyList.append(physicsEngine.body3d(vector(x1,y1,z1),theta1,mass1,speed1,accel1,radius1))
    if numbBodies>=2:
        bodyList.append(physicsEngine.body3d(vector(x2,y2,z2),theta2,mass2,speed2,accel2,radius2))
    if numbBodies==3:
        bodyList.append(physicsEngine.body3d(vector(x3,y3,z3),theta3,mass3,speed3,accel3,radius3))
else:
    import pygame
    pygame.init()
    win=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    WIDTH=pygame.display.Info().current_w
    HEIGHT=pygame.display.Info().current_h
    clock=pygame.time.Clock()
    bodyList.append(physicsEngine.body2d(vector(x1,y1),theta1,mass1,speed1,accel1,radius1,1))
    if numbBodies>=2:
        bodyList.append(physicsEngine.body2d(vector(x2,y2),theta2,mass2,speed2,accel2,radius2,2))
    if numbBodies==3:
        bodyList.append(physicsEngine.body2d(vector(x3,y3),theta3,mass3,speed3,accel3,radius3))
run=True
bodyList[0].draw(win,WIDTH,HEIGHT)
bodyList[1].draw(win,WIDTH,HEIGHT)
#for i in range(3):
while run:
    if dimensions==2:
        clock.tick(60)
        win.fill((0,0,0))
        for i in bodyList:
            if i.num==2:
                i.update(win,WIDTH,HEIGHT,bodyList)
        bodyList[0].draw(win,WIDTH,HEIGHT)
        pygame.display.update()
        time.sleep(1)
        for event in pygame.event.get():
            if event.type==pygame.QUIT or event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                pygame.quit()
                exit()
    else:
        for i in bodyList:
            i.update()