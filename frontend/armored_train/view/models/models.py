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
        self.back_button_active = False


class RatingModel:
    def __init__(self):
        self.login = 'pavel'
        self.user_place = 0
        self.user_overall_score = 0
        self.users_overall_score = None
        self.levels_score = {}
        self.count = 0
        self.level = None
        self.points = None
        self.back_button_active = False


class LevelSelectionModel:
    def __init__(self):
        self.back_button_active = False
