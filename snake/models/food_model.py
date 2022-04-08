from models.observable import Observable

class FoodModel(Observable):

    def __init__(self):
        super().__init__()
        self.x = 1
        self.y = 1
    
    def new(self, x, y):
        self.x = x
        self.y = y
        self.notice_all()