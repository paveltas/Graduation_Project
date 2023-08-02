class WidgetUtils:
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height

    def center_on_x_and_y(self, widget):
        widget_width, widget_height = widget.get_size()
        x = (self.window_width - widget_width) // 2
        y = (self.window_height - widget_height) // 2
        if x > 0 and y > 0:
            return x, y
        if x > 0 or y > 0:
            return x if x > 0 else y
        raise ValueError("Недопустимые значения x и y для центрирования виджета.")
