class Settings():
    """Класс для хранения всех настроек."""

    def __init__(self):
        """Инициализировать статические настройки игры."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (5, 5, 31)

        # Ship settings.
        self.ship_limit = 3

        # Bullet settings.
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 250, 12, 12
        self.bullets_allowed = 3

        # Alien settings.
        self.fleet_drop_speed = 10

        # Speeds up.
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализировать настройки, которые меняются в течение игры."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        self.alien_points = 50

        self.fleet_direction = 1

    def increase_speed(self):
        """Увеличьте настройки скорости и значения очков пришельцев."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)