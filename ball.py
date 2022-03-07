import pygame
from random import randint
from random import choice


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
        
<<<<<<< HEAD
        self.velocity = [randint(4,5),randint(-1,1)]
=======
        self.velocity = [randint(4,8),randint(1,8)]
>>>>>>> 95488032f4b4319e096629dbb37b667a3f6c5d6c
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
          
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
<<<<<<< HEAD
        self.velocity[1] = randint(-800,1)
=======
        self.velocity[1] = choice([i for i in range(-7,7) if i not in [0]])
>>>>>>> 95488032f4b4319e096629dbb37b667a3f6c5d6c
