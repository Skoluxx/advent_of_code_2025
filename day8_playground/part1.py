from junction_box import JunctionBox

def create_points(filename):
    point = []
    with open(filename, 'r') as data:
        for line in data:
            values = line.strip().split(',')
            point.append(JunctionBox(int(values[0]), int(values[1]), int(values[2])))

    return point

def main():
    points = create_points('test_input.md')


main()