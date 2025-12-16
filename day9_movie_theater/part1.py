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
    
def main():
    positions = get_positions('test_input.md')
    print(positions)
    dimensions = get_dimensions(positions)
    print(dimensions[0])
    print(dimensions[1])

main()
