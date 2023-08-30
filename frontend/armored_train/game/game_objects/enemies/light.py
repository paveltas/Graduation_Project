import pygame


class LightEnemyObject:
    def __init__(self, x, y, screen, asset_manager):
        self.__screen = screen
        self.__asset_manager = asset_manager
        self.x = x
        self.y = y
        self.health = 50
        self.damage = 15
        self.speed = 5
        self.zone = 1

        self.__light_enemy_png = pygame.image.load(
            self.__asset_manager.get_asset_path("images", "light_enemy")).convert_alpha()
        self.light_enemy_rect = self.__light_enemy_png.get_rect(topleft=(self.x, self.y))

    def draw(self):
        self.light_enemy_rect.y -= self.speed
        self.__screen.blit(self.__light_enemy_png, self.light_enemy_rect)
