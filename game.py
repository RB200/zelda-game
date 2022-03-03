import pygame
from pygame.locals import *
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH = 1920
HEIGHT = 1080

temp = True
running2 = True

with open('./storage/character_state.txt','r') as f:
    character_state = f.read()

status = 1
velocity = 135
velocity2 = 240
#fps = 100
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("New Game")

running = True 
player_x = 0
player_y = 0

active_screen = 56

player_sprite = pygame.image.load(f'./character assets/face {character_state}.png')
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
            if active_screen != 56:
                active_background = pygame.image.load(f'./backgrounds/{active_screen}.png')
            else:
                active_background = pygame.image.load('./main_bg.png')
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == ord('a'):
                char_state_to_write = character_state + 1
                with open('./storage/character_state.txt','w') as f:
                    f.write(str(char_state_to_write))
                player_sprite = pygame.image.load(f'./character assets/face {character_state}.png')


                random_number = random.randint(1,3)
                if random_number == 1:
                    active_background = pygame.image.load(f'./backgrounds/36.png')
                elif random_number == 2:
                    active_background = pygame.image.load('./backgrounds/46.png')
                else:
                    active_background = pygame.image.load('./backgrounds/66.png')

            if event.key == ord('d'):
                random_number = random.randint(1,3)
                if random_number == 1:
                    active_background = pygame.image.load(f'./backgrounds/36.png')
                elif random_number == 2:
                    active_background = pygame.image.load('./backgrounds/46.png')
                else:
                    active_background = pygame.image.load('./backgrounds/66.png')

            if event.key == ord('w'):
                random_number = random.randint(1,3)
                if random_number == 1:
                    active_background = pygame.image.load(f'./backgrounds/36.png')
                elif random_number == 2:
                    active_background = pygame.image.load('./backgrounds/46.png')
                else:
                    active_background = pygame.image.load('./backgrounds/66.png')
            if event.key == ord('s'):
                random_number = random.randint(1,3)
                if random_number == 1:
                    active_background = pygame.image.load(f'./backgrounds/36.png')
                elif random_number == 2:
                    active_background = pygame.image.load('./backgrounds/46.png')
                else:
                    active_background = pygame.image.load('./backgrounds/66.png')


    screen.blit(active_background,(0,0))
    screen.blit(player_sprite,(player_x, player_y)) 

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == ord('a'):
                random_number = random.randint(1,3)
                if random_number == 1:
                    active_background = pygame.image.load(f'./backgrounds/36.png')
                elif random_number == 2:
                    active_background = pygame.image.load('./backgrounds/46.png')
                else:
                    active_background = pygame.image.load('./backgrounds/66.png')
                player_x -= velocity2
            if event.key == ord('d'):
                random_number = random.randint(1,3)
                if random_number == 1:
                    active_background = pygame.image.load(f'./backgrounds/36.png')
                elif random_number == 2:
                    active_background = pygame.image.load('./backgrounds/46.png')
                else:
                    active_background = pygame.image.load('./backgrounds/66.png')
                player_x += velocity2
            if event.key == ord('w'):
                random_number = random.randint(1,3)
                if random_number == 1:
                    active_background = pygame.image.load(f'./backgrounds/36.png')
                elif random_number == 2:
                    active_background = pygame.image.load('./backgrounds/46.png')
                else:
                    active_background = pygame.image.load('./backgrounds/66.png')
                player_y -= velocity
            if event.key == ord('s'):
                random_number = random.randint(1,3)
                if random_number == 1:
                    active_background = pygame.image.load(f'./backgrounds/36.png')
                elif random_number == 2:
                    active_background = pygame.image.load('./backgrounds/46.png')
                else:
                    active_background = pygame.image.load('./backgrounds/66.png')
                player_y += velocity
            if event.type == QUIT:
                running = False
            

            


    pygame.display.update()


pygame.quit()

