#desafio 1
# n1 = int(input('Digite um número: '))
# print(f'O antecessor de {n1} é {n1 - 1} e o seu sucessor é {n1 + 1 }')

#desafio 2
# n1 = int(input('Digite um número: '))
# print(f'O dobro de {n1} é {n1 * 2 } o seu triplo {n1 * 3 }\n e a sua raiz quadrada é {n1 **(1/2)} ')

#desafio 3
# n1 = int(input('Digite sua primeira nota: '))
# n2 = int(input('Digite sua segunda nota: '))
# print(f'A média entre {n1} e {n2} é {(n1 + n2) / 2 }')

#desafio 4 
# n1 = int(input('Digite uma distância em metros: '))
# print(f'Está distância convertida em centímetros é {n1 * 100 }cm\n e essa distância convertida em mílimetros é {n1 * 1000}mm')

#desafio 5
# n1 = int(input('Vou falar a tabuada do número que digitar: '))
# print( f'A tabuada do {n1} está abaixo' )
# print(f'{n1} x 1 = {n1 * 1}')     ,    print(f'{n1} x 2 = {n1 * 2}')
# print(f'{n1} x 3 = {n1 * 3}')     ,    print(f'{n1} x 4 = {n1 * 4}')
# print(f'{n1} x 5 = {n1 * 5}')     ,    print(f'{n1} x 6 = {n1 * 6}')
# print(f'{n1} x 7 = {n1 * 7}')     ,    print(f'{n1} x 8 = {n1 * 8}')
# print(f'{n1} x 9 = {n1 * 5}')     ,    print(f'{n1} x 10 = {n1 * 10}')

#desafio 6
# carteira = float(input('Digite quantos reais você tem em sua carteira: '))
# print(f'Com {carteira}R$(Reais) você conseguiria comprar {carteira / 3.27:.2f}$(Doláres)')

parede_altura = int(input('Digite a alutura da parede que quer pintar: '))
parede_largura = int(input('Digite a largura da parede que quer pintar: '))
area = parede_altura * parede_largura
print(f'A aréa dessa parede é igual a {area} e se cada litro de tinta cobre\numa aréa de 2m², então você precisará de { area  }')