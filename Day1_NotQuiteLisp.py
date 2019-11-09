raw_data = open("input1.txt", 'r')


floor = 0
for i in raw_data:
    data = i

data_list = data.split()
print(data)

counter = 0
for i in data:
    counter += 1
    if i == '(':
        floor += 1
        if floor == -1:
            print('Position: ' + str(counter))
    else:
        floor -= 1
        if floor == -1:
            print('Position: ' + str(counter))
print(floor)



raw_data.close()