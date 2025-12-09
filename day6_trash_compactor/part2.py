def add_numbers(numbers):
    sum = 0
    for number in numbers:
        sum += int(number)

    return sum

def multiply_numbers(numbers):
    product = int(numbers[0])
    for number in numbers[1:]:
        product *= int(number)

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

def restrucutre_columns(columns):
    return_columns = []

    restructured_columns = []
    for column in columns:
        restructured_column = []
        column = column[1:]
        for number in column:
            restructured_column.append(list(number))
        
        restructured_columns.append(restructured_column)

    for idx in range(len(restructured_columns)):
        restructured_columns[idx] = list(zip(*restructured_columns[idx]))

    for idx in range(len(restructured_columns)):
        for i in range(len(restructured_columns[idx])):
            restructured_columns[idx][i] = list(restructured_columns[idx][i])

    for column in restructured_columns:
        for number in column:
            while number[-1] == '0':
                number.pop(-1)

    for column in restructured_columns:
        return_columns.append([''.join(column2) for column2 in column])
        
    for idx in range(len(columns)):
        return_columns[idx].append(columns[idx][0])
    
    return return_columns
        

def main():
    grand_total = 0
    columns = get_columns('puzzle_input.md')

    columns = restrucutre_columns(columns)
    # print(columns, '\n')

    for column in columns:
        grand_total += solve_problem(column)
    
    print(f'grand total: {grand_total}')

main()