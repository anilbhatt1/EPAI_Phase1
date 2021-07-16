import math

class polygon:
    def __init__(self, num_edges: int, circumrad: float):
        '''
        Accepts 2 parameters - Number of edges(n) and Circumradius(R)
        Derives below properties:
        int_angle -> (n−2) * 180 * n
        edge_len  -> s = 2 * R * sin(π/n)
        apothem   -> a = R * cos(π * n)
        area      -> 12 * n * s * a
        perimeter -> n * s
        '''
        if isinstance(num_edges, int) and num_edges >= 3:
            self.n = num_edges
        else:
            raise ValueError('Number of edges must be integer')

        if isinstance(circumrad, (int, float)) and circumrad > 0:
            self.R = circumrad
        else:
            raise ValueError('Circumradius must be a +ve float or integer')

    def __repr__(self):
        '''
        repr function for polygon class. Will give info on
        No: of edges(n), Circumradius(R)
        '''
        s1 = 'Regular Polygon class having '
        s2 = f'{self.n} sides, circumradius = {self.R}'
        return s1+s2

    def __eq__(self, oth_poly):
        '''
        Checks whether a given polygon object is equal or not based on no:of edges and circumradius(R)
        '''
        return self.n == oth_poly.n and self.R == oth_poly.R

    def __gt__(self, oth_poly):
        '''
        Checks whether a given polygon object is greater than or not based on no:of edges
        '''
        return self.n > oth_poly.n

    @property
    def int_angle(self) -> float:
        '''
        int_angle -> (n−2) * 180 * n
        '''
        return (self.n - 2) * 180 / (self.n)

    @property
    def edge_len(self) -> float:
        '''
        s = 2 * R * sin(π/n)
        '''
        return 2 * self.R * math.sin(math.pi / self.n)

    @property
    def apothem(self) -> float:
        '''
        a = R * cos(π * n)
        '''
        return self.R * math.cos(math.pi / self.n)

    @property
    def area(self) -> float:
        '''
        12 * n * s * a
        '''
        return 0.5 * self.n * self.edge_len * self.apothem

    @property
    def perimeter(self) -> float:
        '''
        n * s
        '''
        return self.n * self.edge_len