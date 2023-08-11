from frontend.armored_train.view.widgets.widget import Widget
from frontend.armored_train.view.widgets.widget_utils import WidgetUtils


class TextBoxWidget(Widget):
    def __init__(self, x, y, width, height, screen, asset_manager, text, center_x=False, center_y=False):
        super().__init__(x, y, width, height, screen, asset_manager, text)
        self.center_x = center_x
        self.center_y = center_y

    def draw(self):
        text_on_screen = self.text_font.render(self.text, True, self.font_color)

        if self.center_x and self.center_y:
            x_pos, y_pos = WidgetUtils.align_center(self.x, self.y, self.screen, text_on_screen, self.center_x, self.center_y)

        if self.center_x:
            x_pos = WidgetUtils.align_center(self.x, self.y, self.screen, text_on_screen, self.center_x, self.center_y)
        else:
            x_pos = self.x

        if self.center_y:
            y_pos = WidgetUtils.align_center(self.x, self.y, self.screen, text_on_screen, self.center_x, self.center_y)
        else:
            y_pos = self.y

        self.screen.blit(text_on_screen, (x_pos, y_pos))
