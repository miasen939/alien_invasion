class Settings():
    """a setting class of game alien invasion"""
    def __init__(self):
        """init game set"""
        #screen set
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #ship set
        self.ship_speed_factor = 0.75

        #bullet set
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3
