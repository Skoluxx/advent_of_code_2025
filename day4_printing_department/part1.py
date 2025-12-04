def create_grid(filename):
    grid = []
    with open(filename, 'r') as data:
        for line in data:
            row = []
            values = list(line.strip())
            for character in values:
                row.append(character)
            grid.append(row)
    
    print(grid)
    return grid


def main():
    grid = create_grid('test_input.md')
    print('\n')
    for row in grid:
        print(row)

main()
