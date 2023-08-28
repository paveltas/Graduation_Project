import pygame


class LocomotiveObject:
    def __init__(self, screen):
        self.__screen = screen
        self.__surface = pygame.Surface((50, 90), pygame.SRCALPHA)
        self.armor = 150
        self.health = 200
        self.slots_on_the_left = 3
        self.slots_on_the_right = 3
        self.slots_on_the_top = 3

    def draw(self):
        rect = pygame.Rect(935, 100, 50, 90)
        self.__surface.fill((130, 130, 130, 200))
        self.__screen.blit(self.__surface, rect)
