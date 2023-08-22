import pygame

from frontend.armored_train.view.widgets.widget import Widget


class TextBoxWidget(Widget):
    def __init__(self, x, y, width, height, screen, asset_manager, text, font_color=None, center_x=False,
                 center_y=False):
        super().__init__(x, y, width, height, screen, asset_manager, text)
        if font_color is not None:
            self.font_color = font_color
        self.center_x = center_x
        self.center_y = center_y

    def align(self, surface, text_on_screen):
        if isinstance(surface, tuple):
            proportions = surface
        else:
            proportions = surface.get_width(), surface.get_height()
        if self.center_x:
            x_pos = self.x + (proportions[0] - text_on_screen.get_width()) // 2
        else:
            x_pos = self.x

        if self.center_y:
            y_pos = self.y + (proportions[1] - text_on_screen.get_height()) // 2
        else:
            y_pos = self.y
        return x_pos, y_pos

    def draw(self):
        text_on_screen = self.text_font.render(self.text, True, self.font_color)

        self.screen.blit(text_on_screen, (self.align(self.screen, text_on_screen)))


class PersonalOverallRatingTextWidget(TextBoxWidget):
    def __init__(self, x, y, width, height, screen, model, asset_manager, text=None, center_x=False, center_y=False):
        super().__init__(x, y, width, height, screen, asset_manager, text)
        self.model = model
        self.center_x = center_x
        self.center_y = center_y

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height), self.border_width)

        title = self.text_font.render('Ваш рейтинг', True, self.font_color)
        username = self.text_font.render(self.model.login, True, self.font_color)
        place = self.text_font.render(f'Ваше место в рейтинге - {self.model.user_place}', True, self.font_color)
        score = self.text_font.render(f'Общее количество ваших очков - {self.model.user_overall_score}', True,
                                      self.font_color)
        self.screen.blit(title, (self.align((self.width, self.height), title)))
        self.screen.blit(username, (self.align((self.width, self.height), username)[0], self.y + 50))
        self.screen.blit(place, (self.align((self.width, self.height), place)[0], self.y + 100))
        self.screen.blit(score, (self.align((self.width, self.height), score)[0], self.y + 150))


class GeneralOverallRatingTextWidget(TextBoxWidget):
    def __init__(self, x, y, width, height, screen, model, asset_manager, text=None, center_x=False, center_y=False):
        super().__init__(x, y, width, height, screen, asset_manager, text)
        self.model = model
        self.center_x = center_x
        self.center_y = center_y
        self.scroll_position = 0
        self.items_size = 50
        self.items_per_screen = self.height // self.items_size

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height), self.border_width)

        start_index = self.scroll_position // self.items_size
        end_index = start_index + self.items_per_screen

        if self.model.users_overall_score:
            visible_items = self.model.users_overall_score[start_index:end_index]

            for i, item in enumerate(visible_items):
                item_text = self.text_font.render(f'{item[0]} место {item[2]:>42} очков  {item[1]:>45}', True,
                                                  self.font_color)
                item_x = self.x + 10
                item_y = self.y + (i * self.items_size)
                self.screen.blit(item_text, (item_x, item_y))

            self.handle_event()

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                if self.scroll_position != 0:
                    self.scroll_position -= self.items_size
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                if self.scroll_position != (
                        len(self.model.users_overall_score) - self.items_per_screen) * self.items_size:
                    if self.items_per_screen < len(self.model.users_overall_score):
                        self.scroll_position += self.items_size
