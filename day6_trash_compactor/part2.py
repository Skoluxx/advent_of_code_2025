def add_numbers(numbers):
    sum = 0
    for number in numbers:
        sum += number

    return sum

def multiply_numbers(numbers):
    product = numbers[0]
    for number in numbers[1:]:
        product *= number

    return product

def solve_problem(problem):
    if problem[-1] == '+':
        solution = add_numbers(problem[:-1])
    else:
        solution = multiply_numbers(problem[:-1])

    return solution

def get_columns(filename):
    with open(filename, 'r') as data:
        rows = [line.strip('\n').split(' ') for line in data]
    operators = []
    for character in rows[-1]:
        if character != '':
            operators.append([character])
        else:
            operators[-1].append(character)

    rows = rows[:-1]
    for idx in range(len(rows)):
        for i in range(len(rows[idx])):
            if not rows[idx][i].isdigit():
                rows[idx][i] = '0'

    columns = []
    for i in range(len(operators)):
        column = [operators[0][0]]
        length = len(operators[0])
        operators.pop(0)      
        for row in rows:
            number = ''
            while len(number) < length:
                number += row[0]
                row.pop(0)

            column.append(number)
        columns.append(column)


    return columns


def main():
    grand_total = 0
    columns = get_columns('test_input.md')
    print(columns, '\n')

    # for problem in problems:
    #     grand_total += solve_problem(problem)
    
    # print(f'grand total: {grand_total}')

main()