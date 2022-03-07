#Import the pygame library and initialise the game engine
import pygame
#Let's import the Paddle Class & the Ball Class
from paddle import Paddle
from ball_old import ball
from brick import Brick

pygame.init()

# Define some colors
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)

score = 0
lives = 3
ball_speed = 5

WIDTH = 500
HEIGHT = 500

# Open a new window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()

#Create the Paddle
paddle = Paddle(LIGHTBLUE, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560

#Create the ball sprite
ball = ball(WHITE,10,10)

all_bricks = pygame.sprite.Group()
for i in range(7):
    brick = Brick(RED,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 60
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(ORANGE,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 100
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(YELLOW,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 140
    all_sprites_list.add(brick)
    all_bricks.add(brick)

# Add the paddle and the ball to the list of sprites
all_sprites_list.add(paddle)
#all_sprites_list.add(ball)

# The loop will carry on until the user exits the game (e.g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
#ball = ball(ball_speed, 200, 200)


while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: #Pressing the x Key will quit the game
                     carryOn=False
        if event.type == pygame.K_SPACE:
            ball.alive = True

    #Moving the paddle when the use uses the arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(5)

    # --- Game logic should go here
    all_sprites_list.update()
    if ball.alive:
        ball.advance()

    #bounce off walls
    if ball.center_x < 10 and ball.velocity_dx < 0:
        ball.bounce_horizontal()
    if ball.center_x > WIDTH - 10 and ball.velocity_dx > 0:
        ball.bounce_horizontal()
    if ball.center_y < 48 and ball.velocity_dy < 0:
        ball.bounce_vertical()

    #respawn if the ball hits the bottom
    if ball.center_y > HEIGHT and ball.velocity_dy > 0:
        if lives > 0:
            lives -= 1
            ball.center_x = paddle.rect.x + 50
            ball.center_y = paddle.rect.y - 13
            ball.velocity_dx = 0
            ball.velocity_dy = 0
            ball.alive = False