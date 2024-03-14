# WRITE YOUR SOLUTION HERE:
import pygame
import math
from datetime import datetime

RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

width, height = 640, 480
display = pygame.display.set_mode((width, height))

center = (width/2, height/2)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    display.fill((0, 0, 0))
    pygame.draw.circle(display, RED, (width/2, height/2), (height-90)/2, 5)
    pygame.draw.circle(display, RED, (width/2, height/2), 10)

    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%H:%M:%S")

    h = currentDateAndTime.hour
    m = currentDateAndTime.minute
    s = currentDateAndTime.second
    pygame.display.set_caption(currentTime)

    radio_h = height / 3.5
    radio_m = radio_s = height / 2.7
    
    # # Radians
    # angle_h = (math.pi / 6) * h + (math.pi / 360) * m - (math.pi/2)
    # angle_m = (math.pi / 30) * m + (math.pi / 1800) * s - math.pi/2
    # angle_s = (math.pi / 30) * s - math.pi/2 
    
    # x_h, y_h = math.cos( angle_h ) * radio_h , math.sin( angle_h ) * radio_h
    # x_m, y_m = math.cos( angle_m ) * radio_m , math.sin( angle_m ) * radio_m
    # x_s, y_s = math.cos( angle_s ) * radio_s , math.sin( angle_s ) * radio_s

    # Degrees
    angle_h = 30 * h + (30/60) * m - 90
    angle_m = 6 * m + (6/60) * s - 90
    angle_s = 6 * s - 90 
    
    x_h, y_h = math.cos( math.radians(angle_h) ) * radio_h , math.sin( math.radians(angle_h) ) * radio_h
    x_m, y_m = math.cos( math.radians(angle_m) ) * radio_m , math.sin( math.radians(angle_m) ) * radio_m
    x_s, y_s = math.cos( math.radians(angle_s) ) * radio_s , math.sin( math.radians(angle_s) ) * radio_s

    pygame.draw.line(display, BLUE, center, (center[0] + x_h, center[1] + y_h), 4)
    pygame.draw.line(display, BLUE, center, (center[0] + x_m, center[1] + y_m), 2)
    pygame.draw.line(display, BLUE, center, (center[0] + x_s, center[1] + y_s), 1)

    pygame.display.flip()
    clock.tick(1)
