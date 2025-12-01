def crack_password(file):
    numbers = []
    for number in range(100):
        numbers.append(number)

    turns = None
    current_number = 50
    zero_count = 0

    with open(file, 'r') as data:
        for line in data:
            turns = int(line[1:])

            if line[0] == 'R':
                current_number += turns
                while current_number not in numbers:
                    current_number -= 100
            
            elif line[0] == 'L':
                current_number -= turns
                while current_number not in numbers:
                    current_number += 100
            
            if current_number == 0:
                zero_count += 1

    return zero_count


def main():
    print('Passord:', crack_password('puzzle_input.md'))

main()