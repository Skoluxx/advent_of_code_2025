def get_ingredient_ids(filename):
    ingredient_ids = set()
    with open(filename, 'r') as data:
        line = data.readline()
        while '-' in line:
            values = line.strip().split('-')
            for number in range(int(values[0]), int(values[1]) + 1):
                ingredient_ids.add(number)
            line = data.readline()
    return list(ingredient_ids)



def main():
    ingredient_ids = get_ingredient_ids('test_input.md')
    print(ingredient_ids)


main()
