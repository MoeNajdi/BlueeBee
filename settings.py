class Settings:
    """A class to store all settings for BlueBee Experiment"""
    def __init__(self):
        """Initializing the game's settings."""

        # Screen's settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Bluebee Settings
        self.bb_speed = 1.0