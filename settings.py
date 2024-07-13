class Settings:
    """This where all setting of alien invasion is"""
    def __init__(self):
        #Screen settings
        self.screen_width = 0
        self.screen_height = 0
        #background color
        self.bg_color = (230,230,230)

        #ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3
        self.ship_speed1 = 1

        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)

        #Alien speeed
        self.alien_speed = 0.5
        self.fleet_drop_speed = 8
        #fleet direction of 1 repersent right, -1 left
        self.fleet_direction = 1