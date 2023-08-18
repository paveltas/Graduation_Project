class AuthorizationModel:
    def __init__(self):
        self.active_box = None
        self.auth_button_active = False
        self.reg_button_active = False
        self.token = None

        self.input_fields = {'login': '', 'password': ''}


class MainMenuModel:
    def __init__(self):
        self.new_game_button_active = False
        self.continue_button_active = False
        self.level_selection_button_active = False
        self.rating_button_active = False


class RatingModel:
    def __init__(self):
        self.count = 0
        self.player = None
        self.level = None
        self.points = None
