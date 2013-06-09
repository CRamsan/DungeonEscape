import util
import player
from math import fabs
from viz import drawable
from time import sleep
from player import Player

import constants

TL = (constants.SIZE, constants.SIZE)
TR = ((constants.SIZE * constants.WIDTH) - (2 * constants.SIZE), constants.SIZE)
BR = ((constants.SIZE * constants.WIDTH) - (2 * constants.SIZE), (constants.SIZE * constants.HEIGHT) - (2 * constants.SIZE))
BL = (constants.SIZE, (constants.SIZE * constants.HEIGHT) - (2 * constants.SIZE))

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
        self.turn = 0
    
    def generate_map(self, matrix, start_h, end_h, start_v, end_v):
        print str((end_h - start_h) * (end_v - start_v))+"\n"
        if (end_h - start_h) * (end_v - start_v) > 25 :
            self.generate_map(matrix, start_h, end_h / 2, start_v, end_v / 2)
            self.generate_map(matrix, int(end_h / 2) + 1, end_h, start_v, end_v / 2)
            self.generate_map(matrix, start_h, end_h / 2, int(start_v / 2) + 1, end_v)
            self.generate_map(matrix, int(end_h / 2) + 1, end_h, int(start_v / 2) + 1, end_v)
        else :
            for i in range(start_v , end_v):
                for j in range(start_h, end_h):
                    matrix[j][i] = 'B'    

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
            if target.x % constants.SIZE == 0 and moveCapable:
                print str(target.x) + " - " +str(target.y - 1) + "\n"
                return target.up()
            else:
                return '{"result":"failed", "reason":"Y movement failed"}'
        elif command == 'down' :
            if target.x % constants.SIZE == 0 and moveCapable:
                print str(target.x) + " - " +str(target.y + 1) + "\n"
                return target.down()
            else:
                return '{"result":"failed", "reason":"Y movement failed"}'
        if command == 'left' :
            if target.y % constants.SIZE == 0 and moveCapable:
                print str(target.x - 1) + " - " +str(target.y) + "\n"
                return target.left()
            else:
                return '{"result":"failed", "reason":"X movement failed"}'
        elif command == 'right' :
            if target.y % constants.SIZE == 0 and moveCapable:
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
            m_x = int((unit.x / constants.SIZE))
            m_y = int(((unit.y - 1) / constants.SIZE))
            print "NEXT TILE: " + str(m_x) + " - " + str(m_y)
            if matrix[m_y][m_x] == 'A':
                return True
            else:
                return False
        elif command == 'down' :
            m_x = int((unit.x / constants.SIZE))
            m_y = int(((unit.y + 1) / constants.SIZE))
            print "NEXT TILE: " + str(m_x) + " - " + str(m_y)
            if matrix[m_y][m_x] == 'A':
                return True
            else:
                return False
        elif command == 'left' :
            m_x = int(((unit.x - 1) / constants.SIZE))
            m_y = int((unit.y / constants.SIZE))
            print "NEXT TILE: " + str(m_x) + " - " + str(m_y)
            if matrix[m_y][m_x] == 'A':
                return True
            else:
                return False        
        elif command == 'right' :
            m_x = int(((unit.x + 1) / constants.SIZE))
            m_y = int((unit.y / constants.SIZE))
            print "NEXT TILE: " + str(m_x) + " - " + str(m_y)
            if matrix[m_y][m_x] == 'A':
                return True
            else:
                return False
        
    
    def draw(self, pygame, screen):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 'A':
                    pygame.draw.rect(screen, (0, 0, 255), [constants.SIZE * j, constants.SIZE * i, constants.SIZE, constants.SIZE], 2)
                elif matrix[i][j] == 'B':
                    pygame.draw.rect(screen, (255, 0, 255), [constants.SIZE * j, constants.SIZE * i, constants.SIZE, constants.SIZE], 2)
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
