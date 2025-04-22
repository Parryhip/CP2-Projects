import pygame
import sys

pygame.init()
pygame.key.set_repeat(300, 30)  # Allow holding keys

display = pygame.display.set_mode([700, 600])
default_font_size = 45
usr_txt = ''
usr_inp_rect = pygame.Rect(200, 400, 320, 50)
color = pygame.Color('white')
active = True

def get_best_font(text, max_width, max_height, max_font_size=45, min_font_size=10):
    for font_size in range(max_font_size, min_font_size - 1, -1):
        font = pygame.font.Font(None, font_size)
        text_width, text_height = font.size(text)
        if text_width <= max_width and text_height <= max_height:
            return font
    return pygame.font.Font(None, min_font_size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                usr_txt = usr_txt[:-1]
            elif event.key == pygame.K_RETURN:
                print("Entered text:", usr_txt)
                usr_txt = ''
            else:
                usr_txt += event.unicode

    display.fill((0, 0, 0))  # Clear screen
    pygame.draw.rect(display, color, usr_inp_rect)

    font = get_best_font(usr_txt, usr_inp_rect.w - 10, usr_inp_rect.h - 10, max_font_size=default_font_size)
    txt_surface = font.render(usr_txt, True, "black")
    display.blit(txt_surface, (usr_inp_rect.x + 5, usr_inp_rect.y + 5))

    pygame.display.flip()
