#desafio 42 QEF (desafio 46 NOG)
#Contagem de fogos
# from time import sleep
# for c in range(10 , -1, -1):
#     print(c)
#     sleep(1)
# print('CABUUMMMM')

#desafio 43 QEF (desafio 47 NOG)
#Contagem de pares
# for c in range(2 , 51 , 2):
#     print(c , end=' ')
# print('Acabou!')

#desafio 44 QEF (desafio 48 NOG)
#soma de numeros ímpares
# cont = 0
# soma = 0
# for c in range(1 , 501 , 2):
#     if c % 3 == 0:
#         soma += c 
#         cont += 1
# print(f'A soma dos {cont} valores solicitados é {soma}!')
# print(f'A soma de todos os {cont} valores solicitados é {soma}')

#desafio 45 QEF (desafio 49 NOG)
#tabuada v2.0
# num = int(input('Digite um número para ver sua tabuada: '))
# for c in range(1 , 11):
#     print(f'{num} X {c:2} = {num * c}')

#desafio 46 QEF (desafio 50 NOG)
#soma de números ímpares
# cont = 0
# soma = 0
# for c in range(1 , 7):
#     num = int(input(f'Digite o {c}° número: '))
#     if num % 2 == 0:
#         cont+= 1
#         soma += num
# print(f'A soma dos {cont} números PARES que me informou é {soma}')

#desafio 47 QEF (desafio 51 NOG)
#Progressão Áritmetica(PA)
# print('==' * 17)
# print('      10 TERMOS DE UMA PA      ')
# print('==' * 17)
# prt = int(input('Primeiro termo: '))
# raz = int(input('Razão: '))
# dec = prt + (11 - 1) * raz
# for c in range(prt , dec , raz):
#     print (c , end=' -> ')
# print('ACABOU')

#desafio 48 QEF (desafio 52 NOG)
#Números primos
num = int(input('Digite um número: '))
sla = 1 + (num - 1) * 1
for c in range(1 , sla + 1):
    if num % c == 0:
        print(c , end=' ')
            