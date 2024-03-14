# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

pygame.init()

class Robot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("robot.png")
        self.rect = self.image.get_rect()
        self.speed_x = 0
    
    def change_speed(self, x: int):
        self.speed_x = x

    def update(self):
        if self.rect.x < 0 or self.rect.x > width - 50:
            self.change_speed(self.speed_x * -1)
        self.rect.x += self.speed_x


width, height = (640, 480)
window = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

all_sprite_list = pygame.sprite.Group()
robot_list = pygame.sprite.Group()

for i in range(2):
    robot = Robot()
    # robot.rect.x = randint(0, width - 50)
    robot.rect.x = 0
    robot.rect.y = 50 + i*(120)
    robot.change_speed(i + 1)
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
