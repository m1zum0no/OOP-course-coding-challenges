class Router:

    __instance = None

    def __new__(cls, *args, **kwargs):  
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.linked_servers = []
        self.buffer = []

    def link(self, server):
        server.link(self)
        self.linked_servers.append(server)

    def unlink(self, server):
        server.unlink()
        self.linked_servers.pop(self.linked_servers.index(server))

    def send_data(self):
        # для отправки всех пакетов (объектов класса Data) из буфера роутера 
        # соответствующим серверам (после отправки буфер должен очищаться).
        for sv in self.linked_servers:
            for pack in self.buffer:
                if pack.ip == sv.ip:
                    sv.buffer.append(pack)
        del self.buffer[::]


class Server:

    count = 0
    
    @classmethod
    def count_instances(cls):
        cls.count += 1

    def __init__(self):
        self.count_instances() 
        self.ip = self.count
        self.buffer = []
    
    def link(self, router):
        self.linked_router = router

    def unlink(self):            
        self.linked_router = None
    
    def send_data(self, data):
        # для отправки информационного пакета data (объекта класса Data) 
        # с указанным IP-адресом получателя (пакет отправляется роутеру и сохраняется в его буфере 
        # - локальном свойстве buffer)
        self.linked_router.buffer.append(data)


    def get_data(self):
        # возвращает список принятых пакетов (если ничего принято не было, 
        # то возвращается пустой список) и очищает входной буфер;
        received_packs = self.buffer.copy()
        del self.buffer[::]
        return received_packs

    def get_ip(self):
        # возвращает свой IP-адрес.        
        return self.ip


class Data:
    
    def __init__(self, data, dest_ip):
        self.data = data
        self.ip = dest_ip


router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))  # no(!) obj ref 
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
print(sv_from.get_data())
print(sv_to.get_data())