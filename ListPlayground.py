import random
import string
import pygame
import sys

from ListButtons import ListButtons
from constants import BG_COLOR, ITEM_START_X, ITEM_START_Y, ITERM_HEIGHT, ITERM_SPACING, ITERM_WIDTH, ITERMS_PER_ROW, SCREEN_HEIGHT, SCREEN_WIDTH

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Python List Visualization Game")

current_list = [random.choice(string.ascii_uppercase) for _ in range(5)]
old_list_1 = []
old_list_2 = []

list_buttons = ListButtons(current_list)

def draw_list(screen, list_object, start_x, start_y, box_color):
    for i, item in enumerate(list_object):
        row = i // ITERMS_PER_ROW
        col = i % ITERMS_PER_ROW

        x = start_x + col * (ITERM_WIDTH + ITERM_SPACING)
        y = start_y + row * (ITERM_HEIGHT + ITERM_SPACING)

        pygame.draw.rect(screen, box_color, (x, y, ITERM_WIDTH, ITERM_HEIGHT))
        font = pygame.font.SysFont('Arial', 20)
        text_surf = font.render(str(item), True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=(x + ITERM_WIDTH / 2, y + ITERM_HEIGHT / 2))
        screen.blit(text_surf, text_rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            old_list_2 = old_list_1.copy()
            old_list_1 = current_list.copy()
            list_buttons.on_click()
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)

    list_buttons.draw_buttons(screen)
    list_buttons.draw_output(screen)

    draw_list(screen, current_list, ITEM_START_X, ITEM_START_Y, (0, 100, 200))
    draw_list(screen, old_list_1, ITEM_START_X, ITEM_START_Y + ITERM_HEIGHT * 3, (50, 150, 250) )

    pygame.display.flip()

pygame.quit()
sys.exit()
