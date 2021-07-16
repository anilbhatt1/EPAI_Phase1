from polygon import polygon
from functools import lru_cache

class poly_seq:
    '''
    This is a ploygon sequence class that can accept:
        - number of vertices for largest polygon in the sequence
        - common circumradius for all polygons
    '''

    def __init__(self, edges: int, radius: 'int or float') -> None:
        '''
        Initializer method
        self.edges -> Input
        self.R     -> Input
        self.eff_ratio -> Will get populated while calling max_efficient()
        '''
        if isinstance(edges, int) and edges > 0:
            self.edges = edges
        else:
            raise ValueError('Number of vertices for largest polygon in the sequence must be integer > 0')

        if isinstance(radius, (int, float)) and radius > 0:
            self.R = radius
        else:
            raise ValueError('Common Circumradius must be float or integer > 0')

        self.eff_ratio = {}

    def __repr__(self):
        '''
        repr function for poly_seq class. Will give info on
        No: of edges(n) of largest polyon in the sequence and common Circumradius(R)
        '''
        s1 = 'poly_seq class instance : Largest Polygon class in the sequence has '
        s2 = f'{self.edges} sides with a common circumradius = {self.R}'
        return s1 + s2

    def __len__(self):
        '''
        Returns length of polygon sequence
        '''
        return self.edges

    def __getitem__(self, idx: int) -> tuple:
        '''
        getitem method that will help us to call the polygon sequences created by index as below
        s1 = poly_seq(6, 10)
        s1[-1], s1[0], s[5] etc.

        getitem based on the index it received, calls method '_calc_ratio' by supplying index+1 (to avoid 0 sides) &
        circumradius used while creating poly_seq class.
        '''
        # This is to handle -ve indexes like -1 s1[-1] should return last element in sequence
        if idx < 0:
            idx = self.edges + idx

        # Here s < 0 is important because this will handle large negative 's' like s = -9999
        if idx < 0 or idx >= self.edges:
            raise ValueError(
                f'Idx Unavailable. For no: of edges = {self.edges}, available indexes are 0 to {int(self.edges - 1)}')

            # for indexes 0 & 1 i.e. sides = 1 and sides =2 return area/perimeter ratio as 0 as they are not polygons
        if idx < 2:
            ratio = 0
        else:
            ratio = poly_seq._calc_ratio(idx + 1, self.R)

        msg = f'Area-Perimeter ration for polygon of side {idx + 1} is {ratio}'
        return msg, ratio

    @staticmethod  # Static methods are methods that are bound to a class rather than its object.
    @lru_cache(2 ** 10)  ##powers of 2
    def _calc_ratio(num_edges: int, c_radius: 'int or float') -> float:
        '''
        This is a method attached to class rather than object. This means we can call this method for parameters that are
        not used while creating object.
        eg: s1 = poly_seq(6, 10). Here sides = 6, radius =10.
        However we can call s1._calc_ratio(10, 20) ie for sides of 10 and radius = 20 without issues as we are not using self here.
        We are using lru_cache to store the values already claculated so that repetitive calculations can be avoided.
        This method is directly called in __getitem__() and indirectly called from max_efficient() methods.
        Returns area-perimeter ratio of the single polygon for given number of edges & circumradius
        '''
        poly = polygon(num_edges, c_radius)
        return poly.area / poly.perimeter

    @property
    def max_efficient(self) -> str:
        '''
        This method returns the Polygon with the highest area: perimeter ratio.
        Calls _getitem__ for each edge starting from 0 till self.edges -1 .
        __getitem__ fetches area-perimeter ratio then by calling _calc_ratio.
        If n = 0, __getitem__ gives area-per ratio for side = 1
           n = 5, __getitem__ gives area-per ratio for side = 6
        '''

        for n in range(self.edges):
            self.eff_ratio[n + 1] = self.__getitem__(n)[1]

        max_eff = max(self.eff_ratio, key=self.eff_ratio.get)
        # Reference for 'max' usage with 'key': https://stackoverflow.com/questions/18296755/python-max-function-using-key-and-lambda-expression

        s1 = f'Polygon with max efficiency for circumradius of {self.R} is one with {max_eff} sides & '
        s2 = f'Area-perimeter ratio for the same is {round(self.eff_ratio.get(max_eff), 4)}'
        return s1 + s2
