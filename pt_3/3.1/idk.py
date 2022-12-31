def on_object_change(func):
    def wrapper(item, value):
        print("value changed %s - %s" % (item, value))
        func(item, value)
    return wrapper

class TestObject:
    def setattr(self, key, value):
        super().__setattr__(key, value)

    def __setattr__(self, key, value):
        self.setattr(key, value)

obj = TestObject()
obj2 = TestObject()

obj.setattr = on_object_change(obj.setattr)

obj.one = 1
obj2.setattr = on_object_change(obj.setattr)
obj2.two = 2
