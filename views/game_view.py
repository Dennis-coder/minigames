import pygame as pg
from globals import *
from views.food_view import FoodView
from views.observer import Observer
from views.snake_view import SnakeView

class GameView(Observer):

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH * TILE_SIZE, HEIGHT * TILE_SIZE))
        self.snake = SnakeView()
        self.food = FoodView()
    
    def draw(self, surface):
        surface.fill(BLACK)
        self.food.draw(self.screen)
        self.snake.draw(self.screen)

    def notice(self, obj):
        self.draw(self.screen)
        pg.display.flip()