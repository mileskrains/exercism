class TriangleError(Exception):
    pass


class Triangle(object):
    def __init__(self, side_a, side_b, side_c):
        self.validate(side_a, side_b, side_c)
        self._a = side_a
        self._b = side_b
        self._c = side_c

    @staticmethod
    def validate(a, b, c):
        if min(a, b, c) <= 0 or max(a, b, c) >= sum([a, b, c]) - max(a, b, c):
            raise TriangleError

    def kind(self):
        uniq_to_kind = {1: 'equilateral', 2: 'isosceles', 3: 'scalene'}
        return uniq_to_kind[len({self._a, self._b, self._c})]
