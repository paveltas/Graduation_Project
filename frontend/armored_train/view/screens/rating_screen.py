import pygame

from frontend.armored_train.view.screens.screen import Screen
from frontend.armored_train.view.widgets.textbox_widget import TextBoxWidget


class RatingScreen(Screen):
    def __init__(self, width: int, height: int, caption: str, model, asset_manager):
        super().__init__(width, height, caption, asset_manager)
        self.caption = caption
        self.model = model
        print(f'экран рейтинга{self.model.player}')
        self.background = pygame.image.load(self.asset_manager.get_asset_path("images", "background")).convert()

        self.rating_screen_title = TextBoxWidget(0, 100, 0, 0, self.screen, self.asset_manager,
                                                 'Рейтинг', center_x=True)
        self.rating_text_box = TextBoxWidget(0, 0, 0, 0, self.screen, self.asset_manager, self.model.player)

    def draw(self):
        self.screen.blit(self.background, (0, 0))

        self.rating_screen_title.text_font = pygame.font.Font(
            self.asset_manager.get_asset_path('fonts', 'Oswald-Light'), 72)
        self.rating_screen_title.draw()

        self.rating_text_box.draw()

        pygame.display.flip()
