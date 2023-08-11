import pygame

from frontend.armored_train.game.assets.asset_manager import AssetManager
from frontend.armored_train.view.models.authorization_model import AuthorizationModel
from frontend.armored_train.view.screens.screen import Screen
from frontend.armored_train.view.widgets.button_widgets import AuthorizationButtonWidget
from frontend.armored_train.view.widgets.input_text_widget import InputTextWidget
from frontend.armored_train.view.widgets.textbox_widget import TextBoxWidget


class AuthorizationScreen(Screen):
    def __init__(self, width: int, height: int, caption: str, model, asset_manager):
        super().__init__(width, height, caption)
        self.model = model
        self.asset_manager = asset_manager
        self.background = pygame.image.load(self.asset_manager.get_asset_path("images", "background")).convert()

        self.authorization_screen_title = TextBoxWidget(0, 100, 0, 0, self.screen, self.asset_manager,
                                                        text='Авторизация', center_x=True)
        self.username_label = TextBoxWidget(600, 400, 0, 0, self.screen, self.asset_manager, 'Почта')
        self.password_label = TextBoxWidget(600, 500, 0, 0, self.screen, self.asset_manager, 'Пароль')
        self.authorization_input = InputTextWidget(760, 400, 400, 50, self.screen, self.model, self.asset_manager)
        self.authorization_button = AuthorizationButtonWidget(860, 900, 200, 50, self.screen, self.model,
                                                              self.asset_manager)

    def draw(self):
        self.screen.blit(self.background, (0, 0))

        self.authorization_screen_title.text_font = pygame.font.Font(
            asset_manager.get_asset_path('fonts', 'Oswald-Light'), 72)
        self.authorization_screen_title.draw()

        self.username_label.draw()
        self.password_label.draw()

        self.authorization_input.draw()

        self.authorization_button.draw()

        pygame.display.flip()


class Controller:
    def __init__(self, model, authorization_screen):
        self.model = model
        self.authorization_screen = authorization_screen
        self.running = True

    def save_auth_data(self):
        self.model.username = self.model.input_boxes[0]['text']
        self.model.password = self.model.input_boxes[1]['text']
        self.model.active_input_box = None
        self.model.input_boxes[0]['text'] = ''
        self.model.input_boxes[1]['text'] = ''
        self.model.auth_button_active = 'inactive'

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

        elif event.type == pygame.KEYDOWN:
            if self.model.active_input_box:
                if event.key == pygame.K_RETURN or self.model.auth_button_active == 'active':
                    self.save_auth_data()
                elif event.key == pygame.K_BACKSPACE:
                    self.model.active_input_box['text'] = self.model.active_input_box['text'][:-1]
                elif len(self.model.active_input_box['text']) < 20:
                    self.model.active_input_box['text'] += event.unicode
        elif self.model.auth_button_active == 'active':
            self.save_auth_data()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)

            self.authorization_screen.draw()

        pygame.quit()


asset_manager = AssetManager("../../game/assets/assets.json")
asset_manager.load_assets()
model = AuthorizationModel()
authorization_screen = AuthorizationScreen(1920, 1080, 'Authorization Screen', model, asset_manager)
controller = Controller(model, authorization_screen)
controller.run()
