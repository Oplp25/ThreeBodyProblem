class vector(object):
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    
    def __str__(self):
        return (str(self.x),str(self.y),str(self.z))
    
    def __add__(self,v2):
        return vector(self.x+v2.y,self.y+v2.y,self.z+v2.z)