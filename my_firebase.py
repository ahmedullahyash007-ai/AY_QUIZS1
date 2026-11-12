import requests

class ValWrapper:
    def __init__(self, data):
        self._data = data
    def val(self):
        return self._data

class DBPath:
    def __init__(self, base_url, path=""):
        self.base_url = base_url
        self.path = path
    
    def child(self, name):
        new_path = f"{self.path}/{name}" if self.path else name
        return DBPath(self.base_url, new_path)
    
    def get(self):
        url = f"{self.base_url}/{self.path}.json"
        try:
            r = requests.get(url, timeout=10)
            return ValWrapper(r.json())
        except Exception as e:
            print(f"Firebase get error: {e}")
            return ValWrapper(None)

class MyFirebase:
    def __init__(self, config):
        self.db_url = config["databaseURL"].rstrip("/")
    
    def database(self):
        return DBPath(self.db_url)

def initialize_app(config):
    return MyFirebase(config)