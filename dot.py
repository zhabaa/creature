import pygame as pg

from settings import COLORS

class Dot:
    def __init__(self, x, y, color):
        self.position = x, y
        self.x = x
        self.y = y
        self.radius = 1
        self.color = color
        

    def draw(self, screen):
        pg.draw.circle(screen, self.color, (self.position), self.radius)
