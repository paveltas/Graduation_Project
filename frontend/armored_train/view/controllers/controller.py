from abc import abstractmethod, ABC


class Controller(ABC):
    def __init__(self, model, screen, screen_manager):
        self.model = model
        self.screen = screen
        self.screen_manager = screen_manager

    @abstractmethod
    def handle_event(self, event):
        pass


