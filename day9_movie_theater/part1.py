def get_positions(filename):
    positions = []

    with open(filename, 'r') as data:
        for line in data:
            values = line.strip().split(',')
            positions.append([int(values[0]), int(values[1])])
            
    return positions
    
def main():
    positions = get_positions('test_input.md')
    print(positions)

main()
