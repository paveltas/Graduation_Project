import pygame

from frontend.armored_train.view.widgets.widget import Widget


class AuthorizationButtonWidget(Widget):
    def __init__(self, x, y, width, height, screen, authorization_model, asset_manager):
        super().__init__(x, y, width, height, screen, asset_manager)
        self.model = authorization_model

    def draw(self):
        authorization_button = pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height),
                                                self.border_width)
        button_text = self.text_font.render('Вход', True, self.font_color)
        self.screen.blit(button_text, (self.x + 72, self.y - 5))

        mouse_over_button = authorization_button.collidepoint(pygame.mouse.get_pos())
        left_click = pygame.mouse.get_pressed()[0]
        if mouse_over_button and left_click:
            self.model.auth_button_active = 'active'
            self.color = 255, 0, 0
            self.border_width = 4

        else:
            self.color = 130, 130, 130
            self.border_width = 2


class RegistrationButtonWidget(Widget):
    def __init__(self, x, y, width, height, screen, authorization_model, asset_manager):
        super().__init__(x, y, width, height, screen, asset_manager)
        self.model = authorization_model

    def draw(self):
        authorization_button = pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height),
                                                self.border_width)
        button_text = self.text_font.render('Регистрация', True, self.font_color)
        self.screen.blit(button_text, (self.x + 21, self.y - 5))

        mouse_over_button = authorization_button.collidepoint(pygame.mouse.get_pos())
        left_click = pygame.mouse.get_pressed()[0]
        if mouse_over_button and left_click:
            self.model.reg_button_active = 'active'
            self.color = 255, 0, 0
            self.border_width = 4

        else:
            self.color = 130, 130, 130
            self.border_width = 2

