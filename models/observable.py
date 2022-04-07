class Observable:

    def __init__(self):
        self.observers = []

    def observe(self, obj):
        self.observers.append(obj)
    
    def notice_all(self):
        for obj in self.observers:
            obj.notice(self)
