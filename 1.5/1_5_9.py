import sys

class ListObject():

    def __init__(self, data):
        self.next_obj = None
        self.data = data

    def link(self, obj):
        self.next_obj = obj

lst_in = list(map(str.strip, sys.stdin.readlines()))

def link_nodes(node):
    global i
    i += 1
    if i == len(lst_in):
        exit()
    node.next_obj = link_nodes(ListObject(lst_in[i])) 

global i
i = 0
head_obj = ListObject(lst_in[i])
link_nodes(head_obj)
