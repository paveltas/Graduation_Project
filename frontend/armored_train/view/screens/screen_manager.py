class ScreenManager:
    def __init__(self):
        self.screens = []
        self.controllers = {}
        self.active_screen = None

    def add_screen_add_controller(self, screen, controller):
        self.screens.append(screen)
        self.controllers[screen.caption] = controller

    def set_active_screen(self, screen_name):
        for screen in self.screens:
            if screen.caption == screen_name:
                self.active_screen = screen

    def handle_event(self, event):
        if self.active_screen:
            self.controllers[self.active_screen.caption].handle_event(event)

    # def update(self):
    #     if self.active_screen:
    #         self.active_screen.update()

    def draw(self):
        if self.active_screen:
            self.active_screen.draw()
