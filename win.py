import pygame
import globals

pygame.init()

font = pygame.font.Font("./assets/fonts/Inter.ttf", 60)
title_font = pygame.font.Font("./assets/fonts/Inter.ttf", 80)


text_play = title_font.render("MAIN MENU", True, (60, 61, 63))
text_play_rect = text_play.get_rect(center=(globals.WINDOW_WIDTH // 2, 400))


def keycheck():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            

            if text_play_rect.collidepoint((mouse_x, mouse_y)):
                globals.GAME_STATUS = "MENU"

            
            


def run(window, clock):
    window.fill((217, 217, 217))

    text_title = title_font.render("YOU WIN!", True, (62, 186, 74))
    text_title_rect = text_title.get_rect(center=(globals.WINDOW_WIDTH // 2, 50))
    window.blit(text_title, text_title_rect)

    text_title = font.render(f"Score: {globals.score}", True, (0,0,0))
    text_title_rect = text_title.get_rect(center=(globals.WINDOW_WIDTH // 2, 220))
    window.blit(text_title, text_title_rect)

    bg_rect= pygame.draw.rect(window, (146, 146, 146), text_play_rect)
    
    
    window.blit(text_play, text_play_rect)

    
    keycheck()
    pygame.display.flip()
    clock.tick(60)