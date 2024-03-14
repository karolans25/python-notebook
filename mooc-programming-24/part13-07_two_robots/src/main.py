# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

pygame.init()

width, height = (640, 480)
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")

clock = pygame.time.Clock()

window.fill((0, 0, 0))
x = []
y = []
speed = []
for i in range(2):
    # x.append(randint(0, width - 50))
    x.append(0)
    y.append(50 + 120*i)
    speed.append(i + 1)
    window.blit(robot, (x[i], y[i]))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    window.fill((0, 0, 0))
    
    for i in range(2):
        if x[i] < 0 or x[i] > width - robot.get_width():
            speed[i] = -1*speed[i]
        x[i] += speed[i]
        window.blit(robot, (x[i], y[i]))
    
    pygame.display.flip()

    clock.tick(60)
