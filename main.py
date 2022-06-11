import pygame
from pygame.locals import *
from src.Game import Game

SCREEN_WIDTH = 360
SCREEN_HEIGHT = 480

pygame.init()

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()
GAME_STATE = True

game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN)

while GAME_STATE:
    SCREEN.fill((0,0,50))

    game.on_draw()
    game.on_update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_STATE = False
        else:
            game.event_control(event)

    pygame.display.update()
    CLOCK.tick(60)

pygame.quit()

        
