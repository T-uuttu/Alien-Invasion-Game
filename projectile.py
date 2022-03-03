import pygame
from pygame.sprite import Sprite


class Projectile(Sprite):
    """ Class to manage projectiles the ship fires. """

    def __init__(self, ai_game):
        """ Create a projectile object at the ship's current position. """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.projectile_color

        # Create a projectile rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.projectile_width,
                                self.settings.projectile_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the projectile's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """ Move the projectile up the screen. """
        # Update the decimal position of the projectile.
        self.y -= self.settings.projectile_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_projectile(self):
        """ Draw the projectile to the screen. """
        pygame.draw.rect(self.screen, self.color, self.rect)
