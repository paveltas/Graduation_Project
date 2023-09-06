import pygame

from frontend.armored_train.game.game_objects.enemies.light import LightEnemyObject
from frontend.armored_train.game.game_objects.wagons.engineering_wagon import EngineeringWagonObject
from frontend.armored_train.game.game_objects.wagons.locomotive import LocomotiveObject
from frontend.armored_train.game.game_objects.wagons.wagon import WagonObject
from frontend.armored_train.view.screens.screen import Screen


class FirstLevelScreen(Screen):
    def __init__(self, width: int, height: int, caption: str, model, asset_manager):
        super().__init__(width, height, caption, asset_manager)
        self.caption = caption
        self.__model = model
        self.__background = pygame.image.load(self.asset_manager.get_asset_path("images", "first_level")).convert()
        self.__enemy_spawn_timer = pygame.time.get_ticks()
        self.__enemy_spawn_delay = 1000

        self.__locomotive = LocomotiveObject(914, 50, self.screen, self.asset_manager)
        self.__engineering_wagon = EngineeringWagonObject(905, 270, self.screen, self.asset_manager)

    def draw(self):
        self.screen.blit(self.__background, (0, 0))

        self.__locomotive.draw()
        self.__engineering_wagon.draw()

        wagon_y = 408
        for _ in range(5):
            wagon = WagonObject(923, wagon_y, self.screen, self.asset_manager)
            self.__model.wagons.append(wagon)
            wagon_y += 128

        for wagon in self.__model.wagons:
            wagon.draw()

        current_time = pygame.time.get_ticks()
        if current_time - self.__enemy_spawn_timer >= self.__enemy_spawn_delay:
            enemy = LightEnemyObject(780, 1080, self.screen, self.asset_manager)
            self.__model.enemies.append(enemy)
            self.__enemy_spawn_timer = current_time

        for enemy in self.__model.enemies:
            enemy.draw()

        pygame.display.flip()
