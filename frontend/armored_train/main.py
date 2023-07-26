import pygame


class Model:
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


class View:
    def __init__(self, model):
        pygame.init()
        self.model = model
        self.screen = pygame.display.set_mode((1920, 1080))
        self.font_title = pygame.font.Font("game/assets/fonts/Oswald-Light.ttf", 72)
        self.font_label = pygame.font.Font("game/assets/fonts/Oswald-Light.ttf", 36)
        self.font_input = pygame.font.Font("game/assets/fonts/Oswald-Light.ttf", 36)
        self.WHITE = (255, 255, 255)
        self.background_image = pygame.image.load("game/assets/images/background.jpg").convert()

    def render(self):
        self.screen.blit(self.background_image, (0, 0))

        title_text = self.font_title.render("Авторизация", True, self.WHITE)
        self.screen.blit(title_text, (750, 100))

        username_label = self.font_label.render("Username:", True, self.WHITE)
        password_label = self.font_label.render("Password:", True, self.WHITE)
        self.screen.blit(username_label, (600, 400))
        self.screen.blit(password_label, (600, 500))

        for box in self.model.input_boxes:
            color = (255, 0, 0) if box['active'] else (0, 0, 0)
            pygame.draw.rect(self.screen, color, box['rect'], 2)

        username_input = self.font_input.render(self.model.input_boxes[0]['text'], True, self.WHITE)
        password_input = self.font_input.render("*" * len(self.model.input_boxes[1]['text']), True, self.WHITE)
        self.screen.blit(username_input, (800, 400))
        self.screen.blit(password_input, (800, 500))

        auth_button_color = (255, 0, 0) if self.model.auth_button_active else (0, 0, 0)
        pygame.draw.rect(self.screen, auth_button_color, self.model.auth_button_rect, 2)
        auth_button_text = self.font_label.render("Авторизация", True, self.WHITE)
        self.screen.blit(auth_button_text, (810, 610))

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

            self.view.render()

        pygame.quit()


model = Model()
view = View(model)
controller = Controller(model, view)
controller.run()
