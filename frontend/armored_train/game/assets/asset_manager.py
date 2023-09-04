import yaml


class AssetManager:
    def __init__(self, yaml_file_path):
        self.__yaml_file_path = yaml_file_path
        self.__assets = {}

    def load_assets(self):
        with open(self.__yaml_file_path, 'r') as file:
            self.__assets = yaml.load(file, Loader=yaml.FullLoader)

    def save_assets(self):
        with open(self.__yaml_file_path, 'w') as file:
            yaml.dump(self.__assets, file)

    def add_asset(self, asset_type, asset_name, asset_path):
        if asset_type not in self.__assets:
            self.__assets[asset_type] = {}
        self.__assets[asset_type][asset_name] = asset_path

    def get_asset_path(self, asset_type, asset_name):
        if asset_type in self.__assets and asset_name in self.__assets[asset_type]:
            return self.__assets[asset_type][asset_name]

    def remove_asset(self, asset_type, asset_name):
        if asset_type in self.__assets and asset_name in self.__assets[asset_type]:
            del self.__assets[asset_type][asset_name]


# asset_manager = AssetManager("assets.yaml")
# asset_manager.load_assets()
#
# new_assets = [{"type": 'images', "name": 'heavy_enemy',
#                "path": "C:\\Users\\user\\PycharmProjects\\Graduation_Project\\frontend\\armored_train\\game\\assets\\images\\heavy_enemy.png"},
#               {"type": 'images', "name": 'light_enemy',
#                "path": "C:\\Users\\user\\PycharmProjects\\Graduation_Project\\frontend\\armored_train\\game\\assets\\images\\light_enemy.png"},
#               {"type": 'images', "name": 'medium_enemy',
#                "path": "C:\\Users\\user\\PycharmProjects\\Graduation_Project\\frontend\\armored_train\\game\\assets\\images\\medium_enemy.png"}
#               ]
#
# for asset in new_assets:
#     asset_manager.add_asset(asset["type"], asset["name"], asset["path"])
#
# asset_manager.save_assets()
