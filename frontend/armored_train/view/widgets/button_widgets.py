import pygame

# from frontend.armored_train.game.assets.asset_manager import AssetManager
from frontend.armored_train.view.widgets.widget import Widget


class AuthorizationButtonWidget(Widget):
    def __init__(self, x, y, width, height, screen):
        super().__init__(x, y, width, height, screen)
        # self.fonts = AssetManager('../../game/assets/assets.json')
        # self.fonts.load_assets()
        # self.fonts.get_asset_path("fonts", "Oswald-Light")
        # self.text_font = pygame.font.Font(self.fonts, 36)

    def draw(self):
        authorization_button = pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height),
                                                self.border_width)
        button_text = self.text_font.render('Вход', True, self.font_color)
        self.screen.blit(button_text, (self.x + 72, self.y - 5))

        mouse_pos = pygame.mouse.get_pos()
        mouse_over_button = authorization_button.collidepoint(mouse_pos)
        left_click = pygame.mouse.get_pressed()[0]

        if mouse_over_button and left_click:
            self.color = 255, 0, 0
            self.border_width = 4
        else:
            self.color = 130, 130, 130
            self.border_width = 2

    def handle_event(self):
        pass
