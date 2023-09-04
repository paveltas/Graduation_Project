import pygame

from frontend.armored_train.view.widgets.widget import Widget


class TextBoxWidget(Widget):
    def __init__(self, x, y, width, height, screen, text, font_color=None, center_x=False,
                 center_y=False):
        super().__init__(x, y, width, height, screen, text)
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
    def __init__(self, x, y, width, height, screen, model, text=None, center_x=False, center_y=False):
        super().__init__(x, y, width, height, screen, text)
        self.__model = model
        self.center_x = center_x
        self.center_y = center_y

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height), self.border_width)

        title = self.text_font.render('Ваш рейтинг', True, self.font_color)
        username = self.text_font.render(self.__model.login, True, self.font_color)
        place = self.text_font.render(f'Ваше место в рейтинге - {self.__model.user_place}', True, self.font_color)
        score = self.text_font.render(f'Общее количество ваших очков - {self.__model.user_overall_score}', True,
                                      self.font_color)
        self.screen.blit(title, (self.align((self.width, self.height), title)))
        self.screen.blit(username, (self.align((self.width, self.height), username)[0], self.y + 50))
        self.screen.blit(place, (self.align((self.width, self.height), place)[0], self.y + 100))
        self.screen.blit(score, (self.align((self.width, self.height), score)[0], self.y + 150))


class GeneralOverallRatingTextWidget(TextBoxWidget):
    def __init__(self, x, y, width, height, screen, model, text=None, center_x=False, center_y=False):
        super().__init__(x, y, width, height, screen, text)
        self.__main_rect = None
        self.__model = model
        self.__scroll_position = 0
        self.__items_size = 50
        self.__items_per_screen = self.height // self.__items_size
        self.center_x = center_x
        self.center_y = center_y

    def draw(self):
        self.__main_rect = pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height),
                                            self.border_width)

        start_index = self.__scroll_position // self.__items_size
        end_index = start_index + self.__items_per_screen

        if self.__model.users_overall_score:
            visible_items = self.__model.users_overall_score[start_index:end_index]

            for i, item in enumerate(visible_items):
                item_text = self.text_font.render(f'{item[0]} место {item[2]:>42} очков  {item[1]:>45}', True,
                                                  self.font_color)
                item_x = self.x + 10
                item_y = self.y + (i * self.__items_size)
                self.screen.blit(item_text, (item_x, item_y))

            self.__handle_event()

    def __handle_event(self):
        can_scroll_up = self.__scroll_position != 0
        can_scroll_down = self.__scroll_position != (
                len(self.__model.users_overall_score) - self.__items_per_screen) * self.__items_size

        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            if self.__main_rect.collidepoint(mouse_pos):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4 and can_scroll_up:
                        self.__scroll_position -= self.__items_size
                    elif event.button == 5 and can_scroll_down:
                        if len(self.__model.users_overall_score) > self.__items_per_screen:
                            self.__scroll_position += self.__items_size


class LevelsRatingTextWidget(TextBoxWidget):
    def __init__(self, x, y, width, height, screen, model, text=None, center_x=False, center_y=False):
        super().__init__(x, y, width, height, screen, text)
        self.__main_rect = None
        self.__login = model.login
        self.__levels_score = model.levels_score
        self.__scroll_position = 0
        self.__items_size = 180
        self.__items_per_screen = self.height // self.__items_size
        self.center_x = center_x
        self.center_y = center_y

    def draw(self):
        self.__main_rect = pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height),
                                            self.border_width)
        if self.__levels_score:
            start_key = self.__scroll_position // self.__items_size
            end_key = start_key + self.__items_per_screen if self.__items_per_screen < len(
                self.__levels_score) else len(
                self.__levels_score)

            count = 0
            for key in range(start_key + 1, end_key + 1):
                for login, value in self.__levels_score[key].items():
                    if value[0] == 1:  # находим игрока на 1 месте.
                        item_text_level = self.text_font.render(f'Уровень {key}', True, self.font_color)
                        item_text_user_place = self.text_font.render(
                            f'Вы заняли {self.__levels_score[key][self.__login][0]} место', True, self.font_color)
                        item_text_user_score = self.text_font.render(
                            f'И набрали {self.__levels_score[key][self.__login][1]} очков', True, self.font_color)
                        item_text_user_best_score = self.text_font.render(
                            f'Лучший счет  составляет {value[1]} очков. Его достиг игрок - {login}', True,
                            self.font_color)
                        item_y = self.y + (count * self.__items_size)

                        pygame.draw.rect(self.screen, self.color, (self.x + 10, item_y + 15, self.width - 20, 175),
                                         self.border_width)
                        self.screen.blit(item_text_level,
                                         (self.align((self.width, self.height), item_text_level)[0], item_y + 10))
                        self.screen.blit(item_text_user_place,
                                         (self.align((self.width, self.height), item_text_user_place)[0], item_y + 55))
                        self.screen.blit(item_text_user_score,
                                         (self.align((self.width, self.height), item_text_user_score)[0], item_y + 95))
                        self.screen.blit(item_text_user_best_score, (
                            self.align((self.width, self.height), item_text_user_best_score)[0], item_y + 135))
                        count += 1

            self.__handle_event()

    def __handle_event(self):
        can_scroll_up = self.__scroll_position != 0
        can_scroll_down = self.__scroll_position != (
                len(self.__levels_score) - self.__items_per_screen) * self.__items_size

        events = pygame.event.get()
        for event in events:
            mouse_pos = pygame.mouse.get_pos()
            if self.__main_rect.collidepoint(mouse_pos):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4 and can_scroll_up:
                        self.__scroll_position -= self.__items_size
                    elif event.button == 5 and can_scroll_down:
                        if len(self.__levels_score) > self.__items_per_screen:
                            self.__scroll_position += self.__items_size
