import turtle

# Configuração da tela
tela = turtle.Screen()
tela.title("Demonstração Turtle")
tela.bgcolor("white")

# Configuração de velocidade da caneta
turtle.speed(7)

# Desenhar círculo preenchido
turtle.penup() #Levanta a caneta
turtle.goto(-200, 100) #Move para a posição da tela
turtle.pendown() #Abaixa a caneta
turtle.fillcolor("yellow") #Define a cor do preenchimento
turtle.begin_fill() #Inicia o preenchimento do desenho
turtle.circle(50) #Desenha um circulo com raio de 50 unid.
turtle.end_fill() #Finaliza o preenchimento

# Desenhar hexágono
turtle.penup() 
turtle.goto(0, 100)
turtle.pendown()

for _ in range(6): #Repete os comandos 6 vezes
    turtle.forward(70) 
    turtle.right(60) #Gira a caneta em 60 graus para a direita


# Função recursiva para desenhar uma espiral
def desenhar_espiral(turtle, tamanho):
    if tamanho >= 1:  # Condição de parada da recursão
        turtle.forward(tamanho)  # Avança com o tamanho atual
        turtle.right(90)  
        desenhar_espiral(turtle, tamanho - 5)  # Chamada recursiva com tamanho reduzido


#definições de caneta e local
turtle.penup()
turtle.goto(200, -100)
turtle.pendown()
turtle.left(90)

# Chamada inicial da função recursiva para desenhar a espiral
desenhar_espiral(turtle, 350)

turtle.hideturtle() #esconde a caneta
tela.mainloop() #permite que o usuário decida qnd fechar o quadro
