import pygame
import globals

pygame.init()
font = pygame.font.Font("./assets/fonts/Inter.ttf", 15)
title_font = pygame.font.Font("./assets/fonts/Inter.ttf", 50)



def keycheck():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if 338<= mouse_x <= 463 and 170 <= mouse_y <= 231:
                globals.GAME_STATUS = "GAME"
                globals.grid = [
                [[False, -1], [False, 1]],
                [[False, 1], [False, 1]]

                ]
                print("Play button clicked")
                
            elif 338 <= mouse_x <= 463 and 270 <= mouse_y <= 331:
                globals.GAME_STATUS = "OPTIONS"

            elif 338 <= mouse_x <= 463 and 370 <= mouse_y <= 431:
                globals.GAME_STATUS = "CREDITS"

            
            elif 338 <= mouse_x <= 463 and 470 <= mouse_y <= 531:
                pygame.quit()


def run(window, clock):
    window.fill((217, 217, 217))

    text_title = title_font.render("Minesweeper", True, (0,0,0))
    text_title_rect = text_title.get_rect(center=(globals.WINDOW_WIDTH // 2, 50))
    window.blit(text_title, text_title_rect)

    text_play = title_font.render("PLAY", True, (138, 251, 149))
    text_play_rect = text_play.get_rect(center=(globals.WINDOW_WIDTH // 2, 200))
    bg_rect= pygame.draw.rect(window, (146, 146, 146), text_play_rect)
    
    window.blit(text_play, text_play_rect)

    text_play = title_font.render("DIFFICULTY", True, (138, 170, 251))
    text_play_rect = text_play.get_rect(center=(globals.WINDOW_WIDTH // 2, 300))
    bg_rect= pygame.draw.rect(window, (146, 146, 146), text_play_rect)
    window.blit(text_play, text_play_rect)

    text_play = title_font.render("CREDITS", True, (60, 61, 63))
    text_play_rect = text_play.get_rect(center=(globals.WINDOW_WIDTH // 2, 400))
    bg_rect= pygame.draw.rect(window, (146, 146, 146), text_play_rect)
    window.blit(text_play, text_play_rect)

    text_play = title_font.render("EXIT", True, (251, 138, 138))
    text_play_rect = text_play.get_rect(center=(globals.WINDOW_WIDTH // 2, 500))
    bg_rect= pygame.draw.rect(window, (146, 146, 146), text_play_rect)
    window.blit(text_play, text_play_rect)

    keycheck()
    pygame.display.flip()
    clock.tick(60)