import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Clickable Buttons")

font = pygame.font.Font(None, 36)

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.action = action
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
                self.action()

def button_action_1():
    print("Button 1 clicked!")

def button_action_2():
    print("Button 2 clicked!")

button1 = Button(100, 100, 200, 50, "Button 1", (200, 200, 200), (255, 255, 255), button_action_1)
button2 = Button(100, 200, 200, 50, "Button 2", (200, 200, 200), (255, 255, 255), button_action_2)

buttons = [button1, button2]

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