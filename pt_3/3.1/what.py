def some(func):
    def wrapper(*args, **kwargs):
        print("value changed %s - %s" % (args, kwargs))
        func(*args, **kwargs)
    return wrapper


class TestObject:

    @some
    def __setattr__(self, *args, **kwargs):
        super().__setattr__(*args, **kwargs)


obj = TestObject()
obj = TestObject(1, 2, 3)
