import requests

from frontend.armored_train.view.controllers.controller import Controller


class RatingController(Controller):
    def __init__(self, model, screen, screen_manager):
        super().__init__(model, screen, screen_manager)

    def handle_event(self, event):
        while self.model.count == 0:
            self.get_score()
            self.model.count += 1
        pass

    def get_score(self):
        response = requests.get('http://localhost:8000/score/1/')  # Replace with your API endpoint
        data = response.json()

        self.model.player = data['player_name']
        print(self.model.player, type(self.model.player))
        # self.model.level = data['level']
        # print(self.model.level)
        # self.model.points = data['points']
        # print(self.model.points)

        for el in data:
            print(el, data[el])