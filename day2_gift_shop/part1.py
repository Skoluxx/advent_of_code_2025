def get_ranges(filename):
    ranges = []
    with open(filename, 'r') as data:
            values = data.readlines()[0].split(',')
            for value in values:
                 numbers = value.split('-')
                 range = [int(numbers[0]), int(numbers[1])]
                 ranges.append(range)

    return ranges

def return_invalid(number_range):
    invalid_ids = []
    for number in range(number_range[0], number_range[1] + 1):
        if len(str(number)) % 2 == 0:
            halfpoint = int(len(str(number)) / 2)
            number1 = str(number)[:halfpoint]
            number2 = str(number)[halfpoint:]
        
            if number1 == number2:
                invalid_ids.append(number)
                print(number)
                
    return invalid_ids
                 
                
               
     
     

def main():
    ranges = get_ranges('test_input.md')
    print(ranges)

    return_invalid([1, 100])


main()