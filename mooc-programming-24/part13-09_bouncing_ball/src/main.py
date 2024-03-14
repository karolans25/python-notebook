# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
width, height = (640, 480)
window = pygame.display.set_mode((width, height))

ball = pygame.image.load("ball.png")

x, y = 0, 0
speed_x, speed_y = 2.5, 2.5
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(ball, (x, y))
    pygame.display.flip()

    if x < 0 or x > width - ball.get_width():
        speed_x = -speed_x
    if y < 0 or y > height - ball.get_height():
        speed_y = -speed_y
    x += speed_x
    y += speed_y

    clock.tick(60)
