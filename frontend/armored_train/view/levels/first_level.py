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
        self.model = model
        self.__background = pygame.image.load(self.asset_manager.get_asset_path("images", "first_level")).convert()
        self.enemy_spawn_timer = pygame.time.get_ticks()
        self.enemy_spawn_delay = 1000

        self.locomotive = LocomotiveObject(914, 50, self.screen, self.asset_manager)
        self.engineering_wagon = EngineeringWagonObject(905, 270, self.screen, self.asset_manager)
        self.wagon1 = WagonObject(923, 408, self.screen, self.asset_manager)
        self.wagon2 = WagonObject(923, 536, self.screen, self.asset_manager)
        self.wagon3 = WagonObject(923, 664, self.screen, self.asset_manager)
        self.wagon4 = WagonObject(923, 792, self.screen, self.asset_manager)
        self.wagon5 = WagonObject(923, 920, self.screen, self.asset_manager)

    def draw(self):
        self.screen.blit(self.__background, (0, 0))

        self.locomotive.draw()
        self.engineering_wagon.draw()
        self.wagon1.draw()
        self.wagon2.draw()
        self.wagon3.draw()
        self.wagon4.draw()
        self.wagon5.draw()

        current_time = pygame.time.get_ticks()
        if current_time - self.enemy_spawn_timer >= self.enemy_spawn_delay:
            enemy = LightEnemyObject(780, 1080, self.screen, self.asset_manager)
            self.model.enemies.append(enemy)
            self.enemy_spawn_timer = current_time

        for enemy in self.model.enemies:
            enemy.draw()

        pygame.display.flip()
