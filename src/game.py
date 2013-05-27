import util
import player
from viz import drawable

from player import Player

class Game(drawable):
    
    def __init__(self):
        self.id = None
        self.state = 'Not Started'
        self.players = []
        self.turn = 0;
    
    def start_new_game(self):
        self.id = util.id_generator()
        self.state = 'Waiting for players'
            
    def add_new_player(self, name):
        if len(self.players) < 4:
            newPlayer = Player(name)
            self.players.append(newPlayer)
            return [newPlayer.id,newPlayer.token]
    
    def execute_command(self):
        return
    
    def get_player(self, playerid):
        for player in self.players :
            if player.id == playerid:
                return player
    
    def draw(self, pygame, pygame, screen):
        pygame.draw.rect(screen, (  0,   0,   0), [75, 10, 50, 20], 2)