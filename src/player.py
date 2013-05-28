import util
from viz import drawable

class Player(drawable):
    
    def __init__(self, name):
        self.id = util.id_generator()
        self.state = 'Not Started'
        self.name = name
        self.units = []
        self.token = util.id_generator(12)
    
    def validate_token(self, token):
        return self.token == token
    
    def get_unit(self, unitid):
        for unit in self.units :
            if unit.id == unitid:
                return unit
            
    def draw(self, pygame, screen):
        pygame.draw.line(screen, (0 , 255, 0), [0, 0], [50, 30], 5)
        for drawable in self.units:
            drawable.draw(pygame, screen)
