import re
import pygame
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH = 1920
HEIGHT = 1080

temp = True
running2 = True

down_mult = 5
left_mult = 4
up_mult = 3
right_mult = 2



status = 1
velocity = 135
velocity2 = 240
#fps = 100
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Genshin Wishing Simulator")

player_sprite = pygame.image.load('./Untitled.png')
running = True 
player_x = 0
player_y = 0

active_screen = 56

active_background = pygame.image.load('./main_bg.png')
while running:


    if player_y < 0:
        active_screen = active_screen - 10
        player_y = 1080-128
        if active_screen != 56:
            active_background = pygame.image.load(f'./backgrounds/{active_screen}.png')
        else:
            active_background = pygame.image.load('./main_bg.png')
    elif player_y >= 1080:
        active_screen = active_screen + 10
        player_y = 0
        if active_screen != 56:
            active_background = pygame.image.load(f'./backgrounds/{active_screen}.png')
        else:
            active_background = pygame.image.load('./main_bg.png')
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
    


    screen.blit(active_background,(0,0))
    screen.blit(player_sprite,(player_x, player_y))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == ord('a'):
                player_x -= velocity2
            if event.key == ord('d'):
                player_x += velocity2
            if event.key == ord('w'):
                player_y -= velocity
            if event.key == ord('s'):
                player_y += velocity


    pygame.display.update()


pygame.quit()


