list = [2,3,4,2,3,4,2,3,4,2,3,4,2,7,8]
print(list)

print(len(list))
for num in list[:len(list)-11]:
    print(num)


list = list[len(list)-11:]
print(list)

list.insert(0, 'nummer')
print(list)
print(len(list))