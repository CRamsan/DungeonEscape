import pygame, sys, os
from pygame.locals import * 
import random
import time

import constants

class Visualizer():
    def vis_loop(self, game):      
         
        pygame.init() 
         
        window = pygame.display.set_mode((constants.WIN_WIDTH, constants.WIN_HEIGHT)) 
        pygame.display.set_caption('DS') 
        screen = pygame.display.get_surface() 

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
            screen.fill(constants.BLACK)
            
            game.draw(pygame, screen)
                        
            # Go ahead and update the screen with what we've drawn.
            # This MUST happen after all the other drawing commands.
            pygame.display.flip()
            
        # Be IDLE friendly
        pygame.quit()

class drawable():
    def draw(self, pygame, screen):
        pass
