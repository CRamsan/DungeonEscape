import util
import player
import random
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
        for i in range(constants.HEIGHT + 1):
            tmp = []
            for k in range(constants.WIDTH + 1):
                tmp.append('C')
            self.matrix.append(tmp)
                    
        self.generate_map(self.matrix, 0, constants.WIDTH - 1, 0, constants.HEIGHT - 1, 0, skip_1, 'B') 
        self.generate_map(self.matrix, 0, constants.WIDTH - 1, 0, constants.HEIGHT - 1, 0, skip_2, 'B')        
        self.generate_map(self.matrix, 0, constants.WIDTH - 1, 0, constants.HEIGHT - 1, 0, skip_3, 'D')
        #self.generate_map(self.matrix, 0, constants.WIDTH - 1, 0, constants.HEIGHT - 1, 0, 10, 'D')

    def generate_map(self, matrix, start_h, end_h, start_v, end_v, depth, skip, tile):
        if depth < 3:
            self.generate_map(self.matrix, start_h,                             start_h + ((end_h - start_h)/2), start_v,                         start_v + ((end_v - start_v)/2), depth + 1, skip, tile)
            self.generate_map(self.matrix, start_h + ((end_h - start_h)/2) + 1, end_h,                           start_v,                         start_v + ((end_v - start_v)/2), depth + 1, skip, tile)
            self.generate_map(self.matrix, start_h,                             start_h + ((end_h - start_h)/2), start_v + ((end_v - start_v)/2), end_v,                           depth + 1, skip, tile)
            self.generate_map(self.matrix, start_h + ((end_h - start_h)/2) + 1, end_h,                           start_v + ((end_v - start_v)/2), end_v,                           depth + 1, skip, tile)
        else :
            if tile == 'D' :
				for i in range(start_h, start_h + ((end_h - start_h)/2), skip) :
					for j in range(start_v, start_v + ((end_v - start_v)/2), skip) :
						matrix[j][i] = tile
            else :
                r = random.randint(0,2)
                if r == 0 :
                    self.create_cross(matrix,  start_h + ((end_h - start_h)/2) , start_v + ((end_v - start_v)/2), ((end_v - start_v)/2) - 1 )
                elif r == 1 :
                    for i in range(start_v , end_v + 1, skip):
                        self.create_v_line(matrix,  start_h + ((end_h - start_h)/2) , start_v + ((end_v - start_v)/2), ((end_v - start_v)/2) - 1 )
                elif r == 2 :
                    for i in range(start_h , end_h + 1, skip):
                        self.create_h_line(matrix,  start_h + ((end_h - start_h)/2) , start_v + ((end_v - start_v)/2), ((end_v - start_v)/2) - 1 )
                            
    def create_cross(self, matrix, x, y, number):
        matrix[y][x] = 'B'
        self.up(matrix, x, y - 1, number - 1)
        self.down(matrix, x, y + 1, number - 1)
        self.left(matrix, x - 1, y, number - 1)
        self.right(matrix, x + 1, y, number - 1)
    
    def create_h_line(self, matrix, x, y, number):
        matrix[y][x] = 'B'
        self.left(matrix, x - 1, y, number - 1)
        self.right(matrix, x + 1, y, number - 1)

    def create_v_line(self, matrix, x, y, number):
        matrix[y][x] = 'B'
        self.up(matrix, x, y - 1, number - 1)
        self.down(matrix, x, y + 1, number - 1)
        
    def up(self, matrix, x, y, number):
        matrix[y][x] = 'B'
        if number > 1 :
            self.up(matrix, x, y - 1, number - 1)
            
    def down(self, matrix, x, y, number):
        matrix[y][x] = 'B'
        if number > 1 :
            self.up(matrix, x, y + 1, number - 1)

    def left(self, matrix, x, y, number):
        matrix[y][x] = 'B'
        if number > 1 :
            self.up(matrix, x-1, y, number - 1)

    def right(self, matrix, x, y, number):
        matrix[y][x] = 'B'
        if number > 1 :
            self.up(matrix, x+1, y, number - 1)            
            
                             
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
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 'B':
                    pygame.draw.rect(screen, (0, 0, 255), [(constants.SIZE * j), (constants.SIZE * i), constants.SIZE, constants.SIZE], 2)
                elif self.matrix[i][j] == 'C':
                    pygame.draw.ellipse(screen, (255, 0, 255), [(constants.SIZE * j) + 9, (constants.SIZE * i) + 9, constants.SIZE - (2*9), constants.SIZE - (2*9)])
                elif self.matrix[i][j] == 'D':
                    pygame.draw.ellipse(screen, (255, 255, 0), [(constants.SIZE * j) + 7, (constants.SIZE * i) + 7, constants.SIZE - (2*7), constants.SIZE - (2*7)])
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
