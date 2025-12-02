def get_ranges(filename):
    ranges = []
    with open(filename, 'r') as data:
            values = data.readlines()[0].split(',')
            for value in values:
                 numbers = value.split('-')
                 range = [int(numbers[0]), int(numbers[1])]
                 ranges.append(range)

    
    return ranges

def main():
    ranges = get_ranges('test_input.md')
    print(ranges)


main()