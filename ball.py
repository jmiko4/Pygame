import pygame
from random import randint

BLACK = (0, 0, 0)
 
class Ball(pygame.sprite.Sprite):
    #This class represents a ball. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the ball, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the ball (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        self.velocity = [randint(4,8),randint(-8,8)]
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
          
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)

class ball():

    def __init__(self, velocity, x_start, y_start):
        #establish variables
        self.center_x = x_start
        self.center_y = y_start
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
