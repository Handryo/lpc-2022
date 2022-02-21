import random
from sys import exit

import pygame
from pygame.locals import *

# Tamanho da tela
screen_higth = 700
screen_length = 650

# Posição da raquete
paddle_x = screen_length / 2 - 7.5 / 2
paddle_y = 650
paddle_size = 40

# Posição da bola
ball_x = screen_length / 2
ball_y = screen_higth / 2

# Direções da bola
ball_up = -1
direction = [1, -1, 1, -1, 1, -1]
ball_side = random.choice(direction)

# Cores
yellow = (200, 200, 0)
green = (0, 153, 0)
red = (200, 0, 0)
blue = (0, 100, 200)
orange = (200, 100, 0)
white = (255, 255, 255)
gray = (200, 200, 200)
color_block = yellow
cont_blocks = 0

# Dimensão dos blocos:
rows = 8
columns = 14
padding_left = 5
padding_top = 5
block_width = 34
block_height = 10
block_list = []

# Criando a tela e a velocidade do jogo
screen = pygame.display.set_mode((screen_length, screen_higth))
pygame.display.set_caption('MY BREAKOUT')
clock = pygame.time.Clock()

# Placar
pontos = 0
decimal = 0
centena = 0
chance = 1
pygame.font.init()
fonte = pygame.font.SysFont('Arial', 72, True, False)

# Variavel de controle de velocidade
block_red = 0
block_orange = 0

# Criando a parede de tijolos
for row in range(rows):
    for col in range(columns):
        x = ((padding_left * col) + padding_left) + (block_width * col)
        y = ((padding_top * row) + padding_top) + (block_height * row)
        block = pygame.Rect(x + 50, y + 150, block_width, block_height)
        block_list.append(block)

