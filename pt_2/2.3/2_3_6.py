# data descriptor
class FloatValue:

    # set descriptor's internal name for setattr to not descend into infinite loop
    # caused by calling itself (setattr method) recursively from the Cell's attribute
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, is_float):
        if not isinstance(is_float, float):
            raise TypeError("Присваивать можно только вещественный тип данных.")
        setattr(instance, self.name, is_float) 


class Cell:

    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value


class TableSheet:
    
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.cells = [[Cell() for _ in range(M)] for _ in range(N)]


table = TableSheet(5, 3)
n = (float(i) for i in range(1, 16))
[setattr(table.cells[y][x],'value',next(n)) for y in range(5) for x in range(3)]
