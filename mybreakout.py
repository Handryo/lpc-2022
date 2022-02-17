import pygame
from pygame.locals import *
from sys import exit

higth = 600
length = 400
x = length/2
y = 550

x_ball = length/2
y_ball = higth/2

# Dire
direct_1 = -1
direct_2 = 0

pygame.init()

screen = pygame.display.set_mode((length, higth))
pygame.display.set_caption('MY BREAKOUT')
clock = pygame.time.Clock()

while True:
    clock.tick((120))
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Controle da raquete
    if pygame.key.get_pressed()[K_RIGHT]:
        x += 3
    if pygame.key.get_pressed()[K_LEFT]:
        x -= 3

    # Desenhando a raquete
    paddle = pygame.draw.rect(screen, (160,100,0), (x, y, 50, 10))
    ball = pygame.draw.circle(screen, (100,30,30), (x_ball, y_ball), 7.5)

    # Colisão da bola na parede
    if y_ball > higth - 7.5:
        direct_1 = 1
    if y_ball < 0:
        direct_1 = -1
    if x_ball > length - 7.5:
        direct_2 = 1
    if x_ball < 0:
        direct_2 = -1

    # Colisão da raquete na parede
    if x < 0:
        x += 3
    if x > length - 50:
        x -= 3

    # Movimentando a bola
    y_ball -= direct_1
    x_ball -= direct_2

    # Colisão da bola na raquete
    if paddle.colliderect(ball):
        direct_1 += 0.5
        direct_2 -= 0.5

    pygame.display.update()
