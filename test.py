import pygame
import math


pygame.init()


width, height = 800, 600
screen = pygame.display.set_mode((width, height))


point_x, point_y = width // 2, height // 2
point_radius = 10
speed = 100 / 60


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_x, mouse_y = pygame.mouse.get_pos()

    dx = mouse_x - point_x
    dy = mouse_y - point_y
    distance = math.hypot(dx, dy)

    if distance > 1:  # Проверяем, чтобы не происходило "демпфирование" при приближении
        # Вычисляем новые координаты точки
        point_x += dx / distance * speed
        point_y += dy / distance * speed

    # Отрисовка
    screen.fill((0, 0, 0))  # Заполнение фона черным цветом
    pygame.draw.circle(screen, (255, 0, 0), (int(point_x), int(point_y)), point_radius)  # Рисуем точку
    pygame.display.flip()  # Обновляем экран

    # Ограничиваем FPS
    pygame.time.Clock().tick(60)

# Завершение Pygame
pygame.quit()
