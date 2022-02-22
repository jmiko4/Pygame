import pygame
from pygame.locals import *

class ball():

    def __init__(self):
        #establish variables
        self.center_x = 200
        self.center_y = 200
        self.center = (self.center_x, self.center_y)
        self.velocity_dx = 1
        self.velocity_dy = 1

    def draw(self):
        #draw the ball to the screen
        pygame.draw.circle(surface, color, self.center, radius)