# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")

robot_x = 0
robot_y = 0

clock = pygame.time.Clock()

window.fill((0, 0, 0))
window.blit(robot, (robot_x, robot_y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1] 

            hit_x = robot_x <= mouse_x <= robot_x + robot.get_width()
            hit_y = robot_y <= mouse_y <= robot_y + robot.get_height()
 
            if hit_x and hit_y:
                robot_x = randint(0, width - robot.get_width())
                robot_y = randint(0, height - robot.get_height())
 
        if event.type == pygame.QUIT:
            exit()
 
        window.fill((0, 0, 0))
        window.blit(robot, (robot_x, robot_y))
        pygame.display.flip()
 