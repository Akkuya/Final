import pygame

import globals

import credits
import game
import lose
import menu
import options

pygame.init()
screen = pygame.display.set_mode((globals.WINDOW_WIDTH,globals.WINDOW_HEIGHT))

clock = pygame.time.Clock()


while True:
    
    if globals.GAME_STATUS == "MENU":
        menu.run(screen, clock)
    elif globals.GAME_STATUS == "OPTIONS":
        options.run(screen, clock)
    elif globals.GAME_STATUS == "CREDITS":
        credits.run(screen, clock) 
    elif globals.GAME_STATUS == "GAME":
        game.run(screen, clock)
    elif globals.GAME_STATUS == "LOSE":
        lose.run(screen, clock)
