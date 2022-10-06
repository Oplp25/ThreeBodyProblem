import startWindow,physicsEngine, panda3d, time
from vector import vector
speed=5
mechanicsType,numbBodies,dimensions,x1,y1,z1,xv1,yv1,zv1,mass1,speed1,accel1,radius1,x2,y2,z2,xv2,yv2,zv2,mass2,speed2,accel2,radius2,  x3,y3,z3,  xv3,yv3,zv3,  mass3,speed3,accel3,radius3  ='N',2,2,   20,20,0,  -400,-500,0,  0,speed,0,10,  -20,2,0,  0,4,-70,  0,speed,0,10,  0,0,0,0,0,0,0,0,0,0#startWindow.runStartWindow()
bodyList=[]
if dimensions==3:
    bodyList.append(physicsEngine.body3d(vector(x1,y1,z1),vector(xv1,yv1,zv1),mass1,speed1,accel1,radius1))
    if numbBodies>=2:
        bodyList.append(physicsEngine.body3d(vector(x2,y2,z2),vector(xv2,yv2,zv2),mass2,speed2,accel2,radius2))
    if numbBodies==3:
        bodyList.append(physicsEngine.body3d(vector(x3,y3,z3),vector(xv3,yv3,zv3),mass3,speed3,accel3,radius3))
else:
    bodyList.append(physicsEngine.body2d(vector(x1,y1),vector(xv1,yv1),mass1,speed1,accel1,radius1,1))
    if numbBodies>=2:
        bodyList.append(physicsEngine.body2d(vector(x2,y2),vector(xv2,yv2),mass2,speed2,accel2,radius2,2))
    if numbBodies==3:
        bodyList.append(physicsEngine.body2d(vector(x3,y3),vector(xv3,yv3),mass3,speed3,accel3,radius3))
run=True
while run:
    for i in bodyList:
        i.update()
        #time.sleep(1)