import pygame
from pygame.locals import *
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
 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout")

