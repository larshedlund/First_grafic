#IMPORTS

import pygame, sys, func
from pygame.locals import * 
from func import *
#sys.path.append('/d/Projekt/python/First_grafc')
 

pygame.init()
#INTIALISATION
FPS = 30 # frames per second setting
FPSCLOCK = pygame.time.Clock()
DISPLAY_SIZE = width, height = 640, 640
DISPLAY = pygame.display.set_mode(DISPLAY_SIZE,0,32)
DISPLAY_SEGMENT_SIZE = 64
DISPLAY_SEGMENT = DISPLAY_SIZE[0]/DISPLAY_SEGMENT_SIZE, DISPLAY_SIZE[1]/DISPLAY_SEGMENT_SIZE
pygame.display.set_caption('PRICK the game')

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
textSurfaceObj = fontObj.render('Everybody like to be Mr Prick', True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (300, 50)

# CONTROLL
direction = 'non'
prick_img = img_right
prick_pos = [1,1]
			
# main game loop
while True: # the main game loop
 
    if direction != 'non':
        update_prick_position(direction, prick_pos,DISPLAY_SEGMENT)
        direction = 'non'
		
    for event in pygame.event.get():
        if not hasattr(event, 'key'): continue
        down = event.type == KEYDOWN 
        if event.key == K_RIGHT or event.key ==  K_d: 
            direction = 'right'
            PRICK_IMG = img_right
        elif event.key == K_LEFT or event.key ==  K_a: 
            direction = 'left'
            PRICK_IMG = img_left
        elif event.key == K_UP or event.key ==  K_w: 
            direction = 'up' 
            PRICK_IMG = img_up
        elif event.key == K_DOWN or event.key ==  K_s: 
            direction = 'down'
            PRICK_IMG = img_down
        elif event.key == QUIT: 
            pygame.quit()
            sys.exit()
        elif event.key == K_ESCAPE:
            sys.exit(0) # quit the game

    DISPLAY.fill(BLUE)
    DISPLAY.blit(textSurfaceObj, textRectObj)
    DISPLAY.blit(prick_img, (prick_dis_pos(prick_pos[0],DISPLAY_SEGMENT_SIZE),prick_dis_pos(prick_pos[1],DISPLAY_SEGMENT_SIZE)))
    
    pygame.display.update() 
    FPSCLOCK.tick(FPS)

