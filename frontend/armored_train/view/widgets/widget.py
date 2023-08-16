from abc import ABC, abstractmethod

import pygame


class Widget(ABC):

    def __init__(self, x, y, width, height, screen, asset_manager, text=None, color=(0, 0, 0), border_width=2,
                 font_color=(250, 250, 250)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.text = text
        self.color = color
        self.border_width = border_width
        self.font_color = font_color
        self.text_font = pygame.font.Font(asset_manager.get_asset_path('fonts', 'Oswald-Light'), 36)

    @abstractmethod
    def draw(self):
        pass

    def handle_event(self):
        pass
