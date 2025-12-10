def get_grid(filename):
    with open(filename, 'r') as data:
        grid = []
        for line in data:
            grid.append(list(line.strip()))
    
    return grid

def get_split_amount(grid, startidx):
    beamidxs = [startidx]
    splits = 0

    for row in grid[1:]:
        new_beamidxs = set()
        removeidxs = []
        for beamidx in beamidxs:
            if row[beamidx] == '^':
                removeidxs.append(beamidx)
                splits += 1
                new_beamidxs.add(beamidx - 1), new_beamidxs.add(beamidx + 1)
                row[beamidx-1] = '|'
                row[beamidx+1] = '|'
            
            else: row[beamidx] = '|'

        for idx in removeidxs:
            beamidxs.remove(idx)

        beamidxs += list(new_beamidxs)
        beamidxs = sorted(list(set(beamidxs)))
    
    return splits


def main():
    grid = get_grid('puzzle_input.md')
    startidx = grid[0].index('S')

    split_amount = get_split_amount(grid, startidx)
    for row in grid:
        print(''.join(row))

    print(f'\nsplit amount: {split_amount}')

main()