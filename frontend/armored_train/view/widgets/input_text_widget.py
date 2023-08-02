import pygame

from frontend.armored_train.view.models.authorization_model import AuthorizationModel
from frontend.armored_train.view.widgets.widget import Widget


class InputTextWidget(Widget):
    def __init__(self, x, y, width, height, screen):
        super().__init__(x, y, width, height, screen)
        self.model = AuthorizationModel()

    def draw(self):
        pygame.draw.rect(self.screen, (130, 130, 130), (self.x, self.y, self.width, self.height), self.border_width)
        pygame.draw.rect(self.screen, (130, 130, 130), (self.x, self.y + 100, self.width, self.height), self.border_width)

        username_input = self.text_font.render(self.model.input_boxes[0]['text'], True, self.font_color)
        password_input = self.text_font.render("*" * len(self.model.input_boxes[1]['text']), True, self.font_color)
        self.screen.blit(username_input, (self.x, self.y))
        self.screen.blit(password_input, (self.x, self.y + 100))

    def handle_event(self):
        pass
