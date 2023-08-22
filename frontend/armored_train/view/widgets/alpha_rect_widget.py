import pygame

from frontend.armored_train.view.widgets.widget import Widget


class AlphaRectWidget(Widget):
    def __init__(self, x, y, width, height, screen, asset_manager, alpha=128):
        super().__init__(x, y, width, height, screen, asset_manager)
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.alpha = alpha

    def draw(self):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.surface.fill((130, 130, 130, self.alpha))
        self.screen.blit(self.surface, rect)




