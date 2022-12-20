class Cell:
    
    def __init__(self, around_mines=0, mine=0):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False

    
class GamePole:

    def calc_logic(self, x, y):
        for delta_x in range(x - 1, x + 2):
            for delta_y in range(y - 1, y + 2):
                if all(0 <= coord < len(self.pole) for coord in (delta_x, delta_y)):
                    if self.pole[delta_x][delta_y].mine == '*':
                        continue
                    else:
                        self.pole[delta_x][delta_y].around_mines += 1


    def count_around_mines(self):
        for x in range(len(self.pole)):
            for y in range(len(self.pole)):
                if self.pole[x][y].mine == '*':
                    self.calc_logic(x, y)

    def set_mines(self, N, M):
        from random import randint
        
        self.mines_coords = set()
        while len(self.mines_coords) < M:
            self.mines_coords.add((randint(0, N), randint(0, N)))  
    
    def init(self, N, M):
        # инициализация поля с новой расстановкой M мин 
        # (случайным образом по игровому полю, каждая мина в отдельной клетке).
        self.set_mines(N, M)
        self.pole = [[Cell(mine='*' if (i, j) in self.mines_coords else 0) for i in range(N)] for j in range(N)]
        self.count_around_mines()

    def __init__(self, N, M):
        self.init(N, M)

    def show(self):
        # отображение поля в консоли в виде таблицы чисел открытых клеток 
        # (если клетка не открыта, то отображается символ #).
        for x in range(len(self.pole)):
            for y in range(len(self.pole)):
                if not self.pole[x][y].fl_open:
                    print('#', end=' ')
                else:    
                    print(self.pole[x][y].around_mines if not self.pole[x][y].mine else self.pole[x][y].mine, end=' ')
            print('\n')              


pole_game = GamePole(10, 12)
