# # WRITE YOUR SOLUTION HERE:
import pygame
import math

pygame.init()
width, height = (640, 480)
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")

x = []
y = []
angle = []
speed = 1
num_robots = 10
radio = 150
const_x, const_y = width/2 - robot.get_width()/2, height/2 - robot.get_height()/2

window.fill((0, 0, 0))
for i in range(num_robots):
    # radians
    angle.append((2*math.pi/num_robots) * (i))
    x.append( const_x + math.cos(angle[i])*radio )
    y.append( const_y + math.sin(angle[i])*radio )
    window.blit(robot, (x[i], y[i]))
    # # degrees
    # angle.append((360/num_robots) * (i))
    # x.append( const_x + math.cos(math.radians(angle[i]))*radio )
    # y.append( const_y + math.sin(math.radians(angle[i]))*radio )
    # window.blit(robot, (x[i], y[i]))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    window.fill((0, 0, 0))
    for i in range(num_robots):
        # radians
        angle[i] += 0.01
        x[i] = const_x + math.cos(angle[i])*radio
        y[i] = const_y + math.sin(angle[i])*radio
        window.blit(robot, (x[i], y[i]))
        # # degrees
        # angle[i] += 0.8
        # x[i] = const_x + math.cos(math.radians(angle[i]))*radio
        # y[i] = const_y + math.sin(math.radians(angle[i]))*radio
        # window.blit(robot, (x[i], y[i]))
    pygame.display.flip()

    clock.tick(60)