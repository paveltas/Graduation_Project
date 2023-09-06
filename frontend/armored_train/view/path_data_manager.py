import yaml


class PathManager:
    def __init__(self, yaml_file_path):
        self.__yaml_file_path = yaml_file_path
        self.__paths = {}

    def load_paths(self):
        with open(self.__yaml_file_path, 'r') as file:
            self.__paths = yaml.load(file, Loader=yaml.FullLoader)

    def save_paths(self):
        with open(self.__yaml_file_path, 'w') as file:
            yaml.dump(self.__paths, file)

    def add_path(self, path_name, path_path):
        self.__paths[path_name] = path_path

    def get_path(self, path_name):
        if path_name in self.__paths:
            return self.__paths[path_name]

    def remove_path(self, path_name):
        if path_name in self.__paths:
            del self.__paths[path_name]


path_manager = PathManager("paths_data.yaml")
path_manager.load_paths()

new_paths = [{'name': 'config.yaml',
              'path': "C:\\Users\\Admin\\PycharmProjects\\Graduation_Project\\backend\\armored_train\\armored_train\\config.yaml"},
             ]

for path in new_paths:
    path_manager.add_path(path["name"], path["path"])

path_manager.save_paths()
