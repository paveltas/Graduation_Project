import pygame


class EngineeringWagonObject:
    def __init__(self, x, y, screen, asset_manager):
        self.__screen = screen
        self.__asset_manager = asset_manager
        self.x = x
        self.y = y
        self.armor = 150
        self.health = 200
        self.slots_on_the_top = 5

        self.__engineering_wagon_png = pygame.image.load(
            self.__asset_manager.get_asset_path("images", "engineering_wagon")).convert_alpha()
        self.engineering_wagon_rect = self.__engineering_wagon_png.get_rect(topleft=(self.x, self.y))

    def draw(self):
        self.__screen.blit(self.__engineering_wagon_png, self.engineering_wagon_rect)
