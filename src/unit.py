import util
from viz import drawable

SIZE = 20
TL =   (20,   20)
TR =   (760,   20)
BR =   (760,   560)
BL =   (20,   560)

class Unit(drawable):
    
    def __init__(self, utype, owner):
        self.id = util.id_generator()
        self.condition = 'Normal'
        self.owner = owner
        self.utype = utype
        
        if self.owner == 1 :
            self.x = TL[0]
            self.y = TL[1]            
        elif self.owner == 2 :
            self.x = TR[0]
            self.y = TR[1]            
        elif self.owner == 3 :
            self.x = BR[0]
            self.y = BR[1]            
        elif self.owner == 4 :
            self.x = BL[0]
            self.y = BL[1]            
        
        print str(self.x) + '+' + str(self.y)
        
        if self.utype == 'A' :
            pass
        elif self.utype == 'B' :
            self.y -= SIZE
        elif self.utype == 'C' :
            self.x += SIZE
        elif self.utype == 'D' :
            self.y += SIZE
        elif self.utype == 'E' :
            self.x -= SIZE
            
    def up(self):
        pass

    def down(self):
        pass
    
    def left(self):
        pass
    
    def right(self):
        pass 
               
    def draw(self, pygame, screen):
        pygame.draw.rect(screen, (255, 255, 0), [self.x, self.y, SIZE, SIZE], 2) 
        
    def test(self):
        pass

    