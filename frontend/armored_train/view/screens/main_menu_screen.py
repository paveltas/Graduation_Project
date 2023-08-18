import pygame

from frontend.armored_train.view.screens.screen import Screen
from frontend.armored_train.view.widgets.button_widgets import NewGameButtonWidget, ContinueButtonWidget, \
    LevelSelectionButtonWidget, RatingButtonWidget
from frontend.armored_train.view.widgets.textbox_widget import TextBoxWidget


class MainMenuScreen(Screen):
    def __init__(self, width: int, height: int, caption: str, model, asset_manager):
        super().__init__(width, height, caption, asset_manager)
        self.caption = caption
        self.model = model

        self.background = pygame.image.load(self.asset_manager.get_asset_path("images", "background")).convert()

        self.main_menu_screen_title = TextBoxWidget(0, 100, 0, 0, self.screen, self.asset_manager,
                                                    'Главное Меню', center_x=True)

        self.new_game_button = NewGameButtonWidget(835, 400, 250, 50, self.screen,
                                                   self.model, self.asset_manager, 'Новая Игра')
        self.continue_button = ContinueButtonWidget(835, 500, 250, 50, self.screen,
                                                    self.model, self.asset_manager, 'Продолжить')
        self.level_selection_button = LevelSelectionButtonWidget(835, 600, 250, 50, self.screen,
                                                                 self.model, self.asset_manager, 'Выбрать Уровень')
        self.rating_button = RatingButtonWidget(835, 700, 250, 50, self.screen,
                                                self.model, self.asset_manager, 'Рейтинг')

    def draw(self):
        self.screen.blit(self.background, (0, 0))

        self.main_menu_screen_title.text_font = pygame.font.Font(
            self.asset_manager.get_asset_path('fonts', 'Oswald-Light'), 72)
        self.main_menu_screen_title.draw()

        self.new_game_button.draw()
        self.continue_button.draw()
        self.level_selection_button.draw()
        self.rating_button.draw()

        pygame.display.flip()
