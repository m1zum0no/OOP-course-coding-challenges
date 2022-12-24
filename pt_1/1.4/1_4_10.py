class Translator:

    def add(self, eng, rus):
        if eng in self.translator and not (rus in self.translator[eng]):
            self.translator[eng] = [*self.translator[eng], rus]
        elif not eng in self.translator:
            self.translator[eng] = [rus]

    def remove(self, eng):
        if eng in self.translator:
            del self.translator[eng]

    def translate(self, eng):
        if eng in self.translator:
            return self.translator[eng]

tr = Translator()
tr.translator = {}

for pair_of_words in ('tree - дерево', 'car - машина', 'car - автомобиль',
                      'leaf - лист', 'river - река', 'go - идти',
                      'go - ехать', 'go - ходить', 'milk - молоко'):
    tr.add(*pair_of_words.split(' - '))

tr.remove('car')
print(tr.translate('go'))