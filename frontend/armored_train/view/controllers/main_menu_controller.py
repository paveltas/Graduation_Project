from frontend.armored_train.view.controllers.controller import Controller


class MainMenuController(Controller):
    def __init__(self, model, screen, screen_manager):
        super().__init__(model, screen, screen_manager)

    def handle_event(self, event):

        if self.model.new_game_button_active:
            print('is active new_game_button_active')

        if self.model.continue_button_active:
            print('is active continue_button_active')

        if self.model.level_selection_button_active:
            self.screen_manager.set_active_screen('Level Selection Screen')
            print('is active level_selection_button_active')

        if self.model.rating_button_active:
            self.screen_manager.set_active_screen('Rating Screen')
            print('is active rating_button_active')
