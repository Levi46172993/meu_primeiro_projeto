#desafio 24 QEF (desafio 28 NOG)
# from random import randint
# from time import sleep
# pensei  = randint(0,5)
# print('-=-' * 30)
# print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
# print('-=-' * 30)
# escolha = int(input('Que número eu pensei?: '))
# print('Processando...')
# sleep(2)#Vou falar sobre essa função do modulo time depois 
# if pensei == escolha:
#     print(f'Boa você acertou, o número que eu tinha pensado era {escolha}')
# else:
#     print(f'Que pena você errou, o número que eu tinha pensado era o {pensei}\n e você escolheu o {escolha} mas você pode tentar denovo')
# print('FIM')

# desafio 25 QEF (desafio 29 NOG)
# carro = float(input('Você estava dirigindo a quantos Km/h?: '))
# if carro > 80:
#     print('Infelizmente você vai ser multado por exceder o limite de 80Km/h.\nCada Km/h ultrupassado lhe custara R$7,00')
#     print(f'Então você terá que pagar {(carro - 80) * 7}R$')
# else:
#     print('Tudo certo já que você estava abaixo do limite de 80Km/h')

#desafio 26 QEF (desafio 30 NOG)
# num = int(input('Digite um número: '))
# par_ou_impar = num % 2
# if par_ou_impar == 0:
#     print('Seu número é PAR!')
# else:
#     print('Seu número é ÍMPAR!')

#desafio 27 QEF (desafio 31 NOG)
# km = float(input('Qual a distância em Km da sua viagem?: '))
# if km > 200 :
#     print(f'O preço da sua passagem relacionada a sua viagem de {km}Km será de {km * 0.45:.2f}R$')
# else:
#     print(f'O preço da sua passagem relacionada a sua viagem de {km}Km será de {km * 0.50:.2f}R$')
# print('Boa viagem :)')

#desafio 28 QEF (desafio 32 NOG)
# ano = int(input('Em que ano você está?: '))
# bissexto = ano % 4
# if bissexto == 0:#Código está errado
#     print('Você sabia que o ano em que você está é bissexto!')
# else:
#     print('Sabia que seu ano NÃO é bissexto!')

#desafio 29 QEF (desafio 33 NOG)
#Preguiça de fazer
pass
#desafio 30 QEF (desafio 34 NOG)
# salario = float(input('Me diga seu salário:R$ '))
# aumento_10 = (salario * 10 / 100) + salario
# aumento_15 = (salario * 15 / 100) + salario 
# if salario < 1250:
#     print(f'Parece que seu salário de {salario}R$ está um pouco abaixo do esperado.\nVocê receberá um aumento de 15%. Seu novo é salário {aumento_15:.2f}R$')     
# else:
#     print(f'Com o seu salário de {salario}R$ você receberá um aumento 10%.Seu novo salário é {aumento_10:.2f}R$')

#desafio 31 QEF (desafio 35 NOG)
# segmento_a = float(input('Digite um comprimento de reta: '))
# segmento_b = float(input('Digite outro comprimento de reta: '))
# segmento_c = float(input('Digite outro comprimento de reta: '))
# reta_1 = segmento_a + segmento_b
# reta_2 = segmento_a + segmento_c
# reta_3 = segmento_b + segmento_c
# if reta_1 > segmento_c and reta_2 > segmento_b and reta_3 > segmento_a:
#     print('De acordo com os comprimentos de reta que você mandou, é possível formar um triângulo!')
# else:
#     print('Parece que algum dos comprimentos que você mandou não é compatível para formar um triângulo')