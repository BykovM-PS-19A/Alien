class GameStats():
    """Статистика отслеживания пришельцев."""

    def __init__(self, ai_settings):
        """Инициализация статистики."""
        self.ai_settings = ai_settings
        self.reset_stats()

        self.game_active = False

        self.high_score = 0

    def reset_stats(self):
        """Инициализация статистики, которая может меняться во время игры."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1