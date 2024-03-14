# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
width, height = (640, 480)
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")

window.fill((0,0,0))
x = robot.get_width()
y = robot.get_height() + 15
for i in range(10):
    window.blit(robot, (x, y))
    x += robot.get_width()
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()