def get_ranges(filename):
    ranges = []
    with open(filename, 'r') as data:
            values = data.readlines()[0].split(',')
            for value in values:
                 numbers = value.split('-')
                 range = [int(numbers[0]), int(numbers[1])]
                 ranges.append(range)

    return ranges

def sum_ids(id_list):
    total = 0
    for number in id_list:
        total += number

    return total


def main():
    number_ranges = get_ranges('test_input.md')
    

main()