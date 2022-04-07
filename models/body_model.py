class BodyModel:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None
    
    def update(self, x, y):
        if self.next:
            self.next.update(self.x, self.y)
        self.x = x
        self.y = y