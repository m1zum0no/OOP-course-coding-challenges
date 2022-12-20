class Graph:

    LIMIT_Y:list = [0, 10]  # type annotation 

    def set_data(self, data):
        self.data = data
    
    def draw(self):
        start, end = self.LIMIT_Y
        res = (i for i in self.data if i in range(start, end+1))
        # OR print(*filter(lambda x: start <= x <= end, self.data))
        print(*res)

graph_1 = Graph()

graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()


