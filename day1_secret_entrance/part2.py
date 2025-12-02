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
                while turns > 0:
                    if current_number == 99:
                        current_number = 0
                    else:
                        current_number += 1
                    
                    if current_number == 0:
                        zero_count += 1

                    turns -= 1
            
            elif line[0] == 'L':
                while turns > 0:
                    if current_number == 0:
                        current_number = 99
                    else:
                        current_number -= 1
                    
                    if current_number == 0:
                        zero_count += 1
                        
                    turns -= 1

            print(current_number)

    return zero_count


def main():
    print('Passord:', crack_password('puzzle_input.md'))

main()