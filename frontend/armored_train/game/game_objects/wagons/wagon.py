import pygame


class WagonObject:
    def __init__(self, x, y, screen, asset_manager):
        self.__screen = screen
        self.__asset_manager = asset_manager
        self.x = x
        self.y = y
        self.armor = 50
        self.health = 150
        self.slots_on_the_left = 2
        self.slots_on_the_right = 2
        self.slots_on_the_top = 2

        self.__wagon_png = pygame.image.load(
            self.__asset_manager.get_asset_path("images", "wagon")).convert_alpha()
        self.wagon_rect = self.__wagon_png.get_rect(topleft=(self.x, self.y))

    def draw(self):
        self.__screen.blit(self.__wagon_png, self.wagon_rect)
