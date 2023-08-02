from abc import ABC, abstractmethod

import pygame


class Screen(ABC):
    pygame.init()

    def __init__(self, width: int, height: int, caption: str):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(caption)

    @abstractmethod
    def draw(self):
        pass
