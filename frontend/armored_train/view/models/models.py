class AuthorizationModel:
    def __init__(self):
        self.active_box = None
        self.auth_button_active = 'inactive'
        self.reg_button_active = 'inactive'
        self.token = None

        self.input_fields = {'login': '', 'password': ''}
