import pygame
from pygame.sprite import Sprite


class Ufo(Sprite):
    """ A class to represent a single UFO in the fleet. """

    def __init__(self, ai_game):
        """ Initialize the UFO and set its starting position. """
        super().__init__()
        self.screen = ai_game.screen

        # Load the UFO image and set its rect attribute.
        self.image = pygame.image.load("images/ufo.bmp")
        self.rect = self.image.get_rect()

        """ Start each new UFO near the top left of the screen. """
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the UFO's exact horizontal position.
        self.x = float(self.rect.x)
