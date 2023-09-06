import json
import os
import threading
import time

import requests
import yaml

from frontend.armored_train.view.controllers.controller import Controller


class RatingController(Controller):
    def __init__(self, model, screen, screen_manager):
        super().__init__(model, screen, screen_manager)

    def handle_event(self, event):
        if self.model.back_button_active:
            self.screen_manager.set_active_screen('Main Menu Screen')

        def repeated_tasks():
            self.get_users_overall_score()
            self.get_user_overall_score()
            self.get_levels_score()
            time.sleep(10)

        thread = threading.Thread(target=repeated_tasks)
        thread.start()

    def get_user_overall_score(self):
        with open(self.path_data_manager.get_path('config.yaml')) as config_file:
            config_data = yaml.load(config_file, Loader=yaml.FullLoader)

        url = self.url_data_manager.get_url_path('user_rating')
        headers = {
            'Authorization': f'Token {config_data["authorization_token"]}'
        }

        response = requests.get(url, headers=headers)

        try:
            response_json = response.json()
            print("Данные являются валидным JSON. user")
            self.model.login = response_json['player_username']
            self.model.user_place = response_json['place']
            self.model.user_overall_score = response_json['total_points']
        except json.JSONDecodeError as e:
            print("Данные не являются валидным JSON. user")
            print(f"Ошибка: {e}")

    def get_users_overall_score(self):
        response = requests.get(self.url_data_manager.get_url_path('users_rating'))

        try:
            response_json = response.json()
            print("Данные являются валидным JSON. users")
            self.model.users_overall_score = response_json
        except json.JSONDecodeError as e:
            print("Данные не являются валидным JSON. users")
            print(f"Ошибка: {e}")

    def get_levels_score(self):
        response = requests.get(self.url_data_manager.get_url_path('score'))
        data = response.json()

        dct = {}

        for el in data:
            if el['level'] in dct:
                dct[el['level']][el['player_name']] = dct[el['level']].get(el['player_name'], el['points'])
            else:
                dct[el['level']] = {el['player_name']: el['points']}

        for k, v in dct.items():
            self.model.levels_score[k] = {k: (i, v) for i, (k, v) in
                                          enumerate(sorted(v.items(), key=lambda item: item[1], reverse=True),
                                                    start=1)}
