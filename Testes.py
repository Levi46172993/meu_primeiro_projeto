import random
import turtle
import time

def gerar_estrelas(qtd=5000, largura=800, altura=700):
    estrelas = set()
    while len(estrelas) < qtd:
        x = random.randint(-largura//2, largura//2)
        y = random.randint(-altura//2, altura//2)
        estrelas.add((x, y))
    return estrelas

def desenhar_estrelas_uma_a_uma(estrelas):
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color("yellow")
    for x, y in estrelas:
        t.penup()
        t.goto(x, y)
        t.pendown()
        for _ in range(5):
            t.forward(15)
            t.right(144)
        turtle.update()
        time.sleep(1)

def mostrar_surpresa_turtle():
    mensagem = "Surpresa, você é gay! ⭐"
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(0, 150)
    t.color("white")
    t.speed(0)
    x, y = t.position()
    fonte = ("Arial", 24, "bold")
    texto = ""
    for i, letra in enumerate(mensagem):
        t.clear()
        texto += letra
        t.goto(x, y)
        t.write(texto, align="center", font=fonte)
        turtle.update()
        turtle.delay(100)
        time.sleep(0.15)
    t.goto(x, y)

def main():
    turtle.bgcolor("black")  # Fundo preto
    turtle.tracer(0, 0)
    estrelas = gerar_estrelas()
    desenhar_estrelas_uma_a_uma(estrelas)
    mostrar_surpresa_turtle()
    turtle.done()

if __name__ == "__main__":
    main()
