class Observable:

    def __init__(self):
        self.observers = []

    def add_observer(self, obj):
        self.observers.append(obj)
    
    def notice_all(self):
        for obj in self.observers:
            obj.notice(self)
