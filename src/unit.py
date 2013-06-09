import util
from random import randint
from viz import drawable
from math import pi
import game
import viz

import constants

TL = (constants.SIZE, constants.SIZE)
TR = (constants.WIN_WIDTH - (2 * constants.SIZE), constants.SIZE)
BR = (constants.WIN_WIDTH - (2 * constants.SIZE), constants.WIN_HEIGHT - (2 * constants.SIZE))
BL = (constants.SIZE, constants.WIN_HEIGHT - (2 * constants.SIZE))

'''TL = (500, 160)
TR = (580, 160)
BR = (580, 300)
BL = (500, 300)
'''

class Unit(drawable):
    
    def __init__(self, utype, owner):
        '''self.id = util.id_generator()'''
        self.id = 'ABC'
        self.condition = 'Normal'
        self.owner = owner
        self.utype = utype
        self.A1 = constants.SIZE / 2
        self.A2 = 0
        self.B1 = 0
        self.B2 = constants.SIZE
        self.C1 = constants.SIZE
        self.C2 = constants.SIZE
        self.rad_start = 0
        self.rad_end = 2 * pi 
        if self.owner == 1 :
            self.color = (0, 255, 255)
        elif self.owner == 2 :
            self.color = (0, 255, 0)
        elif self.owner == 3 :
            self.color = (255, 0, 0)
        elif self.owner == 4 :
            self.color = (255, 255, 255)
                
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
                
        if self.utype == 'A' :
            pass
        elif self.utype == 'B' :
            self.y -= constants.SIZE
        elif self.utype == 'C' :
            self.x += constants.SIZE
        elif self.utype == 'D' :
            self.y += constants.SIZE
        elif self.utype == 'E' :
            self.x -= constants.SIZE
            
    def up(self):
        if self.x % constants.SIZE == 0 and self.y > 0: 
            self.y -= 1
            self.rad_start = 3 * pi / 4
            self.rad_end = 9 * pi / 4
            self.A1 = constants.SIZE / 2
            self.A2 = 0
            self.B1 = 0
            self.B2 = constants.SIZE
            self.C1 = constants.SIZE
            self.C2 = constants.SIZE
            return '{"result":"success"}'
        else:
            return '{"result":"blocked"}'

    def down(self):
        if self.x % constants.SIZE == 0 and self.y < constants.WIN_HEIGHT - constants.SIZE:
            self.y += 1
            self.rad_start = 7 * pi / 4
            self.rad_end = 13 * pi / 4
            self.A1 = 0
            self.A2 = 0
            self.B1 = constants.SIZE / 2
            self.B2 = constants.SIZE
            self.C1 = constants.SIZE
            self.C2 = 0
            return '{"result":"success"}'
        else:
            return '{"result":"blocked"}'        
    
    def left(self):
        if self.y % constants.SIZE == 0 and self.x > 0:
            self.x -= 1
            self.A1 = 0
            self.A2 = constants.SIZE / 2
            self.B1 = constants.SIZE
            self.B2 = 0
            self.C1 = constants.SIZE
            self.C2 = constants.SIZE
            self.rad_start = 5 * pi / 4
            self.rad_end = 11 * pi / 4
            return '{"result":"success"}'
        else:
            return '{"result":"blocked"}'
            
    def right(self):
        if self.y % constants.SIZE == 0 and self.x < constants.WIN_WIDTH - constants.SIZE:
            self.x += 1
            self.A1 = constants.SIZE
            self.A2 = constants.SIZE / 2
            self.B1 = 0
            self.B2 = 0
            self.C1 = 0
            self.C2 = constants.SIZE
            self.rad_start = pi / 4
            self.rad_end = 7 * pi / 4
            return '{"result":"success"}'
        else:
            return '{"result":"blocked"}'
                       
    def draw(self, pygame, screen):
        pygame.draw.arc(screen, self.color, [self.x, self.y, constants.SIZE, constants.SIZE], self.rad_start, self.rad_end, 3)
        pygame.draw.polygon(screen, self.color, [[self.x + self.A1, self.y + self.A2], [self.x + self.B1, self.y + self.B2], [self.x + self.C1, self.y + self.C2]], 3)
   
    def to_json(self):
        return '{ "id" : "' + self.id + '" , "x" : "' + str(self.x) + '", "y" : "' + str(self.y) + '", "condition" : "' + self.condition + '" }'
