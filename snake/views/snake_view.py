import pygame as pg
from globals import *
from views.observer import Observer

class SnakeView(Observer):

    def __init__(self):
        self.snake = []
        self.image = pg.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(GREY)
    
    def draw(self, surface):
        for (x,y) in self.snake:
            surface.blit(self.image, (x * TILE_SIZE, y * TILE_SIZE))

    def notice(self, obj):
        cur = obj.head
        snake = []
        while cur:
            snake.append((cur.x, cur.y))
            cur = cur.next
        self.snake = snake