class Message:
    def __init__(self, text, fl_like):
        self.text = text
        self.fl_like = fl_like

class Viber:

    chat = []

    def add_message(self, msg):
        self.chat.append(msg)
    
    def remove_message(self, msg):
        self.chat.pop(self.chat.index(msg))
    
    def set_like(self, msg):
        msg.fl_like = not msg.fl_like  # invert value 
    
    def show_last_message(self, n):
        print(self.chat[n:][:1])

    def total_messages():
        return len(self.chat)
