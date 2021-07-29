import Polygon2
from Polygon2 import Polygon2


class Polygons2:
    def __init__(self, m, R):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = R
        self._polygons = None

    def __len__(self):
        return self._m - 2  # To exclude sides=1 and sides=2 as they are not polygons

    def __repr__(self):
        return f'Polygons(m={self._m}, R={self._R})'

    def __iter__(self):
        return self.polyiterator(self)

    @property
    def max_efficiency_polygon(self):
        if self._polygons is None:
            self._polygons = [Polygon2(i, self._R) for i in range(3, self._m + 1)]
            self._polygons = sorted(self._polygons,
                                    key=lambda p: p.area / p.perimeter,
                                    reverse=True)
        return self._polygons[0]

    class polyiterator:
        def __init__(self, poly_obj):
            self._index = 3
            self.poly_obj = poly_obj

        def __iter__(self):
            return self

        def __next__(self):
            if self._index > self.poly_obj._m:
                raise StopIteration
            else:
                poly_ = Polygon2(self._index, self.poly_obj._R)
                result = f'Sides = {poly_.edge}, Radius = {poly_.radius}, Eff_ratio = {round((poly_.area / poly_.perimeter),2)}'
                self._index += 1
                return result