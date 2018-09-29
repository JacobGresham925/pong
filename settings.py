class Settings:
    """A class to store all settings for pong."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Paddle settings
        self.paddle_width = 20
        self.paddle_height = 130
        self.paddle_color1 = 0, 0, 255
        self.paddle_color2 = 255, 0, 0
        self.paddle_speed_factor = 2.0
        self.ai_speed_factor = 0.8

        # Ball settings
        self.ball_color = 255, 255, 255
        self.ball_size = 10
        self.ball_limit = 5

        # Divider settings
        self.divider_color = 255, 255, 255
        self.divider_width = 2
        self.divider_height = 800

        # Scores
        self.aiscore = 0
        self.playerscore = 0

        self.game_active = False
