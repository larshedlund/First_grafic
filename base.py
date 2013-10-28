import pygame, sys
from pygame.locals import * 

pygame.init()
size = width, height = 640, 400
DISPLAYSURF = pygame.display.set_mode(size,0,32)

pygame.display.set_caption('First Grafic')
# ball = pygame.image.load(ball.gif)

BLACK = ( 0, 0, 0) 
WHITE = (255, 255, 255) 
RED = (255, 0, 0) 
GREEN = ( 0, 255, 0) 
BLUE = ( 0, 0, 255)

spamRect = pygame.Rect(10, 20, 40, 70)

DISPLAYSURF.fill(WHITE) 
pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277), 
(56, 277), (0, 106)))

# main game loop
while True: 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update() 

