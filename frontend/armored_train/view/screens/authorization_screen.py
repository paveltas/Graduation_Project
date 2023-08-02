import pygame

from frontend.armored_train.view.models.authorization_model import AuthorizationModel
from frontend.armored_train.view.screens.screen import Screen
from frontend.armored_train.view.widgets.button_widget import ButtonWidget
from frontend.armored_train.view.widgets.input_text_widget import InputTextWidget
from frontend.armored_train.view.widgets.widget_utils import WidgetUtils


class AuthorizationScreen(Screen):
    def __init__(self, width: int, height: int, caption: str, model):
        super().__init__(width, height, caption)
        self.model = model
        self.background = pygame.image.load('../../game/assets/images/background.jpg').convert()
        self.font_title = pygame.font.Font("../../game/assets/fonts/Oswald-Light.ttf", 72)
        self.font_label = pygame.font.Font("../../game/assets/fonts/Oswald-Light.ttf", 36)
        self.font_input = pygame.font.Font("../../game/assets/fonts/Oswald-Light.ttf", 36)
        self.WHITE = (255, 255, 255)

        self.center_x = WidgetUtils(self.width, 0)
        self.authorization_input = InputTextWidget(800, 400, 400, 50, self.screen)
        self.authorization_button = ButtonWidget(800, 900, 200, 50, self.screen)

    def draw(self):
        self.screen.blit(self.background, (0, 0))

        title_text = self.font_title.render("Авторизация", True, self.WHITE)
        self.screen.blit(title_text, (self.center_x.center_on_x_and_y(title_text), 100))

        username_label = self.font_label.render("Почта:", True, self.WHITE)
        password_label = self.font_label.render("Пароль:", True, self.WHITE)
        self.screen.blit(username_label, (600, 400))
        self.screen.blit(password_label, (600, 500))

        self.authorization_input.x = self.center_x.center_on_x_and_y(self.authorization_input)
        self.authorization_input.color = (130, 130, 130)
        self.authorization_input.draw()

        self.authorization_button.x = self.center_x.center_on_x_and_y(self.authorization_button)
        self.authorization_button.color = (130, 130, 130)
        self.authorization_button.text_font = self.font_input
        self.authorization_button.caption = 'Вход'
        self.authorization_button.draw()

        pygame.display.flip()


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.model.auth_button_rect = pygame.Rect(800, 600, 200, 50)
        self.model.auth_button_active = False
        self.running = True

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if event.button == 1:
                for box in self.model.input_boxes:
                    if box['rect'].collidepoint(mouse_pos):
                        box['active'] = True
                        self.model.active_input_box = box
                    else:
                        box['active'] = False
                        self.model.active_input_box = None
                if self.model.auth_button_rect.collidepoint(mouse_pos):
                    self.model.username = self.model.input_boxes[0]['text']
                    self.model.password = self.model.input_boxes[1]['text']
                    self.model.input_boxes[0]['text'] = ''
                    self.model.input_boxes[1]['text'] = ''
        elif event.type == pygame.KEYDOWN:
            if self.model.active_input_box:
                if event.key == pygame.K_RETURN:
                    self.model.active_input_box['text'] = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.model.active_input_box['text'] = self.model.active_input_box['text'][:-1]
                elif len(self.model.active_input_box['text']) < 20:
                    self.model.active_input_box['text'] += event.unicode

    def run(self):
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)

            self.view.draw()

        pygame.quit()


model = AuthorizationModel()
authorization_screen = AuthorizationScreen(1920, 1080, 'Authorization Screen', model)
controller = Controller(model, authorization_screen)
controller.run()
