import random
import string
import pygame
from Button import Button
from constants import BUTTON_COLOR, BUTTON_HEIGHT, BUTTON_HIGHLIGHT_COLOR, BUTTON_SPACING, BUTTON_START_X, BUTTON_START_Y, BUTTON_TEXT_COLOR, BUTTON_WIDTH, ITERMS_PER_ROW

MAX_ITEM = ITERMS_PER_ROW * 2

def get_random_value():
    return random.choice(string.ascii_uppercase)

def get_random_index(list_object):
    return random.randint(0, len(list_object) - 1)

def append_action(list_object):
    if len(list_object) >= MAX_ITEM:
        return f"Maximum {MAX_ITEM} allowed."
    
    random_value = get_random_value()

    list_object.append(random_value)
    return f"append({random_value})"

def insert_action(list_object):
    if len(list_object) >= MAX_ITEM:
        return f"Maximum {MAX_ITEM} allowed."

    random_index = get_random_index(list_object)
    random_value = get_random_value()

    list_object.insert(random_index, random_value)
    return f"insert({random_index}, {random_value})"

def extend_action(list_object):
    if len(list_object) >= MAX_ITEM:
        return f"Maximum {MAX_ITEM} allowed."

    random_range = min(random.randint(2, 5), MAX_ITEM - len(list_object))
    new_list = [get_random_value() for _ in range(random_range)]

    list_object.extend(new_list)
    return f"extend({new_list})"

def pop_action(list_object):
    if len(list_object) == 0:
        return f"Nothing to pop."
 
    value = list_object.pop()
    return f"pop() -> {value}"
 
def remove_action(list_object):
    if len(list_object) == 0:
        return f"Nothing to remove."

    random_index = get_random_index(list_object)
    value = list_object[random_index]

    list_object.remove(value)
    return f"remove({value})"

def clear_action(list_object):
    list_object.clear()
    return "clear()"

def sort_action(list_object):
    list_object.sort()
    return "sort()"

def index_action(list_object):
    random_index = get_random_index(list_object)
    value = list_object[random_index]

    index_value = list_object.index(value)
    return f"index({value}) -> {index_value}"

def count_action(list_object):
    random_index = get_random_index(list_object)
    value = list_object[random_index]

    count_value = list_object.count(value)
    return f"count({value}) -> {count_value}"

def reverse_action(list_object):
    list_object.reverse()
    return "reverse()"

class ListButtons():
    def __init__(self, list_object):
        self.list_object = list_object
        self.output = ""
        self.buttons = []

        button_details = [
            ("Append", append_action),
            ("Insert", insert_action),
            ("Extend", extend_action),
            ("Pop", pop_action),
            ("Remove", remove_action),
            ("Clear", clear_action),
            ("Sort", sort_action),
            ("Index", index_action),
            ("Count", count_action),
            ("Reverse", reverse_action),
        ]

        for index, (text, action) in enumerate(button_details):
            x_position = BUTTON_START_X + index % 10 * (BUTTON_WIDTH + BUTTON_SPACING)
            y_position = BUTTON_START_Y + index // 10 * (BUTTON_HEIGHT + BUTTON_SPACING)
            button = Button(text, action, x_position, y_position, BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_COLOR, BUTTON_TEXT_COLOR)
            self.buttons.append(button)

    def draw_buttons(self, screen):
        mouse_pos = pygame.mouse.get_pos()

        for button in self.buttons:
            if button.is_over(mouse_pos):
                button.draw(screen, BUTTON_HIGHLIGHT_COLOR)
            else:
                button.draw(screen)

    def on_click(self):
        mouse_pos = pygame.mouse.get_pos()

        for button in self.buttons:
            if button.is_over(mouse_pos):
                self.output = button.action(self.list_object)

    def draw_output(self, screen):
        rect = (BUTTON_START_X,
                BUTTON_START_Y + BUTTON_HEIGHT + BUTTON_SPACING,
                BUTTON_WIDTH * 10 + BUTTON_SPACING * 9,
                BUTTON_HEIGHT)
        pygame.draw.rect(screen, (0, 0, 0), rect)
        font = pygame.font.SysFont('Arial', 18)
        text_surf = font.render(self.output, True, (255, 255, 255))
        text_rect = (rect[0] + 2, rect[1] + 2, rect[2] - 4, rect[3] - 4)
        screen.blit(text_surf, text_rect)
