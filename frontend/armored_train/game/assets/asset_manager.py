import json


class AssetManager:
    def __init__(self, json_file_path):
        self.__json_file_path = json_file_path
        self.__assets = {}

    def load_assets(self):
        with open(self.__json_file_path, 'r') as file:
            self.__assets = json.load(file)

    def save_assets(self):
        with open(self.__json_file_path, 'w') as file:
            json.dump(self.__assets, file)

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


asset_manager = AssetManager("assets.json")
asset_manager.load_assets()

new_assets = [

]


for asset in new_assets:
    asset_manager.add_asset(asset["type"], asset["name"], asset["path"])


asset_manager.save_assets()
