import random
import pygame as pg
from pygame.locals import *
from models.observable import Observable
from models.snake_model import SnakeModel
from models.food_model import FoodModel
from globals import *

class GameModel(Observable):

    def __init__(self):
        super().__init__()
        self.snake = SnakeModel()
        self.food = FoodModel()

    def update(self):
        self.snake.update()

        if self.check_out_of_bounds():
            self.game_over()

        if self.check_bit_own_tail():
            self.game_over()

        if self.check_snake_ate_apple():
            self.snake.ate_apple()
            self.new_food_pos()

        self.notice_all()

    def check_out_of_bounds(self):
        return not (0 <= self.snake.x < WIDTH and 0 <= self.snake.y < HEIGHT)

    def check_bit_own_tail(self):
        cur = self.snake.head.next
        while cur:
            if self.snake.x == cur.x and self.snake.y == cur.y:
                return True
            cur = cur.next

    def check_snake_ate_apple(self):
        return self.snake.x == self.food.x and self.snake.y == self.food.y
    
    def new_food_pos(self):
        free_spaces = set()
        for x in range(WIDTH):
            for y in range(HEIGHT):
                free_spaces.add((x,y))
        
        cur = self.snake.head
        while cur:
            if (cur.x, cur.y) in free_spaces:
                free_spaces.remove((cur.x, cur.y))
            cur = cur.next
        
        (new_x, new_y) = random.choice(list(free_spaces))
        self.food.new(new_x, new_y)

    def event_handler(self):
        for event in pg.event.get():
            if event.type == QUIT: 
                self.is_running = False
            elif event.type == KEYDOWN:
                self.snake.event_handling(event)

    def run(self):
        self.new_food_pos()
        clock = pg.time.Clock()
        self.is_running = True
        while self.is_running:
            self.event_handler()
            self.update()
            clock.tick(10)
        return self.snake.length

    def game_over(self):
        self.is_running = False