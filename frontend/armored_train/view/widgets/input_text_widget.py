import pygame

from frontend.armored_train.view.widgets.widget import Widget


class InputTextWidget(Widget):
    def __init__(self, x, y, width, height, screen, authorization_model, asset_manager):
        super().__init__(x, y, width, height, screen, asset_manager)
        self.model = authorization_model
        self.username_rect = None
        self.password_rect = None

    def draw(self):
        username_rect_color = (130, 130, 130)
        password_rect_color = (130, 130, 130)

        if self.model.active_box == 'login':
            username_rect_color = (255, 0, 0)
        elif self.model.active_box == 'password':
            password_rect_color = (255, 0, 0)

        self.username_rect = pygame.draw.rect(self.screen, username_rect_color,
                                              (self.x, self.y, self.width, self.height),
                                              self.border_width)
        self.password_rect = pygame.draw.rect(self.screen, password_rect_color,
                                              (self.x, self.y + 100, self.width, self.height),
                                              self.border_width)

        username_input = self.text_font.render(self.model.input_fields['login'], True, self.font_color)
        password_input = self.text_font.render("*" * len(self.model.input_fields['password']), True, self.font_color)
        self.screen.blit(username_input, (self.x + 5, self.y - 3))
        self.screen.blit(password_input, (self.x + 5, self.y + 105))

        self.handle_event()

    def handle_event(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        if self.username_rect.collidepoint(mouse_pos) and left_click:
            self.model.active_box = 'login'
        elif self.password_rect.collidepoint(mouse_pos) and left_click:
            self.model.active_box = 'password'
        elif not self.password_rect.collidepoint(mouse_pos) and left_click:
            self.model.active_box = None
