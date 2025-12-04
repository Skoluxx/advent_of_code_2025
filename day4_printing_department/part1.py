def create_grid(filename):
    grid = []
    with open(filename, 'r') as data:
        for line in data:
            row = []
            values = list(line.strip())
            for character in values:
                row.append(character)
            grid.append(row)

    return grid

def get_neighbour_rolls(grid, x, y):
    neighbours = 0
    nx = x - 1 
    for i1 in range(3):
        ny = y - 1
        for i2 in range(3):
            if (nx != x or ny != y) and (nx >= 0 and nx < len(grid)) and (ny >= 0 and ny < len(grid[0])):
                if grid[nx][ny] == '@':
                    neighbours += 1
            ny += 1
        nx += 1
    return neighbours


def main():
    grid = create_grid('puzzle_input.md')
    # for row in grid:
    #     print(row)

    rolls = 0
    for row in range(len(grid)):
        for value in range(len(grid[row])):
            if grid[row][value] == '@' and get_neighbour_rolls(grid, row, value) < 4:
                rolls += 1

    # print('\n')
    # for row in grid:
    #     print(row)
    
    print(f'accessible rolls: {rolls}')
main()
