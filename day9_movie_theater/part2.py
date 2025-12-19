def get_red_tiles(filename):
    red_tiles = []

    with open(filename, 'r') as data:
        for line in data:
            position = line.strip().split(',')
            red_tiles.append([int(position[0]), int(position[1])])
    
    return red_tiles


def main():
    red_tiles = get_red_tiles('test_input.md')
    print(red_tiles)

main()