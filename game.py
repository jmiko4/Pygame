import pygame
from pygame.locals import *
from ball import ball
from paddle import Paddle
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

# --- Drawing the paddle sprite
paddle = Paddle(WHITE, 100, 10)
paddle.rect.x = 20
paddle.rect.y = 200
 
#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()
 
# Add the paddle to the list of sprites
all_sprites_list.add(paddle)

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
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: #Pressing the x Key will quit the game
                     carryOn=False

    #Moving the paddle when the use uses the arrow keys
     keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(5, 0)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(5, 700) 

    # --- Game logic should go here
    all_sprites_list.update()
    ball.advance()

        #bounce off walls
    if ball.center_x < 0 and ball.velocity_dx < 0:
        ball.bounce_horizontal()
    if ball.center_x > WIDTH and ball.velocity_dx > 0:
        ball.bounce_horizontal()
    if ball.center_y < 0 and ball.velocity_dy < 0:
        ball.bounce_vertical()
    if ball.center_y > HEIGHT and ball.velocity_dy > 0:
        ball.bounce_vertical()
 
    # --- Drawing code should go here
    # First, clear the screen to dark blue. 
    screen.fill(DARKBLUE)
    pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)
    ball.draw(screen, WHITE)

    #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
    #all_sprites_list.draw(screen)

    #Display the score and the number of lives at the top of the screen
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20,10))
    text = font.render("Lives: " + str(lives), 1, WHITE)
    screen.blit(text, (650,10))
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
    # --- Limit to 60 frames per second
    clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()