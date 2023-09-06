from abc import ABC, abstractmethod

import pygame


class Screen(ABC):
    def __init__(self, width: int, height: int, caption: str, asset_manager):
        pygame.init()
        self.__width = width
        self.__height = height
        self.screen = pygame.display.set_mode((self.__width, self.__height))
        pygame.display.set_caption(caption)
        self.asset_manager = asset_manager

    @abstractmethod
    def draw(self):
        pass
