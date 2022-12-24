from random import choice, randint

class Line:
    def __init__(self, a=0, b=0, c=0, d=0):
        self.sp = (a, b)
        self.ep = (c, d)

class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


elements = [] 

for i in range(217):
    # для каждого текущего объекта класс выбирается случайно, координаты также генерируются случайным образом. 
    # все объекты сохраняются в списке elements.
    a, b, c, d = [randint(-255, 255) for i in range(4)]
    elements.append(choice([Line(), Rect(a, b, c, d), Ellipse(a, b, c, d)]))
