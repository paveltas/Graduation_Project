import pygame

from frontend.armored_train.view.screens.screen import Screen
from frontend.armored_train.view.widgets.alpha_rect_widget import AlphaRectWidget
from frontend.armored_train.view.widgets.button_widgets import BackButtonWidget
from frontend.armored_train.view.widgets.textbox_widget import TextBoxWidget, PersonalOverallRatingTextWidget, \
    GeneralOverallRatingTextWidget, LevelsRatingTextWidget


class RatingScreen(Screen):
    def __init__(self, width: int, height: int, caption: str, model, asset_manager):
        super().__init__(width, height, caption, asset_manager)
        self.caption = caption
        self.model = model
        self.__background = pygame.image.load(self.asset_manager.get_asset_path("images", "background")).convert()

        self.__rating_screen_title = TextBoxWidget(0, 0, 0, 0, self.screen, self.asset_manager,
                                                   'Рейтинг', center_x=True)
        self.__right_alpha_rect = AlphaRectWidget(25, 100, 920, 965, self.screen, self.asset_manager, alpha=150)
        self.__left_alpha_rect = AlphaRectWidget(975, 100, 920, 965, self.screen, self.asset_manager, alpha=150)
        self.__personal_overall_rating_rect = PersonalOverallRatingTextWidget(35, 110, 900, 215, self.screen,
                                                                              self.model, self.asset_manager,
                                                                              center_x=True)
        self.__general_overall_rating_rect = GeneralOverallRatingTextWidget(35, 345, 900, 709, self.screen, self.model,
                                                                            self.asset_manager)
        self.__levels_rating_rect = LevelsRatingTextWidget(985, 110, 900, 944, self.screen, self.model,
                                                           self.asset_manager, center_x=True)
        self.__back_button = BackButtonWidget(1795, 35, 100, 50, self.screen, self.model, self.asset_manager, 'Назад')

    def draw(self):
        self.screen.blit(self.__background, (0, 0))

        self.__rating_screen_title.text_font = pygame.font.Font(
            self.asset_manager.get_asset_path('fonts', 'Oswald-Light'), 72)
        self.__rating_screen_title.draw()

        self.__back_button.draw()

        self.__right_alpha_rect.draw()
        self.__left_alpha_rect.draw()

        self.__personal_overall_rating_rect.draw()
        self.__general_overall_rating_rect.draw()
        self.__levels_rating_rect.draw()

        pygame.display.flip()
