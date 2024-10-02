class SecuritySystem:
    def activate(self):
        print("Охранная система активирована.")

    def deactivate(self):
        print("Охранная система деактивирована.")


class VideocamSystem:
    def start(self):
        print("Видеонаблюдение запущено.")

    def stop(self):
        print("Видеонаблюдение остановлено.")


class AccessControlSystem:
    def enable(self):
        print("Система контроля доступа включена.")

    def disable(self):
        print("Система контроля доступа выключена.")


class AlarmSystem:
    def trigger(self):
        print("Сигнализация активирована.")

    def reset(self):
        print("Сигнализация сброшена.")


class SecuritySystemFacade:
    def __init__(self):
        self.security_system = SecuritySystem()
        self.videocam_system = VideocamSystem()
        self.access_control_system = AccessControlSystem()
        self.alarm_system = AlarmSystem()

    def activate_all_systems(self):
        self.security_system.activate()
        self.videocam_system.start()
        self.access_control_system.enable()
        self.alarm_system.trigger()
        print("Все системы безопасности активированы.")

    def deactivate_all_systems(self):
        self.security_system.deactivate()
        self.videocam_system.stop()
        self.access_control_system.disable()
        self.alarm_system.reset()
        print("Все системы безопасности деактивированы.")


if __name__ == "__main__":
    facade = SecuritySystemFacade()
    facade.activate_all_systems()
    facade.deactivate_all_systems()
