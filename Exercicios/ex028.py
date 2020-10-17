from random import choice
n = int(input('Digite um número de 0 a 5: '))
list = [0, 1, 2, 3, 4, 5]
nc = choice(list)
if nc == n :
    print('Parabéns, você acertou!') 
else:
    print('O escolhido foi {}! O computador ganhou!'.format(nc))
