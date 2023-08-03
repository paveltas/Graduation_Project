import pygame

from frontend.armored_train.view.models.authorization_model import AuthorizationModel
from frontend.armored_train.view.widgets.widget import Widget


class InputTextWidget(Widget):
    def __init__(self, x, y, width, height, screen):
        super().__init__(x, y, width, height, screen)
        self.username_rect = None
        self.password_rect = None
        self.model = AuthorizationModel()
        self.active_input_field = None

    def draw(self):
        username_rect_color = (130, 130, 130)
        password_rect_color = (130, 130, 130)

        if self.active_input_field == 'username':
            username_rect_color = (255, 0, 0)
        elif self.active_input_field == 'password':
            password_rect_color = (255, 0, 0)

        self.username_rect = pygame.draw.rect(self.screen, username_rect_color,
                                              (self.x, self.y, self.width, self.height),
                                              self.border_width)
        self.password_rect = pygame.draw.rect(self.screen, password_rect_color,
                                              (self.x, self.y + 100, self.width, self.height),
                                              self.border_width)

        username_input = self.text_font.render('Hello', True, self.font_color)
        password_input = self.text_font.render("*" * len('Hello'), True, self.font_color)
        self.screen.blit(username_input, (self.x + 5, self.y))
        self.screen.blit(password_input, (self.x + 5, self.y + 105))

        self.handle_event()

    def handle_event(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        if self.username_rect.collidepoint(mouse_pos) and left_click:
            self.active_input_field = 'username'
        elif self.password_rect.collidepoint(mouse_pos) and left_click:
            self.active_input_field = 'password'

