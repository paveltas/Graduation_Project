import pygame


class LocomotiveObject:
    def __init__(self, x, y, screen, asset_manager):
        self.__screen = screen
        self.__asset_manager = asset_manager
        self.x = x
        self.y = y
        self.armor = 150
        self.health = 200
        self.slots_on_the_left = 3
        self.slots_on_the_right = 3
        self.slots_on_the_top = 3

        self.__locomotive_png = pygame.image.load(
            self.__asset_manager.get_asset_path("images", "locomotive")).convert_alpha()
        self.locomotive_rect = self.__locomotive_png.get_rect(topleft=(self.x, self.y))

    def draw(self):
        self.__screen.blit(self.__locomotive_png, self.locomotive_rect)
