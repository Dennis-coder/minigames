from pygame.locals import *
from models.body_model import BodyModel
from globals import *
from models.observable import Observable

class SnakeModel(Observable):

    def __init__(self):
        super().__init__()
        self.dir = [0, 0]
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.length = 1
        self.head = BodyModel(self.x, self.y)
        self.tail = self.head

    def update(self):
        self.x += self.dir[0]
        self.y += self.dir[1]
        self.head.update(self.x, self.y)
        self.notice_all()
    
    def event_handling(self, event):
        if event.key == K_UP:
            self.change_dir([0, -1])
        elif event.key == K_DOWN:
            self.change_dir([0, 1])
        elif event.key == K_LEFT:
            self.change_dir([-1, 0])
        elif event.key == K_RIGHT:
            self.change_dir([1, 0])

    def change_dir(self, dir):
        if (self.dir[0] * dir[0] + self.dir[1] * dir[1]) == -1 and self.length > 1:
            return
        self.dir = dir
    
    def add_body_part(self):
        new_body = BodyModel(self.tail.x, self.tail.y)
        self.tail.next = new_body
        self.tail = new_body
        self.length += 1


    def ate_apple(self):
        for _ in range(3):
            self.add_body_part()