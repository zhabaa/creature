import pygame as pg

from settings import SIZE, COLORS, WIDTH, HEIGHT
from functions import generate_dots, get_mouse_position as gmp
from creature import Creature


pg.init()
clock = pg.time.Clock()
clock.tick()

screen = pg.display.set_mode(SIZE)


def main():
    running = True

    dots = generate_dots(52)
    creature = Creature((WIDTH // 2, HEIGHT // 2), COLORS['White'])

    while running:
        clock.tick(60)
        screen.fill(COLORS["Black"])

        for event in pg.event.get():
            if event.type == pg.QUIT or (
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                running = False
            
            if event.type == pg.KEYDOWN and event.key == pg.K_F5:
                dots = generate_dots(52)

        mouse_position = gmp()
        creature.move(mouse_position)

        creature.draw(screen, dots)

        for dot in dots:
            dot.draw(screen)

        pg.display.flip()
    pg.quit()


if __name__ == "__main__":
    main()
