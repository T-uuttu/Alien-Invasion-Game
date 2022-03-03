class Settings():
    """ A class to store all settings for Alien Invasion Part Deux. """

    def __init__(self):
        """ Initialize the game's settings. """
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 85, 255)

        # Ship settings
        self.ship_speed = 1.5

        # Projectile settings
        self.projectile_speed = 1.0
        self.projectile_width = 10
        self.projectile_height = 17
        self.projectile_color = (70, 70, 70)
