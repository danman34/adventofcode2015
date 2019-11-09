import timeit
start = timeit.default_timer()

input_text = open('input3.txt', 'r')
input_list = []

for i in input_text:
    input_list.append(i)
commands = list(input_list[0])


class Santa:
    def __init__(self):
        self.location = [0, 0]
        self.presents = {tuple(self.location): 1}

    def move(self, char):
        if char == '^':
            self.location[1] += 1
        elif char == 'v':
            self.location[1] -= 1
        elif char == '>':
            self.location[0] += 1
        elif char == '<':
            self.location[0] -= 1

        if tuple(self.location) in self.presents:
            self.presents[tuple(self.location)] += 1
        else:
            self.presents[tuple(self.location)] = 1


Santa1 = Santa()
RoboSanta = Santa()

i = 0
for i in range(len(commands)):
    if i % 2 == 0:
        Santa1.move(commands[i])
    else:
        RoboSanta.move(commands[i])

united_presents = Santa1.presents.copy()


for i in RoboSanta.presents:
    if i not in united_presents:
        united_presents[i] = 1
    elif i in united_presents:
        united_presents[i] += 1

print(len(united_presents))
    #print(Santa1.presents)

print(len(Santa1.presents))


input_text.close()

stop = timeit.default_timer()
print('Time: ', stop - start)