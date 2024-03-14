# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

pygame.init()

width, height = (640, 480)
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")

clock = pygame.time.Clock()

window.fill((0, 0, 0))
x, y = [], []
speed = []

num_bots = 2
to_right, to_left, to_up, to_down = [False]*num_bots, [False]*num_bots, [False]*num_bots, [False]*num_bots

for i in range(num_bots):
    x.append(0) if i%2 == 0 else x.append(width - robot.get_width())
    y.append((height/3) * (i+1) - robot.get_height()/2)
    speed.append(1)
    window.blit(robot, (x[i], y[i]))

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left[0] = True
            if event.key == pygame.K_RIGHT:
                to_right[0] = True
            if event.key == pygame.K_UP:
                to_up[0] = True
            if event.key == pygame.K_DOWN:
                to_down[0] = True
            if event.key == pygame.K_a:
                to_left[1] = True
            if event.key == pygame.K_d:
                to_right[1] = True
            if event.key == pygame.K_w:
                to_up[1] = True
            if event.key == pygame.K_s:
                to_down[1] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left[0] = False
            if event.key == pygame.K_RIGHT:
                to_right[0] = False
            if event.key == pygame.K_UP:
                to_up[0] = False
            if event.key == pygame.K_DOWN:
                to_down[0] = False
            if event.key == pygame.K_a:
                to_left[1] = False
            if event.key == pygame.K_d:
                to_right[1] = False
            if event.key == pygame.K_w:
                to_up[1] = False
            if event.key == pygame.K_s:
                to_down[1] = False

        if event.type == pygame.QUIT:
            exit()
    
    window.fill((0, 0, 0))
    for i in range(2):
        if to_right[i] and x[i] <= width - robot.get_width():
            x[i] += 2
        if to_left[i] and x[i] >= 0:
            x[i] -= 2
        if to_up[i] and y[i] >= 0:
            y[i] -= 2
        if to_down[i] and y[i] <= height - robot.get_height():
            y[i] += 2
        window.blit(robot, (x[i], y[i]))
    pygame.display.flip()

    clock.tick(60)
