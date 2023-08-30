import pygame


class HeavyEnemyObject:
    def __init__(self, x, y, screen, asset_manager):
        self.__screen = screen
        self.__asset_manager = asset_manager
        self.x = x
        self.y = y
        self.health = 200
        self.damage = 70
        self.speed = 1
        self.zone = 2

        self.__heavy_enemy_png = pygame.image.load(
            self.__asset_manager.get_asset_path("images", "heavy_enemy")).convert_alpha()
        self.heavy_enemy_rect = self.__heavy_enemy_png.get_rect(topleft=(self.x, self.y))

    def draw(self):
        self.heavy_enemy_rect.y -= self.speed
        self.__screen.blit(self.__heavy_enemy_png, self.heavy_enemy_rect)

    def update(self):
        self.y -= 10
