def get_banks(filename):
    banks = []
    with open(filename, 'r') as data:
        for line in data:
            banks.append(line.strip())
    return banks


def main():
    banks = get_banks('test_input.md')
    print(banks)

main()