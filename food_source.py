import pygame


class FoodSource:
    """A class to create the food source."""

    def __init__(self, bb_game):
        """Initializing the food source and its position."""

        self.screen = bb_game.screen
        self.screen_rect = bb_game.screen.get_rect()
        self.settings = bb_game.settings

        # Load the food source image and get its rect.
        self.image = pygame.image.load('images/foodsource1.bmp')
        self.rect = self.image.get_rect()

        # Initiate foodSource's starting position.
        self.rect.top = self.screen_rect.top
        self.rect.right = self.screen_rect.right

    def blitme(self):
        """Draw FoodSource on the screen."""
        self.screen.blit(self.image, self.rect)
