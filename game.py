import pygame
from math import floor
import random

import globals as g

pygame.init()

font = pygame.font.Font("./assets/fonts/Inter.ttf", 15)
title_font = pygame.font.Font("./assets/fonts/Inter.ttf", 50)
body = pygame.font.Font("./assets/fonts/Inter.ttf", 65)
small_font = pygame.font.Font("./assets/fonts/Inter.ttf", 30)



backbtn = pygame.image.load('./assets/img/backbtn.png')
one = pygame.image.load('./assets/img/one.png')
onebtn = pygame.transform.rotozoom(one, 0, 0.2)
playable_area = pygame.Rect((50, 100, 700, 400))
backbtn = pygame.transform.rotozoom(backbtn, 0, 0.05)
back_rect = backbtn.get_rect(topleft = (5, 5))

def keycheck():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if back_rect.collidepoint(mouse_pos):
                g.GAME_STATUS = "MENU"
            
            elif playable_area.collidepoint(mouse_pos):
                item = floor((mouse_pos[0] - 55)/50)
                row = floor((mouse_pos[1] - 105)/50)
                check_clicked(item, row)
            

    
def init():
    count = 0
    g.grid = []
    
    for i in range(8):
        row = []
        for x in range(14):
            val = 0
            mine_chance = random.randint(1, 100)
            if mine_chance <= 18 and count < g.mines:
                val = -1
                count += 1
            item = [False, val, False]
            row.append(item)
        g.grid.append(row)
    
    for row in range(8):
        for column in range(14):
            val = 0
            if g.grid[row][column][1] == -1:
                continue
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    row_check = row-i
                    column_check = column - j
                    if column_check < 0 or column_check > 13:
                        continue
                    if row_check < 0 or row_check > 7:
                        continue
                
                    if g.grid[row_check][column_check][1] == -1:
                        val += 1
            g.grid[row][column][1] = val
    



    
        
def draw(window, clock):
   
   for row in range(len(g.grid)):
       for item in range(len(g.grid[row])):
           if g.grid[row][item][0] == False:
                color = (238, 130, 130)
           else:
                color = (209, 250, 195)
                
           pygame.draw.rect(window, color, (55 + (item*(g.width+g.spacing)), 105 + (row*(g.width+g.spacing)), g.width, g.width))
           if g.grid[row][item][0] == True:
                x= small_font.render(str(g.grid[row][item][1]), True, (0,0,0))
                y = x.get_rect(topleft=((67 + (item*(g.width+g.spacing)), 107 + (row*(g.width+g.spacing)))))
                window.blit(x, y)


def check_clicked(row, column):
    g.grid[column][row][0] = True
    if g.grid[column][row][1] == -1:
        g.GAME_STATUS = "LOSE"

    print(g.grid)

def run(window, clock:pygame.time.Clock):
    window.fill((217, 217, 217))

    
    draw(window, clock)
    
    
    
    
    
    window.blit(backbtn, back_rect)
    text_title = title_font.render(g.DIFFICULTY, True, (0,0,0))
    text_title_rect = text_title.get_rect(center=(g.WINDOW_WIDTH // 2, 50))
    window.blit(text_title, text_title_rect)
    keycheck()
    pygame.display.flip()
    
    clock.tick(60)  