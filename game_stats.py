class GameStats:
    """Tracking games stats"""

    def __init__(self, ai_game):

        self.settings = ai_game.settings
        self.reset_stats()
        #Stating game in inactive mode
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
