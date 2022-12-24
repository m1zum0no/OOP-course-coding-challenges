class ObjList:
    
    def __init__(self, data):
        self.__prev = None
        self.__data = None
        self.__next = None
        self.set_data(data)

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self): 
        return self.__data
    

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_obj(self, obj):
        # initializing the first element
        if not self.head:
            self.head = obj
            self.tail = self.head
        # adding the second
        elif self.tail == self.head:
            self.head.set_next(obj)
            obj.set_prev(self.head)    
            self.tail = obj
        # the rest
        else:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj

    def remove_obj(self):
        to_rm = self.tail
        if to_rm == self.head:
            self.head = None
        self.tail = self.tail.get_prev()
        del to_rm

    def get_data(self):
        data_lst = []
        if self.head:
            node = self.head
            while node != self.tail:
                data_lst.append(node.get_data())
                node = node.get_next()
            data_lst.append(node.get_data())
        return data_lst
