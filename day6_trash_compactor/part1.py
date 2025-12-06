def get_problems(filename):
    problems = []
    with open(filename, 'r') as data:
        for line in data:
            values = line.strip().split()
            for idx in range(values):
                