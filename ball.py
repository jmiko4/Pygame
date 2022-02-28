import pygame
from pygame.locals import *

class ball():

    def __init__(self, velocity):
        #establish variables
        self.center_x = 200
        self.center_y = 200
        self.velocity_dx = velocity
        self.velocity_dy = velocity
        self.alive = False

    def draw(self, screen, color):
        #draw the ball to the screen
        pygame.draw.circle(screen, color, [self.center_x, self.center_y], 10)

    def advance(self):
        self.center_x += self.velocity_dx
        self.center_y += self.velocity_dy

    #changes the vertical direction of the ball
    def bounce_vertical(self):
        self.velocity_dy *= -1

    #changes the horizontal direction of the ball
    def bounce_horizontal(self):
        self.velocity_dx *= -1