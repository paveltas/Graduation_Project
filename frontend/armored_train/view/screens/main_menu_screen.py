import pygame

from frontend.armored_train.view.screens.screen import Screen
from frontend.armored_train.view.widgets.button_widgets import NewGameButtonWidget, ContinueButtonWidget, \
    LevelSelectionButtonWidget, RatingButtonWidget
from frontend.armored_train.view.widgets.textbox_widget import TextBoxWidget


class MainMenuScreen(Screen):
    def __init__(self, width: int, height: int, caption: str, model, asset_manager):
        super().__init__(width, height, caption, asset_manager)
        self.caption = caption
        self.__model = model
        self.__background = pygame.image.load(self.asset_manager.get_asset_path("images", "background")).convert()

        self.__main_menu_screen_title = TextBoxWidget(0, 100, 0, 0, self.screen,
                                                      'Главное Меню', center_x=True)

        self.__new_game_button = NewGameButtonWidget(835, 400, 250, 50, self.screen,
                                                     self.__model, 'Новая Игра')
        self.__continue_button = ContinueButtonWidget(835, 500, 250, 50, self.screen,
                                                      self.__model, 'Продолжить')
        self.__level_selection_button = LevelSelectionButtonWidget(835, 600, 250, 50, self.screen,
                                                                   self.__model, 'Выбрать Уровень')
        self.__rating_button = RatingButtonWidget(835, 700, 250, 50, self.screen,
                                                  self.__model, 'Рейтинг')

    def draw(self):
        self.screen.blit(self.__background, (0, 0))

        self.__main_menu_screen_title.text_font = pygame.font.Font(
            self.asset_manager.get_asset_path('fonts', 'Oswald-Light'), 72)
        self.__main_menu_screen_title.draw()

        self.__new_game_button.draw()
        self.__continue_button.draw()
        self.__level_selection_button.draw()
        self.__rating_button.draw()

        pygame.display.flip()
