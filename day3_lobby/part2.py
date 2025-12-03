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

def main():
    banks = get_banks('test_input.md')
    print(banks)

main()