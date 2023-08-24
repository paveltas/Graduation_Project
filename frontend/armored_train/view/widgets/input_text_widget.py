import pygame

from frontend.armored_train.view.widgets.widget import Widget


class InputTextWidget(Widget):
    def __init__(self, x, y, width, height, screen, model, asset_manager):
        super().__init__(x, y, width, height, screen, asset_manager)
        self.__model = model
        self.__username_rect = None
        self.__password_rect = None

    def draw(self):
        username_rect_color = (130, 130, 130)
        password_rect_color = (130, 130, 130)

        if self.__model.active_box == 'login':
            username_rect_color = (255, 0, 0)
        elif self.__model.active_box == 'password':
            password_rect_color = (255, 0, 0)

        self.__username_rect = pygame.draw.rect(self.screen, username_rect_color,
                                                (self.x, self.y, self.width, self.height), self.border_width)
        self.__password_rect = pygame.draw.rect(self.screen, password_rect_color,
                                                (self.x, self.y + 100, self.width, self.height),
                                                self.border_width)

        username_input = self.text_font.render(self.__model.input_fields['login'], True, self.font_color)
        password_input = self.text_font.render("*" * len(self.__model.input_fields['password']), True, self.font_color)
        self.screen.blit(username_input, (self.x + 5, self.y - 3))
        self.screen.blit(password_input, (self.x + 5, self.y + 105))

        self.__handle_event()

    def __handle_event(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        if self.__username_rect.collidepoint(mouse_pos) and left_click:
            self.__model.active_box = 'login'
        elif self.__password_rect.collidepoint(mouse_pos) and left_click:
            self.__model.active_box = 'password'
        elif not self.__password_rect.collidepoint(mouse_pos) and left_click:
            self.__model.active_box = None
