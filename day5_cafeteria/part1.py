def get_ingredient_id_ranges(filename):
    ingredient_id_ranges = [] 
    with open(filename, 'r') as data:
        line = data.readline()
        while '-' in line:
            values = line.strip().split('-')
            ingredient_id_ranges.append([int(values[0]), int(values[1])])
            line = data.readline()
    return list(ingredient_ids)



def main():
    ingredient_ids = get_ingredient_id_ranges('test_input.md')
    print(ingredient_ids)
    
    # fresh_ingredients = count_fresh_ingredients('puzzle_input.md', ingredient_ids)
    # print(f'Fresh ingredients: {fresh_ingredients}')



main()
