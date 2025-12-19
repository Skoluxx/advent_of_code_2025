import math

def get_red_tiles(filename):
    red_tiles = []

    with open(filename, 'r') as data:
        for line in data:
            position = line.strip().split(',')
            red_tiles.append([int(position[0]), int(position[1])])
    
    return red_tiles

def get_outer_ranges(red_tiles):
    o_green_ranges = []

    for idx in range(len(red_tiles) - 1):
        x1 = min(red_tiles[idx][0], red_tiles[idx + 1][0])
        x2 = max(red_tiles[idx][0], red_tiles[idx + 1][0])
        y1 = min(red_tiles[idx][1], red_tiles[idx + 1][1])
        y2 = max(red_tiles[idx][1], red_tiles[idx + 1][1])

        if x1 == x2:
            x = x1

            if y1 != y2:
                o_green_ranges.append([[x], [y1, y2]])
            else:
                o_green_ranges.append([[x], [y1]])
        
        else:
            y = y1

            if x1 != x2:
                o_green_ranges.append([[x1, x2], [y]])
            else:
                o_green_ranges.append([[x1], [y]])

    x1 = min(red_tiles[0][0], red_tiles[-1][0])
    x2 = max(red_tiles[0][0], red_tiles[-1][0])
    y1 = min(red_tiles[0][1], red_tiles[-1][1])
    y2 = max(red_tiles[0][1], red_tiles[-1][1])

    if x1 == x2:
        x = x1

        if y1 != y2:
            o_green_ranges.append([[x], [y1, y2]])
        else:
            o_green_ranges.append([[x], [y1]])
    
    else:
        y = y1

        if x1 != x2:
            o_green_ranges.append([[x1, x2 + 1], [y]])
        else:
            o_green_ranges.append([[y], [x1]])
    return o_green_ranges

def paint_grid(red_tiles, o_green_ranges):
    length = 0
    width = 0
    for position in red_tiles:
        if position[0] > length:
            length = position[0]
        if position[1] > width:
            width = position[1]

    dimensions = [length, width]

    o_tiles = []
    for o_range in o_green_ranges:
        if len(o_range[0]) == 1 and len(o_range[1]) == 1:
            o_tiles.append([o_range[0][0], o_range[1][0]])

        elif len(o_range[0]) == 1:
            x = o_range[0][0]

            for y in range(o_range[1][0], o_range[1][1] + 1):
                o_tiles.append([x, y])
        else:
            y = o_range[1][0]

            for x in range(o_range[0][0], o_range[0][1] + 1):
                o_tiles.append([x, y])
    
    print('Painting grid:')
    for y in range(dimensions[1] + 2):
        row = []
        for x in range(dimensions[0] + 3):
            if [x, y] in o_tiles:
                row.append('X')
            else:
                row.append('.')

        print(''.join(row))

def paint_grid2(red_tiles, x_row):
    length = 0
    width = 0
    for position in red_tiles:
        if position[0] > length:
            length = position[0]
        if position[1] > width:
            width = position[1]

    dimensions = [length, width]
    print('Painting grid:')
    for y in range(dimensions[1] + 2):
        row = []
        if y in x_row:
            for x in range(dimensions[0] + 3):
                if x in range(x_row[y][0], x_row[y][-1] + 1):
                    
                    row.append('X')
                else:
                    row.append('.')

        print(''.join(row))

def get_row_ranges(o_ranges):
    row_ranges = {}
    for o_range in o_ranges:
        if len(o_range[1]) == 1:
            if o_range[1][0] not in row_ranges:
                row_ranges[o_range[1][0]] = set(o_range[0])
            else:
                row_ranges[o_range[1][0]].update(set(o_range[0]))
        else:
            for y in range(o_range[1][0], o_range[1][-1] + 1):
                if y not in row_ranges:
                    row_ranges[y] = set(o_range[0])
                else:
                    row_ranges[y].update(set(o_range[0]))

    for value in row_ranges:
        row_ranges[value] = [min(row_ranges[value]), max(row_ranges[value])]
    
    return row_ranges

def main():
    print('Getting red tiles')
    red_tiles = get_red_tiles('test_input.md')
    print('Got red tiles')
    print('len:', len(red_tiles))
    print('Red tiles:', red_tiles, '\n')

    print('Getting outer tile ranges')
    o_ranges = get_outer_ranges(red_tiles)
    print('Got outer tile ranges')
    print('len:', len(o_ranges))
    print('Outer tile ranges:', o_ranges, '\n')

    row_ranges = get_row_ranges(o_ranges)
    print(row_ranges)
    
    paint_grid(red_tiles, o_ranges)

    paint_grid2(red_tiles, row_ranges)



main()