import pygame


class WaterSource:
    """A class to create the water source."""

    def __init__(self, bb_game):
        """Initializing the water source and its position."""

        self.screen = bb_game.screen
        self.screen_rect = bb_game.screen.get_rect()
        self.settings = bb_game.settings

        # Load the water source image and get its rect.
        self.image = pygame.image.load('images/watersource.bmp')
        self.rect = self.image.get_rect()

        # Initiate WaterSource's starting position.
        self.rect.bottom = self.screen_rect.bottom
        self.rect.left = self.screen_rect.left

    def blitme(self):
        """Draw WaterSource on the screen."""
        self.screen.blit(self.image, self.rect)
