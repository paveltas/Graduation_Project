import json

import pygame
import requests

from frontend.armored_train.view.controllers.controller import Controller


class AuthorizationController(Controller):
    def __init__(self, model, screen, screen_manager):
        super().__init__(model, screen, screen_manager)

    def authorize(self):
        url = self.url_data_manager.get_url_path('authorize')
        if self.model.reg_button_active:
            url = self.url_data_manager.get_url_path('register')

        data = {
            'username': self.model.input_fields['login'],
            'password': self.model.input_fields['password']
        }

        if data['username'] and data['password']:
            headers = {'Content-type': 'application/json'}
            response = requests.post(url, data=json.dumps(data), headers=headers)

            if response.status_code == 200:
                self.model.token = response.json().get('token')
                print(f'Успешная авторизация. Токен: {self.model.token}')
                self.screen.warning_text.text = f'Успешная авторизация. Токен: {self.model.token}'
                self.screen_manager.set_active_screen('Main Menu Screen')
            if response.status_code == 401:
                self.screen.warning_text.text = 'Пожалуйста проверьте введенные данные или пройдите регистрацию.'
            if response.status_code == 201:
                print("Регистрация прошла успешно")
                self.screen.warning_text.text = 'Регистрация прошла успешно.'
                self.screen_manager.set_active_screen('Main Menu Screen')
            if response.status_code == 409:
                print("Произошла ошибка при регистрации")
                self.screen.warning_text.text = 'Пользователь с такими данными уже есть.'
        else:
            self.screen.warning_text.text = 'Пожалуйста заполните оба поля.'

        self.model.input_fields['login'] = ''
        self.model.input_fields['password'] = ''

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if self.model.active_box:
                if event.key == pygame.K_RETURN:
                    self.authorize()
                elif event.key == pygame.K_BACKSPACE:
                    self.model.input_fields[self.model.active_box] = self.model.input_fields[self.model.active_box][:-1]
                elif len(self.model.input_fields[self.model.active_box]) < 20:
                    self.model.input_fields[self.model.active_box] += event.unicode

        if self.model.auth_button_active or self.model.reg_button_active:
            self.authorize()
