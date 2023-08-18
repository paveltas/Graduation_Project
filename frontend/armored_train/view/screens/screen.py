from abc import ABC, abstractmethod

import pygame


class Screen(ABC):
    def __init__(self, width: int, height: int, caption: str, asset_manager):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(caption)
        self.asset_manager = asset_manager

    @abstractmethod
    def draw(self):
        pass
