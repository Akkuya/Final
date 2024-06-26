import pygame
import game
import globals

pygame.init()
font = pygame.font.Font("./assets/fonts/Inter.ttf", 60)
title_font = pygame.font.Font("./assets/fonts/Inter.ttf", 80)

text_play = title_font.render("RESTART", True, (138, 170, 251))
text_play_rect = text_play.get_rect(center=(globals.WINDOW_WIDTH // 2, 320))

text_menu = title_font.render("MAIN MENU", True, (60, 61, 63))
text_menu_rect = text_menu.get_rect(center=(globals.WINDOW_WIDTH // 2, 450))

def keycheck():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            
                
            if text_play_rect.collidepoint((mouse_x, mouse_y)):
                game.init()
                globals.GAME_STATUS = "GAME"

            elif text_menu_rect.collidepoint((mouse_x, mouse_y)):
                globals.GAME_STATUS = "MENU"

            
            

def run(window, clock):
    window.fill((217, 217, 217))

    text_title = title_font.render("YOU LOSE!", True, (251, 138, 138))
    text_title_rect = text_title.get_rect(center=(globals.WINDOW_WIDTH // 2, 50))
    window.blit(text_title, text_title_rect)

    text_title = font.render(f"Score: {globals.score}", True, (0,0,0))
    text_title_rect = text_title.get_rect(center=(globals.WINDOW_WIDTH // 2, 180))
    window.blit(text_title, text_title_rect)

    
    bg_rect= pygame.draw.rect(window, (146, 146, 146), text_play_rect)
    window.blit(text_play, text_play_rect)

    
    bg_rect= pygame.draw.rect(window, (146, 146, 146), text_menu_rect)
    window.blit(text_menu, text_menu_rect)

    
    keycheck()
    pygame.display.flip()
    clock.tick(60)