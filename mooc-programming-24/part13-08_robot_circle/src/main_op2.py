# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint
import math

pygame.init()

class Robot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("robot.png")
        self.rect = self.image.get_rect()
        self.speed = 0
        self.angle = 0
    
    def change_speed(self, s: float):
        self.speed = s

    def change_angle(self, angle: float):
        self.angle = angle

    def update(self):
        self.angle += self.speed

        # # radians
        self.rect.x = const_x + math.cos(self.angle)*radio
        self.rect.y = const_y + math.sin(self.angle)*radio

        # # degrees
        # self.rect.x = const_x + math.cos(math.radians(self.angle))*radio
        # self.rect.y = const_y + math.sin(math.radians(self.angle))*radio


width, height = (640, 480)
window = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

all_sprite_list = pygame.sprite.Group()
robot_list = pygame.sprite.Group()

x, y = [], []
speed_r, speed_d = 0.01, 0.7
num_robots = 10
radio = 150
const_x, const_y = width/2 - 50/2, height/2 - 100/2

window.fill((0, 0, 0))
for i in range(num_robots):
    robot = Robot()

    # radians
    robot.change_angle((2*math.pi/num_robots) * (i))
    robot.update()
    robot.change_speed(speed_r)

    # # degrees
    # robot.change_angle((360/num_robots) * (i))
    # robot.update()
    # robot.change_speed(speed_d)

    all_sprite_list.add(robot)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    all_sprite_list.update()
    window.fill((0, 0, 0))
    all_sprite_list.draw(window)
    pygame.display.flip()

    clock.tick(60)
