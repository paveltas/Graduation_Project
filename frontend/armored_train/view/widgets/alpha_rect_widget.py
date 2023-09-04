import pygame

from frontend.armored_train.view.widgets.widget import Widget


class AlphaRectWidget(Widget):
    def __init__(self, x, y, width, height, screen, alpha=128):
        super().__init__(x, y, width, height, screen)
        self.__surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.__alpha = alpha

    def draw(self):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.__surface.fill((130, 130, 130, self.__alpha))
        self.screen.blit(self.__surface, rect)




