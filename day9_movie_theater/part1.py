def get_positions(filename):
    positions = []

    with open(filename, 'r') as data:
        for line in data:
            values = line.strip().split(',')
            positions.append([int(values[0]), int(values[1])])

    return sorted(positions)

def get_dimensions(positions):
    length = positions[-1][0]

    width = 0
    for position in positions:
        if position[1] > width:
            width = position[1]

    return [length, width]

def paint_grid(dimensions, positions):
    for y in range(dimensions[1] + 2):
        row = []
        for x in range(dimensions[0] + 3):
            if [x, y] in positions:
                row.append('#')
            else:
                row.append('.')
        print(''.join(row))


    
def main():
    positions = get_positions('test_input.md')
    print(positions)

    dimensions = get_dimensions(positions)
    print(dimensions)

    paint_grid(dimensions, positions)


main()
