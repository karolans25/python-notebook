# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

pygame.init()

width, height = (640, 480)
window = pygame.display.set_mode((width, height))

pygame.display.set_caption("Asteroids")

robot = pygame.image.load("robot.png")
rock = pygame.image.load("rock.png")

points = 0
game_font = pygame.font.SysFont("Arial", 24)

clock = pygame.time.Clock()

restart = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False

        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    if restart:
        points = 0

        # asteroids
        num_rocks = 20
        x_rk, y_rk = [], []
        speed_y_rk = [1]*num_rocks
        for i in range(num_rocks):
            x_rk.append(randint(0, width - rock.get_width()))
            if i != 0:
                y_rk.append(randint(y_rk[i-1] - rock.get_height() - height/3, y_rk[i-1] - rock.get_height()))
            else:
                y_rk.append(randint(-height/3, -rock.get_height()))
            window.blit(rock, (x_rk[i], y_rk[i]))

        # robot
        robot_x, robot_y = 0, height - robot.get_height()
        speed_robot_x = 2
        to_right, to_left = False, False
        window.blit(robot, (robot_x, robot_y))
        restart = False


    # asteroids
    for i in range(num_rocks):
        y_rk[i] += speed_y_rk[i]
        window.blit(rock, (x_rk[i], y_rk[i]))

    # robot
    if to_right and robot_x <= width - robot.get_width():
        robot_x += speed_robot_x
    if to_left and robot_x >= 0:
        robot_x -= speed_robot_x
    window.blit(robot, (robot_x, robot_y))

    for i in range(num_rocks):
        hit_x = robot_x - rock.get_width() <= x_rk[i] <= robot_x + robot.get_width()
        hit_y = y_rk[i] >= height - robot.get_height() - rock.get_height()
        if hit_x and hit_y:
            x_rk[i] = height + 1000
            y_rk[i] = height + 1000
            points += 1
        
        if y_rk[i] == height - 2*rock.get_height():
            restart = True

    text = game_font.render(f"Points: {points}", True, (255, 0, 0))
    window.blit(text, (width - 120, 10))

    pygame.display.flip()

    clock.tick(60)
