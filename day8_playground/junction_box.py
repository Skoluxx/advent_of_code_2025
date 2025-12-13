class JunctionBox:
    def __init__(self, x: int, y: int, z: int):
        self._x = x
        self._y = y
        self._z = z
        self._coordinates = [self._x, self._y, self._z]

    def __str__(self):
        return f'x: {self._x}, y: {self._y}, z: {self._y}'

    def get_coordinates(self):
        return self._coordinates

    # point = [x, y, z]
    # ed = euclidean distance
    def get_ed(self, other):
        point1 = self.get_coordinates()
        point2 = other.get_coordinates()

        return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2) ** 0.5