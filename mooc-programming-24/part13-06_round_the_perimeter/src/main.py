# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
width, height = (640, 480)
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")

x = 0
y = 0
velocity = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    if y == 0 and x < width - robot.get_width():
        x += velocity
    elif y < height - robot.get_height() and x == width - robot.get_width():
        y += velocity
    elif y == height - robot.get_height() and x > 0:
        x -= velocity
    elif y > 0 and x == 0:
        y -= velocity

    clock.tick(60)

