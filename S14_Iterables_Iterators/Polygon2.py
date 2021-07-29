import math
class Polygon2:
    def __init__(self, n, R):
        if n < 3:
            raise ValueError('Polygon must have at least 3 vertices.')
        self.edge = n  # Edges
        self.radius = R  # Circum-Radius

    def __repr__(self):
        return f'Polygon(n={self._n}, R={self._R})'

    @property
    def edge(self):
        return self._n

    @edge.setter
    def edge(self, n):
        self._n = n
        self._int_angle = None
        self._side_len = None
        self._apothem = None
        self._area = None
        self._perimeter = None

    @property
    def radius(self):
        return self._R

    @radius.setter
    def radius(self, R):
        self._R = R
        self._side_len = None
        self._apothem = None
        self._area = None
        self._perimeter = None

    @property
    def interior_angle(self):
        if self._int_angle is None:
            self._int_angle = (self._n - 2) * 180 / self._n
        return self._int_angle

    @property
    def side_length(self):
        if self._side_len is None:
            self._side_len = 2 * self._R * math.sin(math.pi / self._n)
        return self._side_len

    @property
    def apothem(self):
        if self._apothem is None:
            self._apothem = self._R * math.cos(math.pi / self._n)
        return self._apothem

    @property
    def area(self):
        if self._area is None:
            self._area = self._n / 2 * self.side_length * self.apothem
        return self._area

    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = self._n * self.side_length
        return self._perimeter

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self._n == other._n
                    and self._R == other._R)
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self._n > other._n
        else:
            return NotImplemented