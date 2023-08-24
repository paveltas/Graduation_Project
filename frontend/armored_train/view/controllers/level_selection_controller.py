from frontend.armored_train.view.controllers.controller import Controller


class LevelSelectionController(Controller):
    def __init__(self, model, screen, screen_manager):
        super().__init__(model, screen, screen_manager)

    def handle_event(self, event):
        if self.model.back_button_active:
            self.screen_manager.set_active_screen('Main Menu Screen')
