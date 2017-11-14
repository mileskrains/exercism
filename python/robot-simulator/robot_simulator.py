# Globals for the bearings
# Change the values as you see fit
EAST = (1, 0)
NORTH = (0, 1)
WEST = (-1, 0)
SOUTH = (0, -1)


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.coordinates = (x, y)
    
    def turn_left(self):
        self.bearing = {NORTH: WEST,
                        WEST: SOUTH,
                        SOUTH: EAST,
                        EAST: NORTH}[self.bearing]
    
    def turn_right(self):
        self.bearing = {NORTH: EAST,
                        EAST: SOUTH,
                        SOUTH: WEST,
                        WEST: NORTH}[self.bearing]
    
    def advance(self):
        self.coordinates = (self.coordinates[0] + self.bearing[0],
                            self.coordinates[1] + self.bearing[1])
    
    def simulate(self, sequence):
        for s in sequence:
            if s == 'L':
                self.turn_left()
            elif s == 'R':
                self.turn_right()
            elif s == 'A':
                self.advance()
