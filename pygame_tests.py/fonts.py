import pygame

pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))

# Load a system font
font = pygame.font.SysFont('Arial', 30, bold=True)

# Render some text
text_surface = font.render('Hello, Pygame!', True, "white")

# Blit the text surface onto the screen
screen.blit(text_surface, (100, 100))

# Update the display
pygame.display.flip()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()