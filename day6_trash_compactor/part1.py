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
    
    print(problems)


def main():
    get_problems('test_input.md')

main()
                