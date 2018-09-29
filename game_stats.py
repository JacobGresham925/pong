class GameStats:
    """Track statistics for pong."""

    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Start Alien Invasion in an inactive state.
        self.game_active = False
        # High score should never be reset.
        self.high_score = 0
        self.winner = ""
        self.balls_left = self.ai_settings.ball_limit
        self.playerscore = 0
        self.aiscore = 0
        self.level = 7

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.balls_left = self.ai_settings.ball_limit
        self.playerscore = 0
        self.aiscore = 0
        self.level = 7
