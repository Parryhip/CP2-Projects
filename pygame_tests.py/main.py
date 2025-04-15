import pygame

pygame.init()

num = 0

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Clickable Buttons")

font = pygame.font.Font(None, 36)

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, num):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.num = num
        self.hover_color = hover_color
        self.is_hovered = False

    def draw(self, surface):
        current_color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(surface, current_color, self.rect)
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_hovered:
                self.num += 1
                print(self.num)

button1 = Button(0, 0, 800, 600, "Click here!", "red", (255, 255, 255), num)

buttons = [button1]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for button in buttons:
            button.handle_event(event)

    screen.fill((255, 255, 255))
    for button in buttons:
        button.draw(screen)
    pygame.display.update()

pygame.quit()