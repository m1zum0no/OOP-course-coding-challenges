class Book:

    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, *args):
        if (args[0] in ('title', 'author') and not isinstance(args[1], str)) or (args[0] in ('pages', 'year') and not isinstance(args[1], int)):
            raise TypeError("Неверный тип присваиваемых данных.")
        super().__setattr__(args[0], args[1])

            

book = Book()
book = Book('Python ООП', 'Сергей Балакирев', 123, 2022)
# print(book.__dict__)
