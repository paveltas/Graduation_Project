import pygame

from frontend.armored_train.game.game_objects.enemies.light import LightEnemyObject
from frontend.armored_train.view.screens.screen import Screen
from frontend.armored_train.game.game_objects.wagons.locomotive import LocomotiveObject


class FirstLevelScreen(Screen):
    def __init__(self, width: int, height: int, caption: str, model, asset_manager):
        super().__init__(width, height, caption, asset_manager)
        self.caption = caption
        self.model = model
        self.__background = pygame.image.load(self.asset_manager.get_asset_path("images", "first_level")).convert()

        self.locomotive_object = LocomotiveObject(self.screen)
        self.light_enemy_object = LightEnemyObject(800, 500, self.screen)

    def draw(self):
        self.screen.blit(self.__background, (0, 0))

        self.locomotive_object.draw()

        self.light_enemy_object.draw()

        pygame.display.flip()
