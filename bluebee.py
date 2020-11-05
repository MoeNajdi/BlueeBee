import pygame


class BlueBee:
    """A class to manage BlueBee."""

    def __init__(self, bb_game):
        """Initializing BlueBee and set its starting position."""
        self.screen = bb_game.screen
        self.screen_rect = bb_game.screen.get_rect()
        self.settings = bb_game.settings

        # Load BlueBee's image and get its rect.
        self.image = pygame.image.load('images/bluebeeSmall.bmp')
        self.rect = self.image.get_rect()

        # Initiate BlueBee's starting position.
        self.rect.center = self.screen_rect.center

        # Store a decimal value for BlueBee's position.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw BlueBee on the screen."""
        self.screen.blit(self.image, self.rect)
