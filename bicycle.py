class Bicycle:
    
    COMPASS = ['west', 'north', 'east', 'south']
    COUNT = 0

    def __init__(self, handlebars):
        # set attributes
        self.num_wheels = 2
        self.handlebars = handlebars

        # initial state

        # west = 0, north = 1, east = 2, south = 3
        self.direction = 1
        self.speed = 0

        Bicycle.COUNT +=1

    def brake(self):
        self.speed -= 1

    def pedal(self, intensity = 1):
        self.speed += intensity

    def steer(self, d):
        '''Turn clockwise (1) or counterclockwise (-1).
        
        A value of 0 leaves direction unchanged.
        '''

        self.direction += d


    def __repr__(self):
        heading = Bicycle.COMPASS[self.direction]
        return "Moving {0} at {1}mph.".format(heading, self.speed)
