import pygame

class Button:
    def __init__(self, text, action, x, y, width, height, color, text_color):
        self.x = x
        self.y = y
        self.text = text
        self.action = action
        self.width = width
        self.height = height
        self.color = color
        self.text_color = text_color
        self.font = pygame.font.SysFont("Arial", 20)

    def draw(self, screen, highlight_color = None):
        if highlight_color != None:
            pygame.draw.rect(screen, highlight_color, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

        text_surf = self.font.render(self.text, True, self.text_color)
        screen.blit(text_surf, (self.x + (self.width - text_surf.get_width()) / 2, self.y + (self.height - text_surf.get_height()) / 2))

    def is_over(self, pos):
        if self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height:
            return True
        return False
