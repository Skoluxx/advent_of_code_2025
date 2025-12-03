def get_banks(filename):
    banks = []
    with open(filename, 'r') as data:
        for line in data:
            banks.append(line.strip())
    return banks

def find_largest_joltage(bank):
    number_list = list(bank)
    
    first_largest = 0
    for idx in range(len(number_list) - 1):
        if int(number_list[idx]) > first_largest:
            first_largest = int(number_list[idx])

    temp_number = int(number_list[0])
    while temp_number != first_largest:
         number_list.pop(0)
         temp_number = int(number_list[0])
        
    if '9' in number_list[1:]:
        second_largest = 9
    else:
        second_largest = 0
        for idx in range(1, len(number_list)):
            if int(number_list[idx]) > second_largest:
                second_largest = int(number_list[idx])
    
    return int(f'{first_largest}{second_largest}')

def total_joltage_output(joltages):
    sum = 0
    for joltage in joltages:
        sum += joltage
    
    return sum


def main():
    banks = get_banks('puzzle_input.md')

    largest_joltages = []
    for bank in banks:
        largest_joltages.append(find_largest_joltage(bank))

    print(f'Total joltage output: {total_joltage_output(largest_joltages)}')

main()