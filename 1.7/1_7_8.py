from string import ascii_uppercase, digits

class CardCheck:

    CHARS_FOR_NAME = [ascii_uppercase, digits]

    @classmethod
    def check_card_number(cls, number):
        try:
            num_lst = number.split('-')
            assert len(num_lst) == 4
            for i in range(4):
                assert all(c in cls.CHARS_FOR_NAME[1] for c in num_lst[i]) and len(num_lst[i]) == 4               
            return True
        except:
            return False
    
    @classmethod
    def check_name(cls, name):
        try:
            name_lst = name.split(' ')
            assert len(name_lst) == 2
            for i in range(2):
                assert all(c in cls.CHARS_FOR_NAME[0] for c in name_lst[i])               
            return True
        except:
            return False
