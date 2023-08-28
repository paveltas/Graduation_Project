import pygame


class MediumEnemyObject:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.__screen = screen
        self.__surface = pygame.Surface((30, 50), pygame.SRCALPHA)
        self.health = 200
        self.damage = 70
        self.speed = 10
        self.zone = 2

    def draw(self):
        rect = pygame.Rect(self.x, self.y, 50, 50)
        self.__surface.fill((130, 130, 130, 200))
        self.__screen.blit(self.__surface, rect)
