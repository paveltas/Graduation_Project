from abc import abstractmethod, ABC

from frontend.armored_train.view.path_data_manager import PathManager
from frontend.armored_train.view.url_data_manager import URLManager


class Controller(ABC):
    url_data_manager = URLManager("urls_data.yaml")
    url_data_manager.load_urls()

    path_data_manager = PathManager("paths_data.yaml")
    path_data_manager.load_paths()

    def __init__(self, model, screen, screen_manager, url_data_manager=url_data_manager,
                 path_data_manager=path_data_manager):
        self.model = model
        self.screen = screen
        self.screen_manager = screen_manager
        self.url_data_manager = url_data_manager
        self.path_data_manager = path_data_manager

    @abstractmethod
    def handle_event(self, event):
        pass
