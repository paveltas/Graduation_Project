import pygame.draw

from frontend.armored_train.game.assets.asset_manager import AssetManager
from frontend.armored_train.view.widgets.widget import Widget


class AuthorizationButtonWidget(Widget):
    def __init__(self, x, y, width, height, screen):
        super().__init__(x, y, width, height, screen)
        self.fonts = AssetManager('../../game/assets/assets.json')
        self.fonts.load_assets()
        self.fonts.get_asset_path("fonts", "Oswald-Light")
        self.text_font = pygame.font.Font(self.fonts, 36)

    def draw(self):
        pygame.draw.rect(self.screen, (130, 130, 130), (self.x, self.y, self.width, self.height), self.border_width)
        button_text = self.text_font.render('Вход', True, self.font_color)
        self.screen.blit(button_text, (self.x + 72, self.y - 5))

    def handle_event(self):
        pass
