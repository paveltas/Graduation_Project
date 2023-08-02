import pygame


class AuthorizationModel:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.active_input_box = None

        self.input_boxes = [
            {
                'rect': pygame.Rect(800, 400, 400, 50),
                'active': False,
                'text': ''
            },
            {
                'rect': pygame.Rect(800, 500, 400, 50),
                'active': False,
                'text': ''
            }
        ]
