import util
from viz import drawable

class Unit(drawable):
    
    def __init__(self, utype):
        self.id = util.id_generator()
        self.condition = 'Normal'
        self.x = None
        self.y = None
        self.utype = utype
        
        
    def draw(self, pygame, screen):
        pygame.draw.ellipse(screen, (255, 255, 0), [225, 10, 50, 20], 2) 

    