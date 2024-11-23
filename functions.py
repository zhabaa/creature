import pygame as pg
from random import randint
from settings import WIDTH, HEIGHT, COLORS
from dot import Dot


def get_mouse_position():
    position = pg.mouse.get_pos()
    
    return position


def calculate_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    
    return distance
    

def generate_coords():
    x = randint(0, WIDTH)
    y = randint(0, HEIGHT)
    
    return x, y

def generate_dots(amount):
    dots = list()
    
    for _ in range(amount):
        dots.append(Dot(*generate_coords(), COLORS['White']))
    
    return dots