while True:
    clock.tick(120)
    screen.fill((0, 0, 0))

    # Atualização do placar
    if pontos > 9:
        pontos = 0
        decimal += 1
        if decimal > 9:
            decimal = 0
            centena += 1

    mensage_1 = f'{centena}{decimal}{pontos}'
    mensage_2 = f'{chance}'

    text_1 = fonte.render(mensage_1, True, white)
    text_2 = fonte.render(mensage_2, True, white)

    # Comando de saída
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
    paddle = pygame.draw.rect(screen, blue, (paddle_x, paddle_y, paddle_size, 12.5))
    # Desenhando a bola
    ball = pygame.draw.rect(screen, white, (ball_x, ball_y, 7.5, 7.5))

    # Desenhando tijolos
    for block in block_list:
        if 153.5 < block[1] < 183.5:
            pygame.draw.rect(screen, red, block)
        if 183.5 < block[1] < 213.5:
            pygame.draw.rect(screen, orange, block)
        if 213.5 < block[1] < 243.5:
            pygame.draw.rect(screen, green, block)
        if 243.5 < block[1] < 273.5:
            pygame.draw.rect(screen, yellow, block)

    # Desenhando a parede
    pygame.draw.line(screen, gray, (50, 0), (50, 700), 10)  # lado esquerdo
    pygame.draw.line(screen, red, (50, 153.5), (50, 183.5), 10)
    pygame.draw.line(screen, orange, (50, 183.5), (50, 213.5), 10)
    pygame.draw.line(screen, green, (50, 213.5), (50, 243.5), 10)
    pygame.draw.line(screen, yellow, (50, 243.5), (50, 273.5), 10)
    line_blue_rigth = pygame.draw.line(screen, blue, (50, 640), (50, 673.5), 10)

    pygame.draw.line(screen, gray, (600, 0), (600, 700), 10)  # lado direito
    pygame.draw.line(screen, red, (600, 153.5), (600, 183.5), 10)
    pygame.draw.line(screen, orange, (600, 183.5), (600, 213.5), 10)
    pygame.draw.line(screen, green, (600, 213.5), (600, 243.5), 10)
    pygame.draw.line(screen, yellow, (600, 243.5), (600, 273.5), 10)
    line_blue_left = pygame.draw.line(screen, blue, (600, 640), (600, 673.5), 10)

    pygame.draw.line(screen, gray, (50, 0), (600, 0), 30)  # linha superior

    # Colisão da bola na parede
    if ball_x < 60:
        ball_side *= -1
    if ball_x > screen_length - 60:
        ball_side *= -1
    if ball_y < 30:
        ball_up *= -1
    if ball_y > screen_higth - 20:
        ball_x = screen_higth / 2
        ball_y = screen_length / 2
        chance += 1

    # Colisão da raquete na parede
    if paddle.colliderect(line_blue_left):
        paddle_x -= 5
    if paddle.colliderect(line_blue_rigth):
        paddle_x += 5

    # Colisão bola na raquete
    if ball.colliderect(paddle):
        ball_up *= -1
        ball_side = 1 * random.choice(direction)

    # Colisão bola no tijolo
    for block in block_list:
        if ball.colliderect(block):

            # Colisão tijolo vermelho
            if 153.5 < block[1] < 183.5 and ball_y > 0:
                if ball_side > 0:
                    ball_side *= 1
                if ball_side < 0:
                    ball_side *= 1
                block_red += 1
                ball_side = -1 * random.choice(direction)
                block_list.remove(block)
                pontos += 7
                if block_red == 1:
                    ball_up *= -1.5

            # Colisão tijolo laranja
            if 183.5 < block[1] < 213.5 and ball_y > 0:
                if ball_side > 0:
                    ball_side *= 1
                if ball_side < 0:
                    ball_side *= 1
                block_orange += 1
                block_list.remove(block)
                pontos += 5
                if block_orange == 1:
                    ball_up *= -1.5

            # Colisão tijolo verde
            if 213.5 < block[1] < 243.5 and ball_y > 0:
                if ball_side > 0:
                    ball_side *= 1
                if ball_side < 0:
                    ball_side *= 1
                ball_up *= -1
                block_list.remove(block)
                pontos += 3

            # Colisão tijolo amarelo
            if 243.5 < block[1] < 273.5 and ball_y > 0:
                if ball_side > 0:
                    ball_side *= 1
                if ball_side < 0:
                    ball_side *= 1
                ball_up *= -1
                block_list.remove(block)
                pontos += 1

            # Bola caindo teto para baixo
            # Colisão tijolo vermelho
    for block in block_list:
        if ball.colliderect(block) :
            if 153.5 < block[1] < 183.5 and ball_y < 0:
                if ball_side > 0:
                    ball_side *= 1
                if ball_side < 0:
                    ball_side *= 1
                ball_up = -1
                block_list.remove(block)
                pontos += 7

            # Colisão tijolo laranja
            if 183.5 < block[1] < 213.5 and ball_y < 0:
                if ball_side > 0:
                    ball_side *= 1
                if ball_side < 0:
                    ball_side *= 1
                ball_up = -1
                block_list.remove(block)
                pontos += 5

            # Colisão tijolo verde
            if 213.5 < block[1] < 243.5 and ball_y < 0:
                if ball_side > 0:
                    ball_side *= 1
                if ball_side < 0:
                    ball_side *= 1
                ball_up = -1
                block_list.remove(block)
                pontos += 3

            # Colisão tijolo amarelo
            if 243.5 < block[1] < 273.5 and ball_y < 0:
                if ball_side > 0:
                    ball_side *= 1
                if ball_side < 0:
                    ball_side *= 1
                ball_up = -1
                block_list.remove(block)
                pontos += 1

    # Diminuição da raquete apos a bola ultrapassar o tijolo vermelho
    if ball_y < 153.5:
        paddle_size = 20

    # Movimento da bola
    ball_x += ball_side
    ball_y -= ball_up

    # Placar
    screen.blit(text_1, (100, 80))
    screen.blit(text_2, (60, 20))
    pygame.display.update()
