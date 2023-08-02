import pygame.draw

from frontend.armored_train.view.widgets.widget import Widget
from frontend.armored_train.view.widgets.widget_utils import WidgetUtils


class ButtonWidget(Widget):
    def __init__(self, x, y, width, height, screen):
        super().__init__(x, y, width, height, screen)
        self.center_x_y = WidgetUtils(self.width, self.height)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height), self.border_width)
        button_text = self.text_font.render(self.caption, True, self.font_color)
        # self.screen.blit(button_text, self.center_x_y.center_on_x_and_y(button_text))
        self.screen.blit(button_text, (self.x + 72, self.y - 5))
