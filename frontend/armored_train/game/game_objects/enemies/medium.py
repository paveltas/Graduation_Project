import pygame


class MediumEnemyObject:
    def __init__(self, x, y, screen, asset_manager):
        self.__screen = screen
        self.__asset_manager = asset_manager
        self.x = x
        self.y = y
        self.health = 100
        self.damage = 30
        self.speed = 3
        self.zone = 3

        self.__medium_enemy_png = pygame.image.load(
            self.__asset_manager.get_asset_path("images", "medium_enemy")).convert_alpha()
        self.medium_enemy_rect = self.__medium_enemy_png.get_rect(topleft=(self.x, self.y))

    def draw(self):
        self.medium_enemy_rect.y -= self.speed
        self.__screen.blit(self.__medium_enemy_png, self.medium_enemy_rect)


