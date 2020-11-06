import pygame


class FirePlace:
    """A class to create the fire place."""

    def __init__(self, bb_game):
        """Initializing the fireplace and its position."""

        self.screen = bb_game.screen
        self.screen_rect = bb_game.screen.get_rect()
        self.settings = bb_game.settings

        # Load the fireplace image and get its rect.
        self.image = pygame.image.load('images/fireplace1.bmp')
        self.rect = self.image.get_rect()

        # Initiate FirePlace's starting position.
        self.rect.top = self.screen_rect.top
        self.rect.left = self.screen_rect.left

    def blitme(self):
        """Draw FirePlace on the screen."""
        self.screen.blit(self.image, self.rect)
