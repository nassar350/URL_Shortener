class MemoryStorage:
    def __init__(self):
        self.storage = {}

    def save(self, short_url, long_url):
        self.storage[short_url] = long_url
    
    def get(self, short_url):
        return self.storage.get(short_url, "URL Not Found")

    def get_all(self):
        for key, value in self.storage.items():
            print(f"{key} -> {value}")