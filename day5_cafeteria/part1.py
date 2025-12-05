def get_ingredient_id_ranges(filename):
    ingredient_id_ranges = [] 
    with open(filename, 'r') as data:
        line = data.readline()
        while '-' in line:
            values = line.strip().split('-')
            ingredient_id_ranges.append([int(values[0]), int(values[1])])
            line = data.readline()

    return ingredient_id_ranges


def count_fresh_ingredients(filename, ingredient_ids):
    fresh_ingredients = []
    with open(filename, 'r') as data:
        for line in data:
            line = line.strip()
            if ('-' not in line and line != ''):
                for i_range in ingredient_ids:
                    if int(line) in range(i_range[0], i_range[1] + 1) and line not in fresh_ingredients:
                        fresh_ingredients.append(line)
    
    return len(fresh_ingredients)





def main():
    ingredient_ids = get_ingredient_id_ranges('puzzle_input.md')
    
    fresh_ingredients = count_fresh_ingredients('puzzle_input.md', ingredient_ids)
    print(f'Fresh ingredients: {fresh_ingredients}')



main()
