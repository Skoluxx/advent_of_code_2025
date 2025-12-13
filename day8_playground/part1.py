def get_coordinates(filename):
    coordinates = []
    with open(filename, 'r') as data:
        for line in data:
            values = line.strip().split(',')
            coordinates.append([int(values[0]), int(values[1]), int(values[2])])

    return coordinates


# point = [x, y, z]
def calc_euclidean_distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2) ** 0.5

def main():
    coordinates = get_coordinates('test_input.md')

    e_distance = calc_euclidean_distance(coordinates[0], coordinates[1])
    print(e_distance)
main()