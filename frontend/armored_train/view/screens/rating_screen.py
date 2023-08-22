import pygame

from frontend.armored_train.view.screens.screen import Screen
from frontend.armored_train.view.widgets.alpha_rect_widget import AlphaRectWidget
from frontend.armored_train.view.widgets.textbox_widget import TextBoxWidget, PersonalOverallRatingTextWidget, \
    GeneralOverallRatingTextWidget


class RatingScreen(Screen):
    def __init__(self, width: int, height: int, caption: str, model, asset_manager):
        super().__init__(width, height, caption, asset_manager)
        self.caption = caption
        self.model = model
        print(f'экран рейтинга{self.model.player}')
        self.background = pygame.image.load(self.asset_manager.get_asset_path("images", "background")).convert()

        self.rating_screen_title = TextBoxWidget(0, 0, 0, 0, self.screen, self.asset_manager,
                                                 'Рейтинг', center_x=True)
        self.right_alpha_rect = AlphaRectWidget(25, 100, 920, 965, self.screen, self.asset_manager, alpha=100)
        self.left_alpha_rect = AlphaRectWidget(975, 100, 920, 965, self.screen, self.asset_manager, alpha=100)
        self.personal_overall_rating_rect = PersonalOverallRatingTextWidget(35, 110, 900, 215, self.screen, self.model,
                                                                            self.asset_manager, center_x=True)
        self.general_overall_rating_rect = GeneralOverallRatingTextWidget(35, 345, 900, 709, self.screen, self.model,
                                                                          self.asset_manager, center_x=True)

    def draw(self):
        self.screen.blit(self.background, (0, 0))

        self.rating_screen_title.text_font = pygame.font.Font(
            self.asset_manager.get_asset_path('fonts', 'Oswald-Light'), 72)
        self.rating_screen_title.draw()

        self.right_alpha_rect.draw()
        self.left_alpha_rect.draw()

        self.personal_overall_rating_rect.draw()
        self.general_overall_rating_rect.draw()

        pygame.display.flip()
