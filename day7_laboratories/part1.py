def get_grid(filename):
    with open(filename, 'r') as data:
        grid = [line.strip() for line in data]
    
    return grid



def main():
    grid = get_grid('test_input.md')
    startidx = grid[0].index('S')

main()