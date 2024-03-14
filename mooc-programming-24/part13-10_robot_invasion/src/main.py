# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

pygame.init()

width, height = (640, 480)
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")

clock = pygame.time.Clock()

num_bots = 10
x, y = [], []
speed_x, speed_y = [1]*num_bots, [1]*num_bots

window.fill((0, 0, 0))
for i in range(num_bots):
    x.append(randint(0, width - robot.get_width()))
    y.append(randint(-2*height, -robot.get_height()))
    window.blit(robot, (x[i], y[i]))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    window.fill((0, 0, 0))

    for i in range(num_bots):
        y[i] += speed_y[i]
        if y[i] >= height - robot.get_height():
            y[i] = height - robot.get_height()
            if x[i] <= width/2 :
                speed_x[i] = -1
            else:
                speed_x[i] = 1
            speed_y[i] = 0
            x[i] += speed_x[i]
        if x[i] <= -robot.get_width() or x[i] >= width:
            x[i] = randint(0, width - robot.get_width())
            y[i] = randint(-2*height, -robot.get_height())
            speed_y[i] = 1
        window.blit(robot, (x[i], y[i]))
    
    pygame.display.flip()

    clock.tick(60)
