class SingletonFive:

    __instance = None
    instance_count = 0

    def __new__(cls, *args, **kwargs):  
        if cls.instance_count < 5:
            cls.__instance = super().__new__(cls)
            cls.instance_count += 1
        return cls.__instance

    def __init__(self, denom):
        self.name = denom    

objs = [SingletonFive(str(n)) for n in range(10)]
