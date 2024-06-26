# TODO
# - ORGANIZE CODE
# - MAKE WIN SCREEN
# - DISPLAY SCORES ON RESUTLS SCREENS
# - WRITE HIGH SCORES TO FILE?
# - DFS IF USER CLICKS A TILE WITH A 0 ON IT


##################### EXTERNAL MODULES ####################
import pygame
from math import floor
import random

#####################   OTHER FILES    ####################
import globals as g

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 1000) # Define a tick every second


######################      FONTS      #####################
title_font = pygame.font.Font("./assets/fonts/Inter.ttf", 40)
small_font = pygame.font.Font("./assets/fonts/Inter.ttf", 30)


visited = []

######################      IMAGES      #####################

# Placeable Flag
flag_img = pygame.image.load('./assets/img/flag.png')
flag_img = pygame.transform.rotozoom(flag_img, 0, 0.1)
# Flag Icon
flag_icon = pygame.transform.rotozoom(flag_img, 0, 1.5)
flag_rect = flag_icon.get_rect(center=(200, 550))
# Timer Icon
timer_img = pygame.image.load('./assets/img/timer.png')
timer_img = pygame.transform.rotozoom(timer_img, 0, 0.15)
timer_rect = timer_img.get_rect(center=(450, 550))
# Back Button
backbtn = pygame.image.load('./assets/img/backbtn.png')
backbtn = pygame.transform.rotozoom(backbtn, 0, 0.05)
back_rect = backbtn.get_rect(topleft = (5, 5))

# Title Text
text_title = title_font.render(g.DIFF_NAME[g.DIFFICULTY], True, g.DIFF_COLOUR[g.DIFFICULTY])
text_title_rect = text_title.get_rect(center=(g.WINDOW_WIDTH // 2, 50))

######################      VARIABLES      #######################
curr_time = g.DIFF_TIMER[g.DIFFICULTY]
godmode = False
playable_area = pygame.Rect((50, 100, 700, 400))

def keycheck():
    global curr_time, godmode
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            curr_time -= 1

        if event.type == pygame.QUIT:
            pygame.quit()


        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if back_rect.collidepoint(mouse_pos):
                g.GAME_STATUS = "MENU"
            
            elif playable_area.collidepoint(mouse_pos):
                item = floor((mouse_pos[0] - 55)/50)
                row = floor((mouse_pos[1] - 105)/50)
                check_clicked(item, row)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            mouse_pos = pygame.mouse.get_pos()

            if playable_area.collidepoint(mouse_pos):
                item = floor((mouse_pos[0] - 55)/50)
                row = floor((mouse_pos[1] - 105)/50)
                flag(item, row)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_g:
            print('working')
            if godmode == True:
                godmode = False
            else:
                godmode = True
            

    
def init():
    global text_title, curr_time, godmode
    curr_time = g.DIFF_TIMER[g.DIFFICULTY]
    godmode = False
    g.flagcount = 0
    g.score = 0
    text_title = title_font.render(g.DIFF_NAME[g.DIFFICULTY], True, g.DIFF_COLOUR[g.DIFFICULTY])
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
    g.flags = count
    # I was on adderall when I wrote this i will figure out how it works later

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
    


def flag(row, column):
    if g.grid[column][row][0] or g.flagcount >= g.flags:
        return
    isflag = g.grid[column][row][2]
    if not isflag:
      g.grid[column][row][2] = True # Sets the flagged property of the item to True
      g.flagcount+=1
    else:
      g.grid[column][row][2] = False # Sets the flagged property of the item to True
      g.flagcount-=1
    
        
def draw(window):
   global text_title, curr_time, godmode
   window.fill((217, 217, 217))
   for row in range(len(g.grid)):
       for item in range(len(g.grid[row])):
           if g.grid[row][item][0] == False:
                color = (238, 130, 130)
           else:
                color = (209, 250, 195)
               
                
           pygame.draw.rect(window, color, (55 + (item*(g.width+g.spacing)), 105 + (row*(g.width+g.spacing)), g.width, g.width))
           if g.grid[row][item][0] == True and godmode == False:
            x= small_font.render(str(g.grid[row][item][1]), True, (0,0,0))
            y = x.get_rect(topleft=((67 + (item*(g.width+g.spacing)), 107 + (row*(g.width+g.spacing)))))
            window.blit(x, y)


           elif godmode == True:
            x= small_font.render(str(g.grid[row][item][1]), True, (0,0,0))
            y = x.get_rect(topleft=((67 + (item*(g.width+g.spacing)), 107 + (row*(g.width+g.spacing)))))
            window.blit(x, y)
           
           
           if g.grid[row][item][2]:
               flagrect = flag_img.get_rect(topleft=(60 + (item*(g.width+g.spacing)), 108 + (row*(g.width+g.spacing))))
               window.blit(flag_img, flagrect)
   
   c= (0,0,0)
   if curr_time <= 10: 
       c = (251, 138, 138)
   
   
   timer_text = title_font.render(str(curr_time), True, c)
   time_text_rect = timer_text.get_rect(center=(550,550))
   
   flag_text = title_font.render(str(g.flags-g.flagcount), True, (0,0,0))
   flag_text_rect = flag_text.get_rect(center=(300, 550))
   
   score = title_font.render(f"Score: {g.score}", True, (0,0,0))
   score_rect = score.get_rect(topright = (760,25))
   
   
   window.blit(text_title, text_title_rect)
   window.blit(backbtn, back_rect)
   window.blit(flag_icon, flag_rect)
   window.blit(flag_text, flag_text_rect)
   window.blit(score, score_rect)
   window.blit(timer_img, timer_rect)
   window.blit(timer_text, time_text_rect)




def writescores(x):
    f = open('highscores.txt', "r+")
    scores = f.readline().split(" ")
    print(scores)
    if scores == ['']:
        f.write(str(x))
        return
    added = False
    for i in range(len(scores)):
        if x >= int(scores[i]):
           scores.insert(i, str(x))
           added = True
           break
    if not added:
        scores.append(str(x))
    f.close()
    f = open('highscores.txt', "w")
    out = " ".join(scores)
    print(out)
    f.write(out)
    f.close()


def check_clicked(row, column):
    if not g.grid[column][row][0] and g.grid[column][row][1] != -1:
        g.score+=300

    g.grid[column][row][0] = True

    if g.grid[column][row][2] == True: 
        g.grid[column][row][2] = False


    if g.grid[column][row][1] == -1:
        g.GAME_STATUS = "LOSE"
        if g.score > 0:
            writescores(g.score)
        return 
   
def checkwin():
    for row in range(len(g.grid)):
       for item in range(len(g.grid[row])):
           if g.grid[row][item][0] != True and g.grid[row][item][1] >= 0:
               return
               
    g.score*=g.DIFF_MULTIPLIER[g.DIFFICULTY]
    writescores(g.score)
    g.GAME_STATUS = "WIN"

def run(window, clock:pygame.time.Clock):
    global curr_time
    if curr_time <= 0:
        g.GAME_STATUS = "LOSE"
    draw(window)
    checkwin()
    keycheck()
    pygame.display.flip()
    clock.tick(60)  