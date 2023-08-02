from abc import ABC, abstractmethod

import pygame


class Widget(ABC):

    def __init__(self, x, y, width, height, screen, color=(0, 0, 0), border_width=2,
                 text_font=(None, 36), font_color=(250, 250, 250)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.color = color
        self.border_width = border_width
        self.text_font = pygame.font.Font(*text_font)
        self.font_color = font_color

    def get_size(self):
        return self.width, self.height

    @abstractmethod
    def draw(self):
        pass

    def handle_event(self):
        pass
