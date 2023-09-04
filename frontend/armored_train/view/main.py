import pygame

from frontend.armored_train.game.assets.asset_manager import AssetManager
from frontend.armored_train.view.controllers.authorization_controller import AuthorizationController
from frontend.armored_train.view.controllers.first_level_controller import FirstLevelController
from frontend.armored_train.view.controllers.level_selection_controller import LevelSelectionController
from frontend.armored_train.view.controllers.main_menu_controller import MainMenuController
from frontend.armored_train.view.controllers.rating_controller import RatingController
from frontend.armored_train.view.levels.first_level import FirstLevelScreen
from frontend.armored_train.view.models.models import MainMenuModel, RatingModel, AuthorizationModel, \
    LevelSelectionModel, FirstLevelModel
from frontend.armored_train.view.screens.authorization_screen import AuthorizationScreen
from frontend.armored_train.view.screens.level_selection_screen import LevelSelectionScreen
from frontend.armored_train.view.screens.main_menu_screen import MainMenuScreen
from frontend.armored_train.view.screens.rating_screen import RatingScreen
from frontend.armored_train.view.screens.screen_manager import ScreenManager


def main():
    pygame.init()

    screen_manager = ScreenManager()

    asset_manager = AssetManager("../game/assets/assets.yaml")
    asset_manager.load_assets()

    model = MainMenuModel()
    main_menu_screen = MainMenuScreen(1920, 1080, 'Main Menu Screen', model, asset_manager)
    main_menu_controller = MainMenuController(model, main_menu_screen, screen_manager)
    screen_manager.add_screen_add_controller(main_menu_screen, main_menu_controller)

    model = AuthorizationModel()
    authorization_screen = AuthorizationScreen(1920, 1080, 'Authorization Screen', model, asset_manager)
    authorization_controller = AuthorizationController(model, authorization_screen, screen_manager)
    screen_manager.add_screen_add_controller(authorization_screen, authorization_controller)
    print(authorization_screen.__dict__)
    # print(authorization_screen.width)

    model = RatingModel()
    rating_screen = RatingScreen(1920, 1080, 'Rating Screen', model, asset_manager)
    rating_controller = RatingController(model, rating_screen, screen_manager)
    screen_manager.add_screen_add_controller(rating_screen, rating_controller)

    model = LevelSelectionModel()
    level_selection_screen = LevelSelectionScreen(1920, 1080, 'Level Selection Screen', model, asset_manager)
    level_selection_controller = LevelSelectionController(model, level_selection_screen, screen_manager)
    screen_manager.add_screen_add_controller(level_selection_screen, level_selection_controller)

    model = FirstLevelModel()
    first_level_screen = FirstLevelScreen(1920, 1080, 'First Level Screen', model, asset_manager)
    first_level_controller = FirstLevelController(model, first_level_screen, screen_manager)
    screen_manager.add_screen_add_controller(first_level_screen, first_level_controller)

    screen_manager.set_active_screen('Main Menu Screen')

    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            screen_manager.handle_event(event)

        screen_manager.draw()

    pygame.quit()


if __name__ == "__main__":
    main()
