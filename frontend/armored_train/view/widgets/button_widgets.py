import pygame

from frontend.armored_train.view.widgets.widget import Widget


class ButtonWidget(Widget):
    def __init__(self, x, y, width, height, screen, asset_manager, text):
        super().__init__(x, y, width, height, screen, asset_manager, text)
        self.button_active = False

    def draw(self):
        button = pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height),
                                  self.border_width)
        button_text = self.text_font.render(self.text, True, self.font_color)

        text_x, text_y = self.x + (self.width - button_text.get_width()) // 2, self.y + (
                self.height - button_text.get_height()) // 2

        self.screen.blit(button_text, (text_x, text_y - 4))

        mouse_over_button = button.collidepoint(pygame.mouse.get_pos())
        left_click = pygame.mouse.get_pressed()[0]
        if mouse_over_button and left_click:
            self.button_active = True
            self.color = 255, 0, 0
            self.border_width = 4

        else:
            self.button_active = False
            self.color = 130, 130, 130
            self.border_width = 2


class AuthorizationButtonWidget(ButtonWidget):
    def __init__(self, x, y, width, height, screen, authorization_model, asset_manager, text):
        super().__init__(x, y, width, height, screen, asset_manager, text)
        self.model = authorization_model

    def draw(self):
        super().draw()

        if self.button_active:
            self.model.auth_button_active = True
        else:
            self.model.auth_button_active = False


class RegistrationButtonWidget(ButtonWidget):
    def __init__(self, x, y, width, height, screen, authorization_model, asset_manager, text):
        super().__init__(x, y, width, height, screen, asset_manager, text)
        self.model = authorization_model

    def draw(self):
        super().draw()

        if self.button_active:
            self.model.reg_button_active = True
        else:
            self.model.reg_button_active = False


class NewGameButtonWidget(ButtonWidget):
    def __init__(self, x, y, width, height, screen, main_menu_model, asset_manager, text):
        super().__init__(x, y, width, height, screen, asset_manager, text)
        self.model = main_menu_model

    def draw(self):
        super().draw()

        if self.button_active:
            self.model.new_game_button_active = True
        else:
            self.model.new_game_button_active = False


class ContinueButtonWidget(ButtonWidget):
    def __init__(self, x, y, width, height, screen, main_menu_model, asset_manager, text):
        super().__init__(x, y, width, height, screen, asset_manager, text)
        self.model = main_menu_model

    def draw(self):
        super().draw()

        if self.button_active:
            self.model.continue_button_active = True
        else:
            self.model.continue_button_active = False


class LevelSelectionButtonWidget(ButtonWidget):
    def __init__(self, x, y, width, height, screen, main_menu_model, asset_manager, text):
        super().__init__(x, y, width, height, screen, asset_manager, text)
        self.model = main_menu_model

    def draw(self):
        super().draw()

        if self.button_active:
            self.model.level_selection_button_active = True
        else:
            self.model.level_selection_button_active = False


class RatingButtonWidget(ButtonWidget):
    def __init__(self, x, y, width, height, screen, main_menu_model, asset_manager, text):
        super().__init__(x, y, width, height, screen, asset_manager, text)
        self.model = main_menu_model

    def draw(self):
        super().draw()

        if self.button_active:
            self.model.rating_button_active = True
        else:
            self.model.rating_button_active = False
