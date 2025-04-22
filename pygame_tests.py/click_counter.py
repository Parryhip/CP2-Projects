import pygame

pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Click Counter")

# Initialize font
font = pygame.font.Font(None, 36)

# Initialize click counter
click_count = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_count += 1

    # Clear the screen
    screen.fill((0, 0, 0))  # Black background

    # Render the click counter
    text_surface = font.render("Clicks: " + str(click_count), True, (255, 255, 255))  # White text
    text_rect = text_surface.get_rect(topleft=(10, 10))  # Position at top-left corner
    screen.blit(text_surface, text_rect)

    # Update the display
    pygame.display.flip()

pygame.quit()