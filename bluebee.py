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
        #print(self.x)
        self.y = float(self.rect.y)
        #print(self.y)
        # Movement flags.
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update_movement(self):
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.bb_speed
            #print("left : ",self.x)
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.bb_speed
            #print("right : ", self.x)
        self.rect.x = self.x

        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.bb_speed
            #print("up : ", self.y)
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.bb_speed
            #print("down : ", self.y)
        self.rect.y = self.y

    def blitme(self):
        """Draw BlueBee on the screen."""
        self.screen.blit(self.image, self.rect)
