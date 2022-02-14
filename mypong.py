import turtle
import pygame
# Adicionando musica de fundo
pygame.init()
pygame.mixer.music.set_volume(0.1)
musica = pygame.mixer.music.load("musica de fundo.mpeg")
pygame.mixer.music.play(-1)

# Adicionando som de colisao
colisao = pygame.mixer.Sound("collision2.mp3")
colisao.set_volume(0.2)

# Desenhar tela
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Mesa de tenis
table = turtle.Turtle()
table.shape("square")
table.color('green')
table.shapesize(stretch_wid=22, stretch_len=37)
table.penup()
table.goto(0, 0)

# Linha da mesa
line = turtle.Turtle()
line.shape("square")
line.color('white')
line.shapesize(stretch_wid=22, stretch_len=0.5)
line.penup()
line.goto(0, 0)

# Desenhar raquetes
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("red")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("blue")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)

# Desenhar bolas
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1

ball_2 = turtle.Turtle()
ball_2.speed(0)
ball_2.shape("square")
ball_2.color("white")
ball_2.penup()
ball_2.goto(0, 0)
ball_2.dx = -1
ball_2.dy = -1

# Pontuação
score_1 = 0
score_2 = 0

# Head-up display da pontuação
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 260)
hud.write("0 : 0", align="center", font=("Press Start 2P", 24, "normal"))

# Mover raquetes
def paddle_1_up():
    y = paddle_1.ycor()
    if y < 250:
        y += 20
    else:
        y = 250
    paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor()
    if y > -250:
        y += -20
    else:
        y = -250
    paddle_1.sety(y)

def paddle_2_up():
    y = paddle_2.ycor()
    if y < 250:
        y += 20
    else:
        y = 250
    paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor()
    if y > -250:
        y += -20
    else:
        y = -250
    paddle_2.sety(y)

# Mapeando as teclas
screen.listen()
screen.onkeypress(paddle_1_up, "w")
screen.onkeypress(paddle_1_down, "s")
screen.onkeypress(paddle_2_up, "Up")
screen.onkeypress(paddle_2_down, "Down")

while True:
    screen.update()

    # Movimentação da bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Movimentação bola 2
    ball_2.setx(ball_2.xcor() + ball_2.dx)
    ball_2.sety(ball_2.ycor() + ball_2.dy)

    # Bola 1
    # Colisão com parede superior
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        colisao.play()

    # Colisão com parede inferior
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        colisao.play()

    # Colisão com parede esquerda
    if ball.xcor() < -390:
        score_2 += 1
        ball.color('blue')
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center",
                  font=("Press Start 2P", 24, "normal"))
        ball.dx *= -1
        colisao.play()

    # Colisão com parede direita
    if ball.xcor() > 390:
        score_1 += 1
        ball.color('red')
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center",
                  font=("Press Start 2P", 24, "normal"))
        ball.dx *= -1
        colisao.play()

    # Colisão com raquete 1
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() <
       paddle_2.ycor() + 40 and ball.ycor() > paddle_2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        ball.color("red")
        colisao.play()

    # Colisão com raquete 2
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() <
       paddle_1.ycor() + 40 and ball.ycor() > paddle_1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        ball.color("blue")
        colisao.play()

    # Bola 2
    # Colisão parede superior
    if ball_2.ycor() > 290:
        ball_2.sety(290)
        ball_2.dy *= -1
        colisao.play()

    # Colisão parede inferior
    if ball_2.ycor() < -290:
        ball_2.sety(-290)
        ball_2.dy *= -1
        colisao.play()

    # Colisão com parede esquerda
    if ball_2.xcor() < -390:
        ball_2.dx *= -1
        ball_2.color('blue')
        score_2 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center",
                  font=("Press Start 2P", 24, "normal"))
        colisao.play()

    # Colisão com parede direita
    if ball_2.xcor() > 390:
        ball_2.dx *= -1
        ball_2.color('red')
        score_1 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center",
                  font=("Press Start 2P", 24, "normal"))
        colisao.play()

    # Colisão com raquete 1
    if (ball_2.xcor() > 340 and ball_2.xcor() < 350) and (ball_2.ycor() <
       paddle_2.ycor() + 40 and ball_2.ycor() > paddle_2.ycor() - 40):
        ball_2.setx(340)
        ball_2.dx *= -1
        ball_2.color('red')
        colisao.play()

    # Colisão com raquete 2
    if (ball_2.xcor() < -340 and ball_2.xcor() > -350) and (ball_2.ycor() <
       paddle_1.ycor() + 40 and ball_2.ycor() > paddle_1.ycor() - 40):
        ball_2.setx(-340)
        ball_2.dx *= -1
        ball_2.color("blue")
        colisao.play()
        
