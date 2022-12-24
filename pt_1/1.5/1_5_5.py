class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        self.sides = [self.a, self.b, self.c]
        if not (all(type(e) in (float, int) and e > 0 for e in self.sides)):
            return 1
        else:
            hypothenuse = self.sides.pop(self.sides.index(max(self.sides)))
            if hypothenuse**2 == (self.sides[0]**2 + self.sides[1]**2):
                return 3
            return 2

a, b, c = map(int, input().split())

tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
