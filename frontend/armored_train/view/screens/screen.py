from abc import ABC, abstractmethod

import pygame


# class SuperPrivateDescriptor:
#     def __set_name__(self, owner, name):
#         self.name = '__' + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         setattr(instance, self.name, value)


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
