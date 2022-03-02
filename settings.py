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

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 10
        self.bullet_height = 17
        self.bullet_color = (70, 70, 70)
