class Settings():
    """ A class to store all settings for Alien Invasion Part Deux. """

    def __init__(self):
        """ Initialize the game's settings. """
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 85, 255)

        # Ship settings
        self.ship_speed = 1.2

        # Projectile settings
        self.projectile_speed = 0.5
        self.projectile_width = 10
        self.projectile_height = 19
        self.projectile_color = (211, 92, 2)
        self.projectiles_allowed = 3
