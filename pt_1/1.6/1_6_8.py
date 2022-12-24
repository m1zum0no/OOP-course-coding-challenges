TYPE_OS = 1  # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:
    # Класс Dialog должен создавать объекты класса DialogWindows, если переменная TYPE_OS = 1 
    # и объекты класса DialogLinux, если переменная TYPE_OS не равна 1
    __instance = None

    def __new__(cls, *args, **kwargs):  
        if TYPE_OS == 1:
            cls.__instance = super().__new__(DialogWindows)
        else:
            cls.__instance = super().__new__(DialogLinux)
        setattr(cls.__instance, 'name', args[0])  # == cls.__instance.name = args[0] 
        return cls.__instance
