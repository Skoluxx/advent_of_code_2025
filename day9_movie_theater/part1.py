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

def paint_grid(positions):
    dimensions = get_dimensions(positions)
    
    for y in range(dimensions[1] + 2):
        row = []
        for x in range(dimensions[0] + 3):
            if [x, y] in positions:
                row.append('#')
            else:
                row.append('.')
        print(''.join(row))

def get_all_areas(positions):
    areas = {}
    for pos1 in positions:
        for pos2 in positions:
            if pos1 is not pos2:
                length = (max(pos1[0], pos2[0]) - min(pos1[0], pos2[0]) + 1)
                width = (max(pos1[1], pos2[1]) - min(pos1[1], pos2[1]) + 1)
            
                areas[length * width] = [pos1, pos2]
    
    return areas

    
def main():
    positions = get_positions('puzzle_input.md')
    # print(positions)

    areas = get_all_areas(positions)
    print(sorted(areas)[-1])



main()
