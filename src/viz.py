import pygame, sys, os
from pygame.locals import * 
import random
import time

HEIGHT = 30
WIDTH = 40

class Visualizer():
    def vis_loop(self, game):      
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        BLUE = (0, 0, 255)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)
         
        pygame.init() 
         
        window = pygame.display.set_mode((800, 600)) 
        pygame.display.set_caption('DS') 
        screen = pygame.display.get_surface() 
         
        '''unit = pygame.image.load("../assets/star.png")
        unitrect = unit.get_rect()
        
        wall = pygame.image.load("../assets/black.png")
        wallrect = wall.get_rect()
        
        floor = pygame.image.load("../assets/green.png")
        floorrect = floor.get_rect()'''

        # Loop until the user clicks the close button.
        done = False
        clock = pygame.time.Clock()
         
        while not done:
         
            # This limits the while loop to a max of 10 times per second.
            # Leave this out and we will use all CPU we can.
            '''clock.tick(10)'''
            
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
         
            # All drawing code happens after the for loop and but
            # inside the main while done==False loop.
             
            # Clear the screen and set the screen background
            screen.fill(BLACK)
            
            game.draw(pygame, screen)
                        
            # Go ahead and update the screen with what we've drawn.
            # This MUST happen after all the other drawing commands.
            pygame.display.flip()
            
            '''game.test()'''
            
        # Be IDLE friendly
        pygame.quit()

class drawable():
    def draw(self, pygame, screen):
        pass
