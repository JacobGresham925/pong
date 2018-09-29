import pygame.font


class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_settings, screen, stats):
        """Inintialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        # Font settings for scoring information.
        self.text_color1 = (255, 0, 0)
        self.text_color2 = (0, 0, 255)
        self.text_color3 = (0, 255, 0)
        self.font = pygame.font.SysFont(None, 48)

        # Initilize so can get green check
        self.score_image = 0
        self.score_rect = 0
        self.high_score_image = 0
        self.high_score_rect = 0
        self.level_image = 0
        self.level_rect = 0

        # Prepare the initial score images.
        self.prep_playerscore()
        self.prep_level()
        self.prep_aiscore()

    def prep_playerscore(self):
        """Turn the store into a rendered image."""
        rounded_score = int(round(self.stats.playerscore, 0))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color2,
                                            self.ai_settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.screen_rect.centerx - 20
        self.score_rect.top = self.screen_rect.top

    def prep_level(self):
        """Turn the high score into a rendered image."""
        high_score = int(round(self.stats.level, 0))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_color3, self.ai_settings.bg_color)

        # Cetner the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        # self.high_score_rect.top = self.score_rect.top + 20
        self.high_score_rect.centery += 40

    def prep_aiscore(self):
        """Turn the level into a rendered image."""
        self.level_image = self.font.render(str(self.stats.aiscore), True,
                                            self.text_color1, self.ai_settings.bg_color)

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.centerx = self.screen_rect.centerx + 20
        self.level_rect.top = self.screen_rect.top

    def show_score(self):
        """Draw score and ships to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
