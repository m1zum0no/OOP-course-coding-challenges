class Graph:
    def __init__(self, data):
        self.data = data.copy()  # == data[:] -- shallow copy
        self.is_show = True

    def dont_show(self):
        print("Отображение данных закрыто")

    def set_data(self, data):
        self.data = data.copy()

    def show_table(self):
        if self.is_show:
            print(*[i for i in self.data])
        else:
            self.dont_show()

    def show_graph(self):
        if self.is_show:
            print("Графическое отображение данных: ", end='')
            self.show_table()
        else:
            self.dont_show()

    def show_bar(self):
        if self.is_show:
            print("Столбчатая диаграмма: ", end='')
            self.show_table()
        else:
            self.dont_show()

    def set_show(self, fl_show):
        self.is_show = fl_show
    

data_graph = list(map(int, input().split()))

gr = Graph(data_graph)

gr.show_bar()
gr.set_show(False)
gr.show_table()