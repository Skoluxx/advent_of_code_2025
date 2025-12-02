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

def invalid_ids(number_range):
    ids = []
    for number in range(number_range[0], number_range[1] + 1):
        number_text = str(number)
        for divisor in range(1, len(number_text)):
            if len(number_text) % divisor == 0:
                temp_text = number_text
                cuts = len(number_text) // divisor
                slices = []
                for i in range(cuts):
                    slices.append(temp_text[:divisor])
                    temp_text = temp_text[divisor:]
                if len(set(slices)) == 1 and number not in ids:
                    ids.append(number)
    return ids


def main():
    number_ranges = get_ranges('test_input.md')

    ids = []
    for number_range in number_ranges:
        ids += invalid_ids(number_range)
    print(ids)

main()