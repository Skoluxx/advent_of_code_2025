def get_grid(filename):
    with open(filename, 'r') as data:
        grid = []
        for line in data:
            grid.append(list(line.strip()))
            
    return grid
    

# Denne oppgaven var way 2 hard for meg tbh. Måtte få hjelp med denne functionen, jeg claimer ikke å ha naila denne her.
# It is what it is.
def count_timelines(grid):
    nrows, ncols = len(grid), len(grid[0])

    for c in range(ncols):
        if grid[0][c] == 'S':
            start = (0, c)
            break

    active = {start: 1}

    for r in range(start[0], nrows - 1):
        next_active = {}
        for (row, col), count in active.items():
            if row != r:
                continue
            cell = grid[row][col]

            if cell == '^':
                for dc in (-1, 1):
                    nc = col + dc
                    if 0 <= nc < ncols:
                        next_active[(row + 1, nc)] = next_active.get((row + 1, nc), 0) + count
            else:
                nc = col
                if 0 <= nc < ncols:
                    next_active[(row + 1, nc)] = next_active.get((row + 1, nc), 0) + count

        active = next_active

    return sum(active.values())

def main():
    grid = get_grid('puzzle_input.md')

    # for row in grid:
    #     print(''.join(row))

    timelines = count_timelines(grid)
    print(f'\nTimelines: {timelines}')

main()