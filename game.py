import pygame
import globals

pygame.init()
font = pygame.font.Font("Inter.ttf", 15)
title_font = pygame.font.Font("Inter.ttf", 50)
body = pygame.font.Font("Inter.ttf", 65)



backbtn = pygame.image.load('./backbtn.png')
one = pygame.image.load('./one.png')
onebtn = pygame.transform.rotozoom(one, 0, 0.2)

backbtn = pygame.transform.rotozoom(backbtn, 0, 0.05)
back_rect = backbtn.get_rect(topleft = (5, 5))

def keycheck():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if back_rect.collidepoint((mouse_x, mouse_y)):
                globals.GAME_STATUS = "MENU"

            elif 200 <= mouse_x <= 400 and 100 <= mouse_y <= 300:
                globals.GAME_STATUS = "LOSE"

            elif 410 <= mouse_x <= 610 and 100 <= mouse_y <= 300:
                globals.grid[0][1][0] = True
            elif 200 <= mouse_x <= 400 and 310 <= mouse_y <= 510:
                globals.grid[1][0][0] = True

            elif 410 <= mouse_x <= 610 and 310 <= mouse_y <= 510:
                globals.grid[1][1][0] = True

    
def init():
    globals.grid = [
        [[False, -1], [False, 1]],
        [[False, 1], [False, 1]]

        ]
        

def run(window, clock):
    window.fill((217, 217, 217))

    for row in range(len(globals.grid)):
        for j in range(len(globals.grid[row])):
            if globals.grid[row][j][0] == False:
                color = (238, 130, 130)
            else:
                color = (209, 250, 195)
            
            pygame.draw.rect(window, color, (200 + (j*200) + (j*20), 100 + (row*200) + (row*10), 200, 200))

            if globals.grid[row][j][0] == True:
                one_rect = onebtn.get_rect(topleft= (200 + (j*200) + (j*20), 100 + (row*200) + (row*10)))
                window.blit(onebtn, one_rect)
    window.blit(backbtn, back_rect)
    text_title = title_font.render(globals.DIFFICULTY, True, (0,0,0))
    text_title_rect = text_title.get_rect(center=(globals.WINDOW_WIDTH // 2, 50))
    window.blit(text_title, text_title_rect)
    keycheck()
    pygame.display.flip()
    clock.tick(60)