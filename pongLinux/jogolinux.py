import turtle
import os

"Criar tela"
tela = turtle.Screen()
tela.title("Ping Pong 1º INFO")
tela.bgcolor("blue")
tela.setup(width=800,height=600)
tela.tracer(0)
"Pontuação"
placar_a = 0
placar_b = 0

"Criar personagem"
"Jogador A"
jogador_a = turtle.Turtle()
jogador_a.shape("square")
jogador_a.color("white")
jogador_a.shapesize(stretch_wid=5, stretch_len=1)
jogador_a.penup()
jogador_a.goto(-350,0)
"Jodador B"
jogador_b = turtle.Turtle()
jogador_b.shape("square")
jogador_b.color("white")
jogador_b.shapesize(stretch_wid=5, stretch_len=1)
jogador_b.penup()
jogador_b.goto(350,0)
"Bola"
bola = turtle.Turtle()
bola.shape("circle")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = 0.2
bola.dy = -0.2
"Placar"
placar = turtle.Turtle()
placar.speed(0)
placar.color("white")
placar.penup()
placar.hideturtle()
placar.write("Jogador A: 0 Jogador B: 0", align="center", font=("Courier", 20, "normal"))

"Funções"
def jogador_a_up():
    y = jogador_a.ycor()
    y += 20
    y = jogador_a.sety(y)
def jogador_a_down():
    y = jogador_a.ycor()
    y -= 20
    y = jogador_a.sety(y)
def jogador_b_up():
    y = jogador_b.ycor()
    y += 20
    y = jogador_b.sety(y)
def jogador_b_down():
    y = jogador_b.ycor()
    y -= 20
    y = jogador_b.sety(y)
"Receber comando do teclado"
tela.listen()
tela.onkeypress(jogador_a_up, "w")
tela.onkeypress(jogador_a_down, "s")
tela.onkeypress(jogador_b_up, "Up")
tela.onkeypress(jogador_b_down, "Down")

while True:
    tela.update()

    "Movimentação da bola"
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)
    "Limites para bola"
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1
    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1
    if bola.xcor() >390:
        bola.goto(0, 0)
        bola.dx *= -1
        placar_a += 1
        placar.clear()
        placar.write(f'Jogador A: {placar_a} Jogador B: {placar_b}', align="center", font=("Courier", 20, "normal"))
        os.system("mpg123 ponto.mp3&")

    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1
        placar_b += 1
        placar.clear()
        placar.write(f'Jogador A: {placar_a} Jogador B: {placar_b}', align="center", font=("Courier", 20, "normal"))
        os.system("mpg123 ponto2.mp3&")

    "Colisão da bola com os jogadores"
    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < jogador_b.ycor() + 40 and bola.ycor() > jogador_b.ycor() -40):
        bola.setx(340)
        os.system("mpg123 bate.mp3&")
        bola.dx *= -1

    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < jogador_a.ycor() + 40) and (bola.ycor() > jogador_a.ycor() -40):
        bola.setx(-340)
        os.system("mpg123 rebate.mp3&")
        bola.dx *= -1

