
for number in range(95, 116):
    text = str(number)
    for divisor in range(1, len(text)):
        if len(text) % divisor == 0:
            temp = text
            cuts = len(text) // divisor
            slices = []
            for i in range(cuts):
                slices.append(temp[:divisor])
                temp = temp[divisor:]
            
            if len(set(slices)) == 1:
                print(True)
            else:
                print(False)

            print(number)