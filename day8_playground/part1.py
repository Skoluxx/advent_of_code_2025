from junction_box import JunctionBox
from curcuit import Curcuit
import math

def create_points(filename):
    points = []
    with open(filename, 'r') as data:
        for line in data:
            values = line.strip().split(',')
            points.append(JunctionBox(int(values[0]), int(values[1]), int(values[2])))

    return points

def create_curcuits(points):
    curcuits = []
    for point in points:
        curcuits.append(Curcuit(point))
    
    return curcuits

def get_distances(points):
    distances = {}
    for point1 in points:
        for point2 in points:
            if point1 is not point2:
                ed = point1.get_ed(point2)
                if ed not in distances:
                    distances[ed] = [point1, point2]
                    
    return distances

def combine_curcuits(closest, curcuits):
    c1 = closest[0].get_curcuit()
    c2 = closest[1].get_curcuit()

    c1.append_curcuit(c2)

    idx = curcuits.index(c2)
    curcuits.pop(idx)

def main():
    points = create_points('puzzle_input.md')
    curcuits = create_curcuits(points)
    distances = get_distances(points)
    distance_keys = sorted(distances)
    jb_per_curcuit = []

    for idx in range(1000):
        closest = distance_keys[idx]
        if distances[closest][0].get_curcuit() is not distances[closest][1].get_curcuit():
            combine_curcuits(distances[closest], curcuits)

    for curcuit in curcuits:
        jb_per_curcuit.append(curcuit.get_curcuit_length())

    print(f'Product of the three largest circuits: {math.prod(sorted(jb_per_curcuit)[-3:])}')
main()