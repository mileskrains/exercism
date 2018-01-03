class Clock(object):
    def __init__(self, hour, minute):
        self.minutes = ((hour % 24) * 60 + minute) % (24 * 60)
        self.resolve()

    def resolve(self):
        self.minute = self.minutes % 60
        self.hour = (self.minutes - self.minute) // 60

    def __add__(self, other):
        if type(other) == Clock:
            self.minutes += other.minutes
        elif type(other) == int:
            self.minutes += other
        self.minutes = self.minutes % (24 * 60)
        self.resolve()
        return self.__repr__()

    def __repr__(self):
        return f'{self.hour:0>2}:{self.minute:0>2}'

    def __eq__(self, other):
        return self.minutes == other.minutes

