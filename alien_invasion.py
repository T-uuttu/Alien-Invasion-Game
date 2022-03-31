import sys
import pygame

from settings import Settings
from ship import Ship
from projectile import Projectile
from ufo import Ufo


class AlienInvasion():
    """ Overall class to manage game assets and behaviour. """

    def __init__(self):
        """ Initialize the game and create game resources. """
        pygame.init()
        self.settings = Settings()

        # Left in Fullscreen mode code in comments, just in case.
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        #self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Alien Invasion Part XYZ")

        self.ship = Ship(self)
        self.projectiles = pygame.sprite.Group()
        self.ufos = pygame.sprite.Group()

        self._create_fleet()

        # Set the background color.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """ Start the main loop for the game. """
        while True:
            self._check_events()
            self.ship.update()
            self._update_projectiles()
            self._update_screen()

            # Get rid of projectiles that have flown outside of view.
            for projectile in self.projectiles.copy():
                if projectile.rect.bottom <= 0:
                    self.projectiles.remove(projectile)

    def _check_events(self):
        """ Respond to keypresses and mouse events. """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """ Respond to keypresses. """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_projectile()

    def _check_keyup_events(self, event):
        """ Respond to key releases. """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_projectile(self):
        """ Create a new projectile and add it to the projectiles group. """
        if len(self.projectiles) < self.settings.projectiles_allowed:
            new_projectile = Projectile(self)
            self.projectiles.add(new_projectile)

    def _update_projectiles(self):
        """ Update position of projectiles and get rid of old projectiles. """
        # Update bullet positions.
        self.projectiles.update()

        # Get rid of projectiles that have disappeared.
        for projectile in self.projectiles.copy():
            if projectile.rect.bottom <= 0:
                self.projectiles.remove(projectile)

    def _update_screen(self):
        """ Update images on the screen, and flip to the new screen. """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for projectile in self.projectiles.sprites():
            projectile.draw_projectile()
        self.ufos.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _create_fleet(self):
        """ Create a fleet of UFOs. """
        # Make an UFO and find the number of UFOs in a row.
        # Spacing between each UFO is equal to one UFO width.
        ufo = Ufo(self)
        self.ufos.add(ufo)
        ufo_width, ufo_height = ufo.rect.size
        x_space_available = self.settings.screen_width - (2 * ufo_width)
        number_ufos_x = x_space_available // (2 * ufo_width)

        # Determine the number of rows of UFOs that fit on the screen.
        ship_height = self.ship.rect.height
        y_space_available = (self.settings.screen_height -
                             (3 * ufo_height) - ship_height)
        number_of_rows = y_space_available // (2 * ufo_height)

        # Create full fleet of UFOs.
        for row_number in range(number_of_rows):
            for ufo_number in range(number_ufos_x):
                self._create_ufo(ufo_number, row_number)

            self._create_ufo(ufo_number, ufo_number)

    def _create_ufo(self, ufo_number, number_of_rows):
        """ Create an UFO and place it in the row. """
        ufo = Ufo(self)
        ufo_width, ufo_height = ufo.rect.size
        ufo.x = ufo_width + 2 * ufo_width * ufo_number
        ufo.rect.x = ufo.x
        ufo.rect.y = ufo.rect.height + 2 * ufo.rect.height * number_of_rows
        self.ufos.add(ufo)


if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
