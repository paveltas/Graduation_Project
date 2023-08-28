from frontend.armored_train.view.controllers.controller import Controller


class FirstLevelController(Controller):
    def __init__(self, model, screen, screen_manager):
        super().__init__(model, screen, screen_manager)

    def handle_event(self, event):
        pass
