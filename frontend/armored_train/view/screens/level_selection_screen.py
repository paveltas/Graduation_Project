import pygame

from frontend.armored_train.view.screens.screen import Screen
from frontend.armored_train.view.widgets.button_widgets import BackButtonWidget
from frontend.armored_train.view.widgets.textbox_widget import TextBoxWidget


class LevelSelectionScreen(Screen):
    def __init__(self, width: int, height: int, caption: str, model, asset_manager):
        super().__init__(width, height, caption, asset_manager)
        self.caption = caption
        self.model = model
        self.__background = pygame.image.load(self.asset_manager.get_asset_path("images", "background")).convert()

        self.__rating_screen_title = TextBoxWidget(0, 100, 0, 0, self.screen,
                                                   'Выбор Уровня', center_x=True)
        self.__back_button = BackButtonWidget(1795, 35, 100, 50, self.screen, self.model, 'Назад')

    def draw(self):
        self.screen.blit(self.__background, (0, 0))

        self.__rating_screen_title.text_font = pygame.font.Font(
            self.asset_manager.get_asset_path('fonts', 'Oswald-Light'), 72)
        self.__rating_screen_title.draw()

        self.__back_button.draw()

        pygame.display.flip()
