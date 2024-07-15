import turtle 

#configuração de tempo
turtle.speed(0)

#configura a cor de fundo da tela
turtle.bgcolor('black')
#Lista de cores
colors=['white','grey']
for numbers in range(700):
#inicia o loop para repetir os comandos 700 vezes
    turtle.forward(numbers + 1)
    #move a caneta para frente aumentando uma unidade cada vez
    turtle.right(89)
    #gira 89 graus para a direita
    turtle.pencolor(colors[numbers%2])
    #faz a alternacia na lista de cores com base na interação
turtle.mainloop()