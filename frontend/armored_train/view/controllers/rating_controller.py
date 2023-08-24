import requests

from frontend.armored_train.view.controllers.controller import Controller


class RatingController(Controller):
    def __init__(self, model, screen, screen_manager):
        super().__init__(model, screen, screen_manager)

    def handle_event(self, event):
        if self.model.back_button_active:
            self.screen_manager.set_active_screen('Main Menu Screen')
        while self.model.count == 0:
            self.get_overall_score()
            self.model.count += 1

    def get_overall_score(self):
        response = requests.get('http://localhost:8000/score/')
        data = response.json()
        if data:
            self.get_users_overall_score(data)
            self.get_levels_score(data)

    def get_users_overall_score(self, data):
        dct = {}

        for el in data:
            dct[el['player_name']] = dct.get(el['player_name'], 0) + el['points']

        self.model.users_overall_score = [(i, k, v) for i, (k, v) in
                                          enumerate(sorted(dct.items(), key=lambda item: item[1], reverse=True),
                                                    start=1)]
        self.model.user_overall_score = dct[self.model.login]
        self.model.user_place = next((el[0] for el in self.model.users_overall_score if el[1] == self.model.login), 0)

    def get_levels_score(self, data):
        dct = {}

        for el in data:
            if el['level'] in dct:
                dct[el['level']][el['player_name']] = dct[el['level']].get(el['player_name'], el['points'])
            else:
                dct[el['level']] = {el['player_name']: el['points']}

        for k, v in dct.items():
            self.model.levels_score[k] = {k: (i, v) for i, (k, v) in
                                          enumerate(sorted(v.items(), key=lambda item: item[1], reverse=True), start=1)}
