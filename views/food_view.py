import pygame as pg
from globals import *
from views.observer import Observer

class FoodView(Observer):

    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = pg.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(RED)
    
    def draw(self, surface):
        surface.blit(self.image, (self.x * TILE_SIZE, self.y * TILE_SIZE))

    def notice(self, obj):
        self.x = obj.x
        self.y = obj.y