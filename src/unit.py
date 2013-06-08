import util
from random import randint
from viz import drawable
from math import pi
from game import SIZE
from viz import WIN_HEIGHT
from viz import WIN_WIDTH

TL = (SIZE, SIZE)
TR = (WIN_WIDTH - (2 * SIZE), SIZE)
BR = (WIN_WIDTH - (2 * SIZE), WIN_HEIGHT - (2 * SIZE))
BL = (SIZE, WIN_HEIGHT - (2 * SIZE))

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
        self.A1 = SIZE / 2
        self.A2 = 0
        self.B1 = 0
        self.B2 = SIZE
        self.C1 = SIZE
        self.C2 = SIZE
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
            self.y -= SIZE
        elif self.utype == 'C' :
            self.x += SIZE
        elif self.utype == 'D' :
            self.y += SIZE
        elif self.utype == 'E' :
            self.x -= SIZE
            
    def up(self):
        if self.x % SIZE == 0 and self.y > 0: 
            self.y -= 1
            self.rad_start = 3 * pi / 4
            self.rad_end = 9 * pi / 4
            self.A1 = SIZE / 2
            self.A2 = 0
            self.B1 = 0
            self.B2 = SIZE
            self.C1 = SIZE
            self.C2 = SIZE
            return '{"result":"success"}'
        else:
            return '{"result":"blocked"}'

    def down(self):
        if self.x % SIZE == 0 and self.y < WIN_HEIGHT - SIZE:
            self.y += 1
            self.rad_start = 7 * pi / 4
            self.rad_end = 13 * pi / 4
            self.A1 = 0
            self.A2 = 0
            self.B1 = SIZE / 2
            self.B2 = SIZE
            self.C1 = SIZE
            self.C2 = 0
            return '{"result":"success"}'
        else:
            return '{"result":"blocked"}'        
    
    def left(self):
        if self.y % SIZE == 0 and self.x > 0:
            self.x -= 1
            self.A1 = 0
            self.A2 = SIZE / 2
            self.B1 = SIZE
            self.B2 = 0
            self.C1 = SIZE
            self.C2 = SIZE
            self.rad_start = 5 * pi / 4
            self.rad_end = 11 * pi / 4
            return '{"result":"success"}'
        else:
            return '{"result":"blocked"}'
            
    def right(self):
        if self.y % SIZE == 0 and self.x < WIN_WIDTH - SIZE:
            self.x += 1
            self.A1 = SIZE
            self.A2 = SIZE / 2
            self.B1 = 0
            self.B2 = 0
            self.C1 = 0
            self.C2 = SIZE
            self.rad_start = pi / 4
            self.rad_end = 7 * pi / 4
            return '{"result":"success"}'
        else:
            return '{"result":"blocked"}'
                       
    def draw(self, pygame, screen):
        pygame.draw.arc(screen, self.color, [self.x, self.y, SIZE, SIZE], self.rad_start, self.rad_end, 3)
        pygame.draw.polygon(screen, self.color, [[self.x + self.A1, self.y + self.A2], [self.x + self.B1, self.y + self.B2], [self.x + self.C1, self.y + self.C2]], 3)
   
    def to_json(self):
        return '{ "id" : "' + self.id + '" , "x" : "' + str(self.x) + '", "y" : "' + str(self.y) + '", "condition" : "' + self.condition + '" }'
