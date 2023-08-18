import pygame

from frontend.armored_train.view.screens.screen import Screen
from frontend.armored_train.view.widgets.button_widgets import AuthorizationButtonWidget, RegistrationButtonWidget
from frontend.armored_train.view.widgets.input_text_widget import InputTextWidget
from frontend.armored_train.view.widgets.textbox_widget import TextBoxWidget


class AuthorizationScreen(Screen):
    def __init__(self, width: int, height: int, caption: str, model, asset_manager):
        super().__init__(width, height, caption, asset_manager)
        self.caption = caption
        self.model = model
        self.background = pygame.image.load(self.asset_manager.get_asset_path("images", "background")).convert()

        self.authorization_screen_title = TextBoxWidget(0, 100, 0, 0, self.screen, self.asset_manager,
                                                        'Авторизация', center_x=True)
        self.warning_text = TextBoxWidget(0, 300, 0, 0, self.screen, self.asset_manager, '', font_color=(255, 0, 0),
                                          center_x=True)
        self.username_label = TextBoxWidget(600, 400, 0, 0, self.screen, self.asset_manager, 'Логин')
        self.password_label = TextBoxWidget(600, 500, 0, 0, self.screen, self.asset_manager, 'Пароль')
        self.authorization_input = InputTextWidget(760, 400, 400, 50, self.screen, self.model, self.asset_manager)
        self.authorization_button = AuthorizationButtonWidget(755, 900, 200, 50, self.screen, self.model,
                                                              self.asset_manager, 'Авторизация')
        self.registration_button = RegistrationButtonWidget(965, 900, 200, 50, self.screen, self.model,
                                                            self.asset_manager, 'Регистрация')

    def draw(self):
        self.screen.blit(self.background, (0, 0))

        self.authorization_screen_title.text_font = pygame.font.Font(
            self.asset_manager.get_asset_path('fonts', 'Oswald-Light'), 72)
        self.authorization_screen_title.draw()

        self.warning_text.draw()

        self.username_label.draw()
        self.password_label.draw()

        self.authorization_input.draw()

        self.authorization_button.draw()
        self.registration_button.draw()

        pygame.display.flip()



