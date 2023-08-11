import pygame


class AuthorizationModel:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.active_input_box = None
        self.auth_button_active = 'inactive'

        self.input_boxes = [
            {
                'text': ''
            },
            {
                'text': ''
            }
        ]