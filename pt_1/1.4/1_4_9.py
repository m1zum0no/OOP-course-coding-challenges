import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока

class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    
    def select(self, a, b):
        sel_lst = []
        for i in self.lst_data[a:]:
            sel_lst.append(i)
            if (b < (len(self.lst_data))) and (self.lst_data.index(i) == b):
                break
        return sel_lst

    def insert(self, data):
        for i in data:
            dct_el = {}
            entry = list(i.split())
            for j in range(len(self.FIELDS)):
                dct_el[self.FIELDS[j]] = entry[j]
            self.lst_data.append(dct_el)


db = DataBase()
db.insert(lst_in)