def get_banks(filename):
    banks = []
    with open(filename, 'r') as data:
        for line in data:
            banks.append(int(line.strip()))
    return banks


def main():
    banks = get_banks('test_input.md')
    print(banks)

main()