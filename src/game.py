import util
import player
import random
from random import choice
from math import fabs
from viz import drawable
from time import sleep
from player import Player
from math import pi
 
import constants

TL = (constants.SIZE, constants.SIZE)
TR = ((constants.SIZE * constants.WIDTH) - (2 * constants.SIZE), constants.SIZE)
BR = ((constants.SIZE * constants.WIDTH) - (2 * constants.SIZE), (constants.SIZE * constants.HEIGHT) - (2 * constants.SIZE))
BL = (constants.SIZE, (constants.SIZE * constants.HEIGHT) - (2 * constants.SIZE))

units = []

class Game(drawable):
    
    def __init__(self):
        self.state = 'Not Started'
        self.players = []
        self.turn = 0
        self.matrix = []

    def generate_the_map(self, skip_1=2, skip_2=3, skip_3=9):
        self.matrix = []
        for i in range(constants.WIDTH + 1):
            tmp = []
            for k in range(constants.HEIGHT + 1):
                tmp.append('B')
            self.matrix.append(tmp)
                    
        self.generate_map(self.matrix) 

    def generate_map(self, matrix):
        for i in range(len(self.matrix)/3):
            v_start = i + 1
            lower_bound = False
            for j in range(v_start) :
                v_limit = j
                if v_limit >= (len(self.matrix[0])/3):
                    v_limit = (len(self.matrix[0])/3) - 1
                    lower_bound = True
                    break
                self.generate_cel(matrix, ((i*3) + 1), ((v_limit*3) + 1))
            if lower_bound :
                continue
            for k in range(i) :
                tmp = i - k - 1
                self.generate_cel(matrix,((tmp*3) + 1), ((v_limit*3) + 1))

    def generate_cel(self, matrix, x, y):
        matrix[x][y] = 'D'
        options = ['u', 'd', 'l', 'r']
        exits = 0
        if x - 1 == 0:
            options.remove('l')
        if y - 1 == 0:
            options.remove('u')
        if x + 1 == constants.WIDTH - 1:
            options.remove('r')
        if y + 1 == constants.HEIGHT - 1:
            options.remove('d')
        
        if x - 2 >= 0 :
            if matrix[x - 2][y] == 'D':
                matrix[x - 1][y] = 'D'
                options.remove('l')
                exits+=1
                print "LEFT"
                sleep(0.001)
        if y - 2 >= 0 :
            if matrix[x][y - 2] == 'D':
                matrix[x][y - 1] = 'D'
                print "UP"
                exits+=1
                options.remove('u')
                sleep(0.001)
        if x + 2 < constants.WIDTH - 1 :
            if matrix[x + 2][y] == 'D':
                matrix[x + 1][y] = 'D'
                options.remove('r')
                print "RIGHT"
                exits+=1
                sleep(0.001)
        if y + 2 < constants.HEIGHT - 1:
            if matrix[x][y + 2] == 'D':
                matrix[x][y + 1] = 'D'
                options.remove('d')
                print "DOWN"
                exits+=1
                sleep(0.001)

        while exits < 4  and len(options) > 0:
            if exits == 3:
                if random.randint(0, 100) <= 100:
                    break
            if exits == 4:
                if random.randint(0, 100) <= 85:
                    break
            direction = choice(options)
            options.remove(direction)
            if direction == 'l' :
                matrix[x - 1][y] = 'D'
            elif direction == 'u' :
                matrix[x][y - 1] = 'D'
            elif direction == 'r':
                matrix[x + 1][y] = 'D'
            elif direction == 'd' :
                matrix[x][y + 1] = 'D'
            exits+=1
            sleep(0.001)
                    
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
                return target.up()
            else:
                return '{"result":"failed", "reason":"Y movement failed"}'
        elif command == 'down' :
            if target.x % constants.SIZE == 0 and moveCapable:
                return target.down()
            else:
                return '{"result":"failed", "reason":"Y movement failed"}'
        if command == 'left' :
            if target.y % constants.SIZE == 0 and moveCapable:
                return target.left()
            else:
                return '{"result":"failed", "reason":"X movement failed"}'
        elif command == 'right' :
            if target.y % constants.SIZE == 0 and moveCapable:
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
            if self.matrix[m_y][m_x] != 'B':
                return True
            else:
                return False
        elif command == 'down' :
            m_x = int((unit.x / constants.SIZE))
            m_y = int(((unit.y + constants.SIZE + 1) / constants.SIZE))
            print "NEXT TILE: " + str(m_x) + " - " + str(m_y)
            if self.matrix[m_y][m_x] != 'B':
                return True
            else:
                return False
        elif command == 'left' :
            m_x = int(((unit.x - 1) / constants.SIZE))
            m_y = int((unit.y / constants.SIZE))
            print "NEXT TILE: " + str(m_x) + " - " + str(m_y)
            if self.matrix[m_y][m_x] != 'B':
                return True
            else:
                return False        
        elif command == 'right' :
            m_x = int(((unit.x + constants.SIZE + 1) / constants.SIZE))
            m_y = int((unit.y / constants.SIZE))
            print "NEXT TILE: " + str(m_x) + " - " + str(m_y)
            if self.matrix[m_y][m_x] != 'B':
                return True
            else:
                return False
        
    
    def draw(self, pygame, screen):
        for i in range(len(self.matrix) - 1):
            for j in range(len(self.matrix[i]) - 1):
                if self.matrix[i][j] == 'B':
                    pygame.draw.rect(screen, (0, 0, 255), [(constants.SIZE * i), (constants.SIZE * j), constants.SIZE, constants.SIZE], 2)
                elif self.matrix[i][j] == 'C':
                    pygame.draw.ellipse(screen, (255, 0, 255), [(constants.SIZE * i) + 9, (constants.SIZE * j) + 9, constants.SIZE - (2*9), constants.SIZE - (2*9)])
                elif self.matrix[i][j] == 'D':
                    pygame.draw.ellipse(screen, (255, 255, 0), [(constants.SIZE * i) + 7, (constants.SIZE * j) + 7, constants.SIZE - (2*7), constants.SIZE - (2*7)])
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
