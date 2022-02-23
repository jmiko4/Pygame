import pygame
from pygame.locals import *

class ball():

    def __init__(self):
        #establish variables
        self.center_x = 200
        self.center_y = 200
        self.center = [self.center_x, self.center_y]
        self.velocity_dx = 1
        self.velocity_dy = 1

    def draw(self, screen, color):
        #draw the ball to the screen
        pygame.draw.circle(screen, color, self.center, 10)

    def bounce_vertical(self):
        self.velocity_dy *= -1

    def bounce_horizontal(self):
        self.velocity_dx *= -1