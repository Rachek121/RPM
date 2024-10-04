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


def main():
    # Получаем экземпляр ConfigCache (генерируем его, если его ещё нет)
    config_cache = ConfigCache.new()

    # Получаем конфигурационные значения
    db_host = config_cache.get('database')
    db_port = config_cache.get('port')
    db_user = config_cache.get('user')
    db_password = config_cache.get('password')

    # Печатаем загруженные конфигурации
    print("Database Host:", db_host)
    print("Database Port:", db_port)
    print("Database User:", db_user)
    print("Database Password:", db_password)

    # Пример изменения конфигурации
    config_cache.set('database', '127.0.0.1')
    new_db_host = config_cache.get('database')
    print("Updated Database Host:", new_db_host)

if __name__ == "__main__":
    main()