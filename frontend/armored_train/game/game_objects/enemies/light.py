import pygame


class LightEnemyObject:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.__screen = screen
        self.__surface = pygame.Surface((20, 30), pygame.SRCALPHA)
        self.health = 50
        self.damage = 15
        self.speed = 30
        self.zone = 1

    def draw(self):
        rect = pygame.Rect(self.x, self.y, 20, 30)
        self.__surface.fill((130, 130, 130, 200))
        self.__screen.blit(self.__surface, rect)