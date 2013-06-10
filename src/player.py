import util
from unit import Unit
from viz import drawable

class Player(drawable):
    
    def __init__(self, name, number):
        '''self.id = util.id_generator()'''
        self.id = 'ABC'
        self.number = number
        self.state = 'Not Started'
        self.name = name
        self.units = []
        '''self.token = util.id_generator(12)'''
        self.token = 'ABCD'             
        self.units.append(Unit('A', self.number))	        

    def validate_token(self, token):
        return self.token == token
    
    def get_unit(self, unitid):
        for unit in self.units :
            if unit.id == unitid:
                return unit
            
    def draw(self, pygame, screen):
        for drawable in self.units:
            drawable.draw(pygame, screen)
            
    def to_json(self):
        return '{ "id" : "' + self.id + ', "name" : "' + self.name + ' "}'
    
    def units_to_json(self):
        message = '[ '
        for unit in self.units:
            message += unit.to_json() + ", "
        message += ' ]'
        return message
    
    
