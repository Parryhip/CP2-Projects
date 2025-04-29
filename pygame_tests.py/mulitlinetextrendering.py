import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
font = pygame.font.Font(None, 30)
text_color = (255, 255, 255)
background_color = (0, 0, 0)

def render_multiline_text(surface, text, font, color, position):
    lines = text.splitlines()
    y_offset = 0
    for line in lines:
        text_surface = font.render(line, True, color, background_color)
        text_rect = text_surface.get_rect(topleft=(position[0], position[1] + y_offset))
        surface.blit(text_surface, text_rect)
        y_offset += font.get_linesize()
        
text_to_render = "This is the first line.\nThis is the second line.\nAnd this is the third line."
text_position = (50, 50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(background_color)
    render_multiline_text(screen, text_to_render, font, text_color, text_position)
    pygame.display.flip()
    
pygame.quit()