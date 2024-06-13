import pygame
import globals

pygame.init()
font = pygame.font.Font("./assets/fonts/Inter.ttf", 15)
title_font = pygame.font.Font("./assets/fonts/Inter.ttf", 50)
body = pygame.font.Font("./assets/fonts/Inter.ttf", 65)


backbtn = pygame.image.load('./assets/img/backbtn.png')
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
            
            
        


def run(window, clock):
    window.fill((217, 217, 217))

    text_title = title_font.render("CREDITS", True, (0,0,0))
    text_title_rect = text_title.get_rect(center=(globals.WINDOW_WIDTH // 2, 50))
    window.blit(text_title, text_title_rect)

    text_DEV = body.render("Lead Developer: Rishi", True, (0, 0, 0))
    text_DEV_rect = text_DEV.get_rect(center=(globals.WINDOW_WIDTH // 2, 200))
    window.blit(text_DEV, text_DEV_rect)
    
    text_design = body.render("Designer: Taqeef", True, (0, 0, 0))
    text_design_rect = text_design.get_rect(center=(globals.WINDOW_WIDTH // 2, 320))
    window.blit(text_design, text_design_rect)

    text_graphics = body.render("Graphics: Taqeef", True, (0, 0, 0))
    text_graphics_rect = text_graphics.get_rect(center=(globals.WINDOW_WIDTH // 2, 440))
    window.blit(text_graphics, text_graphics_rect)
    
    text_sfx = body.render("SFX: Ayman", True, (0, 0, 0))
    text_sfx_rect = text_sfx.get_rect(center=(globals.WINDOW_WIDTH // 2, 560))
    window.blit(text_sfx, text_sfx_rect)
    

    window.blit(backbtn, back_rect)

    keycheck()
    pygame.display.flip()
    clock.tick(60)