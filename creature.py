import pygame as pg

from functions import calculate_distance
from settings import COLORS, LINE_WIDTH, WIDTH

class Creature:
    def __init__(self, position, color):
        self.position = list(position)

        self.color = color
        
        self.size = 13
        self.tentacles_radius = 5
        self.speed = 10
    
    def move(self, new_position):
        dx = new_position[0] - self.position[0]
        dy = new_position[1] - self.position[1]
        
        distance = calculate_distance(new_position, self.position)
        
        self.speed = distance * 3 / 144
        
        if distance > 1:
            self.position[0] += dx / distance * self.speed
            self.position[1] += dy / distance * self.speed
        
    def create_tentacle(self, screen, dots):
        for dot in dots:
            if calculate_distance(self.position, dot.position) < 150:
                pg.draw.line(screen, self.color, self.position, dot.position, LINE_WIDTH)
        
    def draw(self, screen, dots):
        pg.draw.circle(screen, self.color, self.position, self.size)
        self.create_tentacle(screen, dots)


