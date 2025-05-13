"""
Primeiro dia (aprendendo algo novo) no curso em vídeo do Guanabara
Oque aprendemos?:
*Import(Ele importa funções secretas do python como o math(é só oq eu sei até agora).Ele importa funções
    Úteis da matematica como a raiz quadrada(sqrt), arredondar um número para cima(ceil) ou até arredondar
    um número para baixo(floor), importar só uma função(from math import X) entre outras coisas.

*Random(Random é um modulo e dentro desse modulo tem a função chamada random que faz com que a máquina escolha 
    um número aleátorio racional de 1 entre 0, mas dá para usar uma função chamada de radint que faz com que
     ela escolha um número inteiro que vc escolher. x , x  )

#Obs 1:O import acessa como se fosse uma biblioteca secreta de funções, e os livros dessa biblioteca são chamados
    de modulos ou seja o math é um modulo 
     
#Obs 1:Dá pra instalar outros modulos feitos por outros devs no pycharm como um modulo de emojis
"""
#Import
import math
num = int(input('Digite um número: '))
sqrt = math.sqrt(num)#Precisa do math.sqrt quando é importado o modulo em geral
print(f'A raiz quadrada de {num} é {sqrt}')

num1 = float(input('Digite um número com vírgula: '))
arredondado_cima = math.ceil(num1)
print(f'O seu número({num1}) com vírgula arredondado é considerado {arredondado_cima}')

num2 = float(input('Digite um número com vírgula:'))
arredondado_baixo = math.floor(num2)
print(f'O seu número({num2}) com vígula arredondado é considerado{arredondado_baixo}')

from math import sqrt#Fazer a importação desse jeito ocupa menos espaço na memoria do seu computador
num = int(input('Digite um número: '))
sqrt = sqrt(num)#não é necessario o math.sqrt quando só é importado uma ou poucas funções só é necessario a abreviação da função
print(f'A raiz quadrada de {num} é {sqrt}')

#Random
import random
num = random.random()
print(num)

import random
num = random.randint(1 , 100)
print(num)