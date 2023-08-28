import pygame


class WagonObject:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.__screen = screen
        self.__surface = pygame.Surface((50, 90), pygame.SRCALPHA)
        self.armor = 50
        self.health = 150
        self.slots_on_the_left = 2
        self.slots_on_the_right = 2
        self.slots_on_the_top = 2

    def draw(self):
        rect = pygame.Rect(self.x, self.y, 50, 90)
        self.__surface.fill((130, 130, 130, 200))
        self.__screen.blit(self.__surface, rect)
