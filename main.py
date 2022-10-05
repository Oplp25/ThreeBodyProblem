import startWindow,physicsEngine, panda3d
from vector import vector
mechanicsType,numbBodies,x1,y1,z1,xv1,yv1,zv1,mass1,speed1,accel1,x2,y2,z2,xv2,yv2,zv2,mass2,speed2,accel2,x3,y3,z3,xv3,yv3,zv3,mass3,speed3,accel3=startWindow.runStartWindow()
bodyList=[]
bodyList.append(physicsEngine.body(vector(x1,y1,z1),vector(xv1,yv1,zv1),mass1,speed1,accel1))
if numbBodies>=2:
    bodyList.append(physicsEngine.body(vector(x2,y2,z2),vector(xv2,yv2,zv2),mass2,speed2,accel2))
if numbBodies==3:
    bodyList.append(physicsEngine.body(vector(x3,y3,z3),vector(xv3,yv3,zv3),mass3,speed3,accel3))
run=True
while run:
    for i in bodyList:
        i.update()