from frontend.armored_train.view.widgets.widget import Widget


class TextBoxWidget(Widget):
    def __init__(self, x, y, width, height, screen, asset_manager, text, font_color=None, center_x=False,
                 center_y=False):
        super().__init__(x, y, width, height, screen, asset_manager, text)
        if font_color is not None:
            self.font_color = font_color
        self.center_x = center_x
        self.center_y = center_y

    def draw(self):
        text_on_screen = self.text_font.render(self.text, True, self.font_color)

        if self.center_x:
            x_pos = self.x + (self.screen.get_width() - text_on_screen.get_width()) // 2
        else:
            x_pos = self.x

        if self.center_y:
            y_pos = self.y + (self.screen.get_height() - text_on_screen.get_height()) // 2
        else:
            y_pos = self.y

        self.screen.blit(text_on_screen, (x_pos, y_pos))


# class RatingTextBoxWidget(Widget):
#     def __init__(self, x, y, width, height, screen, asset_manager, model, text=None, font_color=None, center_x=False,
#                  center_y=False):
#         super().__init__(x, y, width, height, screen, asset_manager, text)
#         if font_color is not None:
#             self.font_color = font_color
#         self.center_x = center_x
#         self.center_y = center_y
#         self.model = model
#
#     def draw(self):
#         text_on_screen = self.text_font.render(self.model.player, True, self.font_color)
#
#         if self.center_x:
#             x_pos = self.x + (self.screen.get_width() - text_on_screen.get_width()) // 2
#         else:
#             x_pos = self.x
#
#         if self.center_y:
#             y_pos = self.y + (self.screen.get_height() - text_on_screen.get_height()) // 2
#         else:
#             y_pos = self.y
#
#         self.screen.blit(text_on_screen, (x_pos, y_pos))