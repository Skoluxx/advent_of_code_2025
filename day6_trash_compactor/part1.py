def get_problems(filename):
    problems = []

    with open(filename, 'r') as data:
        for line in data:
            values = line.strip().split()

            if not problems:
                for item in values:
                    problems.append([int(item)])
            else:
                for idx in range(len(values)):
                    if values[idx].isdigit():
                        values[idx] = int(values[idx])
                    problems[idx].append(values[idx])
    
    return problems

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


def main():
    grand_total = 0
    problems = get_problems('puzzle_input.md')

    for problem in problems:
        grand_total += solve_problem(problem)
    
    print(f'grand total: {grand_total}')

main()
                