import util
import player
from math import fabs
from viz import drawable
from time import sleep
from player import Player

SIZE = 20
WIDTH = 40
HEIGHT = 30
VISION_RANGE = 100

TL = (SIZE, SIZE)
TR = ((SIZE * WIDTH) - (2 * SIZE), SIZE)
BR = ((SIZE * WIDTH) - (2 * SIZE), (SIZE * HEIGHT) - (2 * SIZE))
BL = (SIZE, (SIZE * HEIGHT) - (2 * SIZE))

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
        if command == 'up' :
            if target.x % SIZE == 0 and moveCapable:
                print str(target.x) + " - " +str(target.y - 1) + "\n"
                return target.up()
            else:
                return '{"result":"failed", "reason":"Y movement failed"}'
        elif command == 'down' :
            if target.x % SIZE == 0 and moveCapable:
                print str(target.x) + " - " +str(target.y + 1) + "\n"
                return target.down()
            else:
                return '{"result":"failed", "reason":"Y movement failed"}'
        if command == 'left' :
            if target.y % SIZE == 0 and moveCapable:
                print str(target.x - 1) + " - " +str(target.y) + "\n"
                return target.left()
            else:
                return '{"result":"failed", "reason":"X movement failed"}'
        elif command == 'right' :
            if target.y % SIZE == 0 and moveCapable:
                print str(target.x + 1) + " - " +str(target.y) + "\n"
                return target.right()
            else:
                return '{"result":"failed", "reason":"X movement failed"}'
        else:
            return '{"result":"failed", "reason":"X/Y movement failed"}'        
    
    def get_player(self, playerid):
        for player in self.players :
            if player.id == playerid:
                return player
    
    def start(self):
        pass
    
    def move_capable(self, unit, command):
        if command == 'up' :
            m_x = int((unit.x / SIZE))
            m_y = int(((unit.y - 1) / SIZE))
            print "NEXT TILE: " + str(m_x) + " - " + str(m_y)
            if matrix[m_y][m_x] == 'A':
                return True
            else:
                return False
        elif command == 'down' :
            m_x = int((unit.x / SIZE))
            m_y = int(((unit.y + 1) / SIZE))
            print "NEXT TILE: " + str(m_x) + " - " + str(m_y)
            if matrix[m_y][m_x] == 'A':
                return True
            else:
                return False
        elif command == 'left' :
            m_x = int(((unit.x - 1) / SIZE))
            m_y = int((unit.y / SIZE))
            print "NEXT TILE: " + str(m_x) + " - " + str(m_y)
            if matrix[m_y][m_x] == 'A':
                return True
            else:
                return False        
        elif command == 'right' :
            m_x = int(((unit.x + 1) / SIZE))
            m_y = int((unit.y / SIZE))
            print "NEXT TILE: " + str(m_x) + " - " + str(m_y)
            if matrix[m_y][m_x] == 'A':
                return True
            else:
                return False
        
    
    def draw(self, pygame, screen):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 'A':
                    pygame.draw.rect(screen, (0, 0, 255), [SIZE * j, SIZE * i, SIZE, SIZE], 2)
                elif matrix[i][j] == 'B':
                    pygame.draw.rect(screen, (255, 0, 255), [SIZE * j, SIZE * i, SIZE, SIZE], 2)
        for drawable in self.players:
            drawable.draw(pygame, screen)
            
    def vision_to_json(self, target):
        found = []
        for unit in units:
            if  fabs(unit.x - target.x) < VISION_RANGE and fabs(unit.y - target.y) < VISION_RANGE :
                if unit.owner != target.owner :
                    found.append(unit)
        message = '{ "units":[ '
        for unit in found:
            message += unit.to_json() + ", "
        message += ' ]}'
        return message
        
            
    def to_json(self):
        return '{ "players" : "' + str(len(self.players)) + '"}'
