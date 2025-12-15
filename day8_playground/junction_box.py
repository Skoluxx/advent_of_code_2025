class JunctionBox:
    def __init__(self, x: int, y: int, z: int):
        self._coordinates = [x, y, z]
        self._curcuit = None

    def __str__(self):
        return f'x: {self._coordinates[0]}, y: {self._coordinates[1]}, z: {self._coordinates[2]}'

    def get_coordinates(self):
        return self._coordinates

    # ed = euclidean distance
    def get_ed(self, other):
        point1 = self.get_coordinates()
        point2 = other.get_coordinates()

        return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2) ** 0.5
    
    def get_curcuit(self):
        return self._curcuit
    
    def set_curcuit(self, curcuit):
        self._curcuit = curcuit

    def get_x(self):
        return self._coordinates[0]