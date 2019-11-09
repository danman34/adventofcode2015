input_text = open('input2.txt', 'r')

input_list = []

for i in input_text:
    input_list.append(i[:-1].split('x'))

for i in range(len(input_list)):
    for j in range(len(input_list[i])):
        input_list[i][j] = int(input_list[i][j])


list_of_boxes = []


class Box:
    def __init__(self, list):
        self.l = list[0]
        self.w = list[1]
        self.h = list[2]
        self.mat = 0
        self.f1 = self.l * self.w
        self.f2 = self.w * self.h
        self.f3 = self.h * self.l
        self.sides_list = [self.f1, self.f2, self.f3]
        self.sides_sorted = sorted(list.copy())
        self.smallest = min(self.sides_list)
        self.measure()
        self.ribbon = self.sides_sorted[0]*2 + self.sides_sorted[1]*2 + self.l*self.w*self.h

    def measure(self):
        self.mat = 2 * self.f1 + 2 * self.f2 + 2 * self.f3 + self.smallest


for i in input_list:
    list_of_boxes.append(Box(i))

material = 0

ribbon = 0

for i in list_of_boxes:
    material += i.mat
    ribbon += i.ribbon

print(material)
print(ribbon)
input_text.close()

print(input_list[0])

b = Box([2, 3, 4])

print(b.mat)
print(b.ribbon)