#IMPORTS
import pygame, sys
from pygame.locals import * 

pygame.init()
#INTIALISATION
FPS = 30 # frames per second setting
FPSCLOCK = pygame.time.Clock()
DISPLAY_SIZE = width, height = 1024, 768
DISPLAY = pygame.display.set_mode(DISPLAY_SIZE,0,32)
pygame.display.set_caption('First Grafic')

#COLORS
BLACK = ( 0, 0, 0) 
WHITE = (255, 255, 255) 
RED = (255, 0, 0) 
GREEN = ( 0, 255, 0) 
BLUE = ( 0, 0, 255)

#IMAGE LOAD
img_right = pygame.image.load("prick_right.png")
img_left = pygame.image.load("prick_left.png")
img_down = pygame.image.load("prick_falling.png")
img_up = pygame.image.load("prick_flying.png")


#TEXT
fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('DAMN! Boj ar jo kool or nott', True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (300, 300)

# CONTROLL
direction = 'right'
prick_img = img_right
prick_position_x = 50
prick_position_y = 50

# main game loop
while True: # the main game loop
    
    
    if direction == 'right':
        prick_position_x += 5
        if prick_position_x >= 1044:
             prick_position_x = -30
            
    elif direction == 'down':
        prick_position_y += 5
        if prick_position_y >= 818:
             prick_position_y = 5
			 
    elif direction == 'left':
        prick_position_x -= 5
        if prick_position_x <= -40:
            prick_position_x = 1024
			
    elif direction == 'up':
        prick_position_y -= 5
        if prick_position_y <= -50:
            prick_position_y = 758

   
    for event in pygame.event.get():
        if not hasattr(event, 'key'): continue
        down = event.type == KEYDOWN 
        if event.key == K_RIGHT: 
            direction = 'right'
            prick_img = img_right
        elif event.key == K_LEFT: 
            direction = 'left'
            prick_img = img_left
        elif event.key == K_UP: 
            direction = 'up' 
            prick_img = img_up
        elif event.key == K_DOWN: 
            direction = 'down'
            prick_img = img_down
        elif event.key == QUIT: 
            sys.exit()
            pygame.quit()
        elif event.key == K_ESCAPE: sys.exit(0) # quit the game

    DISPLAY.fill(BLUE)
    DISPLAY.blit(textSurfaceObj, textRectObj)
    DISPLAY.blit(prick_img, (prick_position_x, prick_position_y))
    
    pygame.display.update() 
    FPSCLOCK.tick(FPS)
