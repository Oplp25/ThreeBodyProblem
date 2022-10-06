import PySimpleGUI  as ps

def runStartWindow():
    layout=[[ps.Text('Complexity:   '),ps.Text('Newtonian'),ps.Radio('','mechanics',key='N',default=True),ps.Text('Relativistic'),ps.Radio('','mechanics',key='R',default=False)],
    [ps.Text('Number of Dimensions:   '),ps.Text('2'),ps.Radio('','dimensions',key='2',default=True),ps.Text('3'),ps.Radio('','dimensions',key='3',default=False)],
    [ps.Text('Number of Bodies'),ps.Input(default_text=2,key='bodies')],
    [ps.Text('Starting position of body 1'),ps.Text('x:'),ps.Input(0,key='x1'),ps.Text('y:'),ps.Input(0,key='y1'),ps.Text('z:'),ps.Input(0,key='z1')],
    [ps.Text('Starting direction of travel of body 1'),ps.Text('x:'),ps.Input(0,key='xv1'),ps.Text('y:'),ps.Input(0,key='yv1'),ps.Text('z:'),ps.Input(0,key='zv1')],
    [ps.Text('Mass of body 1'),ps.Input(0,key='mass1')],
    [ps.Text('Speed of body 1'),ps.Input(0,key='speed1')],
    [ps.Text('Acceleration of body 1'),ps.Input(0,key='accel1')],
    [ps.Text('Radius of body 1'),ps.Input(0,key='radius1')],
    [ps.Text('')],
    [ps.Text('Starting position of body 2'),ps.Text('x:'),ps.Input(0,key='x2'),ps.Text('y:'),ps.Input(0,key='y2'),ps.Text('z:'),ps.Input(0,key='z2')],
    [ps.Text('Starting direction of travel of body 2'),ps.Text('x:'),ps.Input(0,key='xv2'),ps.Text('y:'),ps.Input(0,key='yv2'),ps.Text('z:'),ps.Input(0,key='zv2')],
    [ps.Text('Mass of body 2'),ps.Input(0,key='mass2')],
    [ps.Text('Speed of body 2'),ps.Input(0,key='speed2')],
    [ps.Text('Acceleration of body 2'),ps.Input(0,key='accel2')],
    [ps.Text('Radius of body 2'),ps.Input(0,key='radius2')],
    [ps.Text('')],
    [ps.Text('Starting position of body 3'),ps.Text('x:'),ps.Input(0,key='x3'),ps.Text('y:'),ps.Input(0,key='y3'),ps.Text('z:'),ps.Input(0,key='z3')],
    [ps.Text('Starting direction of travel of body 3'),ps.Text('x:'),ps.Input(0,key='xv3'),ps.Text('y:'),ps.Input(0,key='yv3'),ps.Text('z:'),ps.Input(0,key='zv3')],
    [ps.Text('Mass of body 3'),ps.Input(0,key='mass3')],
    [ps.Text('Speed of body 3'),ps.Input(0,key='speed3')],
    [ps.Text('Acceleration of body 3'),ps.Input(0,key='accel3')],
    [ps.Text('Radius of body 3'),ps.Input(0,key='radius3')],
    [ps.Button('Run Simulation')]]
    win=ps.Window(title='Start Configuration',layout=layout,margins=[50,50])
    win.read()
    run=True
    while run:
        events,values=win.read()
        if 'Run Simulation' in events:
            if values['N']:
                mechanicsType='N'
            else:
                mechanicsType='R'
            if values['2']:
                dimensions=2
            else:
                dimension=3
            numbBodies=int(values['bodies'])
            x1=int(values['x1'])
            y1=int(values['y1'])
            z1=int(values['z1'])
            xv1=int(values['xv1'])
            yv1=int(values['yv1'])
            zv1=int(values['zv1'])
            mass1=int(values['mass1'])
            speed1=int(values['speed1'])
            accel1=int(values['accel1'])
            radius1=int(values['radius1'])
            x2=int(values['x2'])
            y2=int(values['y2'])
            z2=int(values['z2'])
            xv2=int(values['xv2'])
            yv2=int(values['yv2'])
            zv2=int(values['zv2'])
            mass2=int(values['mass2'])
            speed2=int(values['speed2'])
            accel2=int(values['accel2'])
            radius2=int(values['radius2'])
            x3=int(values['x3'])
            y3=int(values['y3'])
            z3=int(values['z3'])
            xv3=int(values['xv3'])
            yv3=int(values['yv3'])
            zv3=int(values['zv3'])
            mass3=int(values['mass3'])
            speed3=int(values['speed3'])
            accel3=int(values['accel3'])
            radius3=int(values['radius3'])
            run=False
    win.close()
    return mechanicsType,numbBodies,dimensions,x1,y1,z1,xv1,yv1,zv1,mass1,speed1,accel1,radius1,x2,y2,z2,xv2,yv2,zv2,mass2,speed2,accel2,radius2,x3,y3,z3,xv3,yv3,zv3,mass3,speed3,accel3,radius3