with open('test_input.md', 'r') as data:
    for line in data:
        print(list(line.rstrip()))