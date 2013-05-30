import util
import player
from math import fabs
from viz import drawable

from player import Player

SIZE = 20
TL = (20, 20)
TR = (760, 20)
BR = (760, 560)
BL = (20, 560)

units = []

matrix = [
['B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A' , 'A', 'A' , 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B'],
['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A' , 'A', 'A' , 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B'],
['B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A' , 'A', 'A' , 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B'],
['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A' , 'A', 'A' , 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B'],
['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A' , 'A', 'A' , 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B'],
['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A' , 'A', 'A' , 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B'],
['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A' , 'A', 'A' , 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B'],
['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A' , 'A', 'A' , 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B'],
['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A' , 'A', 'A' , 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B'],
['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A' , 'A', 'A' , 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B'],
['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A' , 'A', 'A' , 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B'],
['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A' , 'A', 'A' , 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B'],
['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A' , 'A', 'A' , 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B'],
['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A' , 'A', 'A' , 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B'],
['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A' , 'A', 'A' , 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B'],
['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A' , 'A', 'A' , 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B'],
['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A' , 'A', 'A' , 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B'],
['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A' , 'A', 'A' , 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B'],
['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A' , 'A', 'A' , 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B'],
['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A' , 'A', 'A' , 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B'],
['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A' , 'A', 'A' , 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B'],
['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A' , 'A', 'A' , 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B'],
['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A' , 'A', 'A' , 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B'],
['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A' , 'A', 'A' , 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B'],
['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A' , 'A', 'A' , 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B'],
['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A' , 'A', 'A' , 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B'],
['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A' , 'A', 'A' , 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B'],
['B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A' , 'A', 'A' , 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B'],
['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A' , 'A', 'A' , 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B'],
['B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A' , 'A', 'A' , 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B'],
['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B' , 'B', 'B' , 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
]

print len(matrix)
print len(matrix[29])

class Game(drawable):
    
    def __init__(self):
        self.state = 'Not Started'
        self.players = []
        self.turn = 0;
    
    def start_new_game(self):
        self.id = util.id_generator()
        self.state = 'Waiting for players'
            
    def add_new_player(self, name):
        if len(self.players) < 4:
            newPlayer = Player(name, len(self.players) + 1)
            self.players.append(newPlayer)
            for unit in newPlayer.units:
                units.append(unit)
            return [newPlayer.id, newPlayer.token]
    
    def execute_command(self, player, unit, command):
        target = self.get_player(player).get_unit(unit)
        
        moveCapable = self.move_capable(target, command)
        print moveCapable
        if target.x % 20 == 0 and moveCapable:
            if command == 'up' :
                return target.up()
            elif command == 'down' :
                return target.down()
            else:
                return '{"result":"failed"}'
        if target.y % 20 == 0 and moveCapable:
            if command == 'left' :
                return target.left()
            elif command == 'right' :
                return target.right()
            else:
                return '{"result":"failed"}'
        return '{"result":"failed"}'
    
    def get_player(self, playerid):
        for player in self.players :
            if player.id == playerid:
                return player
    
    def start(self):
        pass
    
    def move_capable(self, unit, command):
        m_x = int((unit.x / 20))
        m_y = int((unit.y / 20))
        if command == 'up' :
            if matrix[m_y - 1][m_x] == 'A':
                return True
            else:
                return False
        elif command == 'down' :
            if matrix[m_y + 1][m_x] == 'A':
                return True
            else:
                return False
        elif command == 'left' :
            if matrix[m_y][m_x - 1] == 'A':
                return True
            else:
                return False        
        elif command == 'right' :
            if matrix[m_y][m_x + 1] == 'A':
                return True
            else:
                return False
        
    
    def draw(self, pygame, screen):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 'A':
                    pygame.draw.rect(screen, (0, 0, 255), [20 * j, 20 * i, 20, 20], 2)
                elif matrix[i][j] == 'B':
                    pygame.draw.rect(screen, (255, 0, 255), [20 * j, 20 * i, 20, 20], 2)
        for drawable in self.players:
            drawable.draw(pygame, screen)
            
    def vision_to_json(self, target):
        found = []
        for unit in units:
            if  fabs(unit.x - target.x) < 10 and fabs(unit.y - target.y) < 10 :
                if unit.owner != target.owner :
                    found.append(unit)
        message = '{ "units":[ '
        for unit in found:
            message += unit.to_json() + ", "
        message += ' ]}'
        return message
        
            
    def to_json(self):
        return '{ "players" : "' + str(len(self.players)) + '"}'