import yaml


class URLManager:
    def __init__(self, yaml_file_path):
        self.__yaml_file_path = yaml_file_path
        self.__urls = {}

    def load_urls(self):
        with open(self.__yaml_file_path, 'r') as file:
            self.__urls = yaml.load(file, Loader=yaml.FullLoader)

    def save_urls(self):
        with open(self.__yaml_file_path, 'w') as file:
            yaml.dump(self.__urls, file)

    def add_url(self, url_name, url_path):
        self.__urls[url_name] = url_path

    def get_url_path(self, url_name):
        if url_name in self.__urls:
            return self.__urls[url_name]

    def remove_url(self, url_name):
        if url_name in self.__urls:
            del self.__urls[url_name]


url_manager = URLManager("urls_data.yaml")
url_manager.load_urls()

new_urls = [{'name': 'authorize', 'path': 'http://127.0.0.1:8000/auth/token/authorize/'},
            {'name': 'register', 'path': 'http://127.0.0.1:8000/auth/register/'},
            {'name': 'score', 'path': 'http://localhost:8000/score/'},
            {'name': 'users_rating', 'path': 'http://127.0.0.1:8000/users_rating/'},
            {'name': 'user_rating', 'path': 'http://127.0.0.1:8000/user_rating/'},
            ]

for url in new_urls:
    url_manager.add_url(url["name"], url["path"])

url_manager.save_urls()
