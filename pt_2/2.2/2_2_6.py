class StackObj:

    def __init__(self, data):
        self.__data = data
        self.__next = None


    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, next):
        if isinstance(next, StackObj) or next is None:
            self.__next = next


    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data


class Stack:
    
    def __init__(self):
        self.top = None

    def get_last(self):
        if self.top:
            node = self.top
            last_two = []
            while node.next:
                if not node.next.next:  # one before last for removing the link
                    # in pop operation, indexed with 0
                    last_two.append(node)
                node = node.next    
            last_two.append(node) 
            return last_two

    def push(self, obj):
        if self.top:
            last_two = self.get_last()
            last_two[len(last_two) - 1].next = obj
        else:    
            self.top = obj    

    def pop(self):
        last_two = self.get_last()
        if len(last_two) == 2:  # check whether there is a previous node
            last = last_two[1] 
            last_two[0].next = None
        else:
            last = last_two[0]
            self.top = None 
        return last

    def get_data(self):
        data_lst = []
        if self.top:
            st_frame = self.top 
            while st_frame:
                data_lst.append(st_frame.data)
                st_frame = st_frame.next
        return data_lst
