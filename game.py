import pygame
from pygame.locals import *
from ball import ball
print("edit")

pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional
 
HEIGHT = 720
WIDTH = 1280
ACC = 0.5
FRIC = -0.12
FPS = 60

WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)

score = 0
lives = 3

carryOn = True
 
FramePerSec = pygame.time.Clock()
 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout")

clock = pygame.time.Clock()

ball = ball()

while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
 
    # --- Game logic should go here
    ball.advance()
    print (ball.center_y, ball.center_x)
 
    # --- Drawing code should go here
    # First, clear the screen to dark blue. 
    screen.fill(DARKBLUE)
    pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)
    ball.draw(screen, WHITE)

    #Display the score and the number of lives at the top of the screen
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20,10))
    text = font.render("Lives: " + str(lives), 1, WHITE)
    screen.blit(text, (650,10))
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
    # --- Limit to 60 frames per second
    clock.tick(FPS)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()