import PySimpleGUI  as ps

def runStartWindow():
    layout=[[]]
    win=ps.Window(title='Start Configuration',layout=layout,margins=[250,250])
    win.read()

runStartWindow()