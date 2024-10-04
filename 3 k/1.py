class ConfigCache:
    _instance = None

    @classmethod
    def new(cls):
        if cls._instance is None:
            cls._instance = cls()
            cls._instance._load_config_cache()
        return cls._instance

    def _load_config_cache(self):
        self._config_cache = {}
        config_file = 'config.txt'
        try:
            with open(config_file) as config_cache:
                for line in config_cache:
                    key, value = line.strip().split('=', 1)
                    self._config_cache[key] = value
        except FileNotFoundError:
            pass # Файл не найден скипаем

    def get(self, key):
        return self._config_cache.get(key)

    def set(self, key, value):
        self._config_cache[key] = value