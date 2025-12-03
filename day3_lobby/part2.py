def get_banks(filename):
    banks = []
    with open(filename, 'r') as data:
        for line in data:
            banks.append(line.strip())
    
    return banks

def sum_joltages(joltages):
    sum = 0
    for joltage in joltages:
        sum += joltage
    
    return sum

def find_largest_joltage(bank):
    largest_joltage = ''
    number_list = list(bank)

    for x in range(12):
        largest = 0
        for number in number_list[:len(number_list) - 11 + x]:
            if int(number) > largest:
                largest = int(number)
        idx = number_list.index(str(largest))
        largest_joltage += str(largest)
        number_list = number_list[idx+1:]

    return int(largest_joltage)

def main():
    joltages = []

    banks = get_banks('puzzle_input.md')
    for bank in banks:
        joltages.append(find_largest_joltage(bank))

    print(f'Sum: {sum_joltages(joltages)}')

main()