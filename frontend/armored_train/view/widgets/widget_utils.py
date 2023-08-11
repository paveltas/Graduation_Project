class WidgetUtils:
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height

    @staticmethod
    def align_center(x, y, surface, widget, center_x=False, center_y=False):
        if center_x and center_y:
            return x + (surface.get_width() - widget.get_width()) // 2, y + (
                        surface.get_height() - widget.get_height()) // 2

        if center_x:
            return x + (surface.get_width() - widget.get_width()) // 2

        if center_y:
            return y + (surface.get_height() - widget.get_height()) // 2
