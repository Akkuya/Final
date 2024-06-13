import pygame
import globals

pygame.init()
font = pygame.font.Font("./assets/fonts/Inter.ttf", 15)
title_font = pygame.font.Font("./assets/fonts/Inter.ttf", 50)


backbtn = pygame.image.load('./assets/img/backbtn.png')
backbtn = pygame.transform.rotozoom(backbtn, 0, 0.05)
back_rect = backbtn.get_rect(topleft = (5, 5))


def keycheck():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if 338<= mouse_x <= 463 and 220 <= mouse_y <= 281:
                print('1 pressed')
                globals.DIFFICULTY = 0
                
            elif 338 <= mouse_x <= 463 and 320 <= mouse_y <= 381:
                

                globals.DIFFICULTY = 1

            elif 338 <= mouse_x <= 463 and 420 <= mouse_y <= 481:
                print('3 pressed')

                globals.DIFFICULTY = 2
                
            elif back_rect.collidepoint((mouse_x, mouse_y)):
                globals.GAME_STATUS = "MENU"
            


def run(window, clock):
    window.fill((217, 217, 217))

    text_title = title_font.render("DIFFICULTY", True, (0,0,0))
    text_title_rect = text_title.get_rect(center=(globals.WINDOW_WIDTH // 2, 50))
    window.blit(text_title, text_title_rect)

    text_play = title_font.render("EASY", True, (138, 251, 149))
    text_play_rect = text_play.get_rect(center=(globals.WINDOW_WIDTH // 2, 250))
    if globals.DIFFICULTY == 0:
        x = (51, 45, 45)
    else:
        x = (146, 146, 146)
        
    bg_rect= pygame.draw.rect(window, x, text_play_rect)
    
    window.blit(text_play, text_play_rect)

    text_play = title_font.render("MEDIUM", True, (138, 170, 251))
    text_play_rect = text_play.get_rect(center=(globals.WINDOW_WIDTH // 2, 350))
    if globals.DIFFICULTY == 1:
        x = (51, 45, 45)
    else:
        x = (146, 146, 146)
    bg_rect= pygame.draw.rect(window,x, text_play_rect)

    window.blit(text_play, text_play_rect)


    text_play = title_font.render("HARD", True, (251, 138, 138))
    text_play_rect = text_play.get_rect(center=(globals.WINDOW_WIDTH // 2, 450))
    if globals.DIFFICULTY == 2:
        x = (51, 45, 45)
    else:
        x = (146, 146, 146)
    bg_rect= pygame.draw.rect(window, x, text_play_rect)
    window.blit(text_play, text_play_rect)


    window.blit(backbtn, back_rect)
    keycheck()
    pygame.display.flip()
    clock.tick(60)