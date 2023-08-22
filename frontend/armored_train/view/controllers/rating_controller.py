import requests

from frontend.armored_train.view.controllers.controller import Controller


class RatingController(Controller):
    def __init__(self, model, screen, screen_manager):
        super().__init__(model, screen, screen_manager)
        self.data = None

    def handle_event(self, event):
        while self.model.count == 0:
            self.get_overall_score()
            self.model.count += 1
        pass

    def get_overall_score(self):
        response = requests.get('http://localhost:8000/score/')
        self.data = response.json()
        self.get_users_overall_score()

    def get_users_overall_score(self):
        dct = {}

        if self.data:
            for el in self.data:
                dct[el['player_name']] = dct.get(el['player_name'], 0) + el['points']

        self.model.users_overall_score = [(i, k, v) for i, (k, v) in
                                          enumerate(sorted(dct.items(), key=lambda item: item[1], reverse=True),
                                                    start=1)]
        self.model.user_overall_score = dct[self.model.login]
        self.model.user_place = next((el[0] for el in self.model.users_overall_score if el[1] == self.model.login), 0)
        print(self.model.users_overall_score)
