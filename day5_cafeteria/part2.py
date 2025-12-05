def get_ingredient_id_ranges(filename):
    ingredient_id_ranges = [] 
    with open(filename, 'r') as data:
        line = data.readline()
        while '-' in line:
            values = line.strip().split('-')
            ingredient_id_ranges.append((int(values[0]), int(values[1])))
            line = data.readline()

    return sorted(ingredient_id_ranges)


def merge_ranges(ids):
    merged = []

    for range in ids:
        if not merged or merged[-1][1] < range[0]:
            merged.append(range)
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], range[1]))
    return merged

def get_total_ids(merged_ids):
    ids = 0
    for range in merged_ids:
        ids += range[1] - range [0] + 1

    return ids


def main():
    ids = get_ingredient_id_ranges('puzzle_input.md')

    merged_ids = merge_ranges(ids)
    
    total_ids = get_total_ids(merged_ids)

    print(f'Total ids: {total_ids}')

main()
