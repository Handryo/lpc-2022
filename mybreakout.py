import random

import pygame
from pygame.locals import *
from sys import exit
from random import choice

# Tamanho da tela
screen_higth = 700
screen_length = 650

# Posição da raquete
paddle_x = screen_length / 2 - 7.5 / 2
paddle_y = 650

# Posição da bola
ball_x = screen_length / 2
ball_y = screen_higth / 2

# Direções da bola
ball_up = -1
direction = [1, -1]
ball_side = random.choice(direction)

# Cores
yellow = (200, 200, 0)
green = (0, 240, 50)
red = (200, 0, 0)
blue = (0, 100, 200)
orange = (200, 100, 0)
white = (255, 255, 255)
gray = (200, 200, 200)

pygame.init()

#Criando a tela e um relogio
screen = pygame.display.set_mode((screen_length, screen_higth))
pygame.display.set_caption('MY BREAKOUT')
clock = pygame.time.Clock()

# Looping do jogo
while True:
    clock.tick((120))
    screen.fill((0,0,0))
    
    # Captando o evento de saída
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Controle da raquete
    if pygame.key.get_pressed()[K_RIGHT]:
        paddle_x += 5
    if pygame.key.get_pressed()[K_LEFT]:
        paddle_x -= 5

    # Desenhando a raquete
    paddle = pygame.draw.rect(screen, blue, (paddle_x, paddle_y, 40, 12.5))

    # Desenhando a bola
    ball = pygame.draw.circle(screen, green, (ball_x, ball_y), 7.5)

    # Desenhando a parede
    line_left = pygame.draw.line(screen, gray, (50, 0), (50, 700), 10)
    pygame.draw.line(screen, blue, (50, 640), (50, 673.5), 10)

    line_rigth = pygame.draw.line(screen, gray, (600, 0), (600, 700), 10)
    pygame.draw.line(screen, blue, (600, 640), (600, 672.5), 10)

    line_up = pygame.draw.line(screen, gray, (50, 0), (600, 0), 30)

    # Colisão da bola na parede
    if ball_x < 60:
        ball_side *= -1
    if ball_x > screen_length - 60:
        ball_side *= -1
    if ball_y < 30:
        ball_up *= -1
    if ball_y > screen_higth - 60:
        ball_up *= -1


    # Colisão da raquete na parede
    if paddle_x < 50:
        paddle_x += 5
    if paddle_x > screen_length - 90:
        paddle_x -= 5
    
    # Movimentação da bola
    '''ball_x -= ball_side
    ball_y += ball_up'''

    pygame.display.update()
