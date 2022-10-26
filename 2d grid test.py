import pygame,random, vector
pygame.init()
win=pygame.display.set_mode((660,660))
def drawGrid():
    win.fill((0,255,0))
    for x,y in zip(range(77),range(77)):
        pygame.draw.rect(win,(0,0,0),(x*10,1,1,660))
        pygame.draw.rect(win,(0,0,0),(1,y*10,660,1))
    pygame.display.update()
drawGrid()
class point(vector.vector):
    def __init__(self,x,y):
        super().__init__(x,y)
    def draw(self):
        pygame.draw.circle(win,(255,0,0),(self.x,self.y),5)
pointList=[]
def draw():
    for i in pointList:
        i.draw()
    pygame.display.update()
while True:
    draw()
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            x=round(pos[0]/10)*10
            y=round(pos[1]/10)*10
            pointList.append(point(x,y))
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.KEYDOWN and event.key==pygame.K_RETURN:
            pointList=[]
            drawGrid()
