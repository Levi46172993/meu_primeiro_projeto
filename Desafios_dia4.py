#desafio 32 QEF (desafio 36 NOG)
pass

#desafio 33 QEF (desafio 37 NOG)
pass

#desafio 34 QEF (desafio 38 NOG)
# num_1 = int(input('Digite um número: '))
# num_2 = int(input('Digite outro número: '))
# if num_1 > num_2:
#     print(f'O valor {num_1} é maior que {num_2}!')
# elif num_1 < num_2:
#     print(f'O valor {num_2} é maior que {num_1}!')
# else: 
#     print('Eu não consigo identificar qual é maior e qual é menor, pois os dois números são iguais')
# desafio 35 QEF (desafio 39 NOG)
# from datetime import datetime
# ano = int(input('Me diga o seu ano de nascimento: '))
# idade = datetime.now().year - ano
# if idade > 18:
#     ida_ao_exercito = input(f'\033[0;35mParece que o dia de se alistar ao exercito passou por {abs(18 - idade)} ano(s), você já foi lá??:')
#     ida_ao_exercito = ida_ao_exercito.lower()
#     if ida_ao_exercito == 'n' or ida_ao_exercito == 'nn' or ida_ao_exercito == 'não' or ida_ao_exercito == 'nao':
#         print('\033[1;31mVOCÊ NÃO FOI AO EXERCITO????ENTÃO SERÁ PRESO!\033[m')
#     elif ida_ao_exercito == 's' or ida_ao_exercito == 'ss' or ida_ao_exercito == 'sim':
#         print('\033[0;36mMuito bem, parece que você fez seu dever como cidadão brasileiro\033[m')
#     else:
#         print('\033[1;31mISSO NÃO É UMA RESPOSTA VÁLIDA, VOCÊ VAI SER PRESO\033[m')
# elif idade == 18:
#     print('\033[1;31mESTÁ NA HORA DE IR SERVIR AO EXERCITO BRASILEIRO VÁ AGORA JOVEM GAFANHOTO\033[m')
# else:
#     print(f'\033[0;36mSe prepare para quando você for servir o exercito brasileiro falta somente {abs(18 - idade)} ano(s)\033[m')

#desafio 36 QEF (desafio 40 NOG)
# nota_1 = float(input('\033[4;35mMe diga sua primeira nota:\033[m '))
# nota_2 = float(input('\033[4;35mMe diga sua segunda:\033[m '))
# media = (nota_1 + nota_2) / 2
# if media < 5 :
#     print(f'\033[0;36mSua nota final foi {media}\033[m')
#     print('\033[1;31mREPROVADO\033[m')
#     print(f'\033[1;31m{media} SÉRIO?? VOCÊ FAZ MELHOR. ESTUDE MUITO MAIS\033[m')
# elif media < 6.9:
#     print(f'\033[0;36mSua nota final foi {media}\033[m')
#     print('\033[1;33mRECUPERAÇÃO\033[m')
#     print('\033[1;33mMEDIANO, ESTUDE MAIS\033[m')
# else:
#     print(f'\033[0;36mSua nota final foi {media}\033[m')
#     print('\033[1;32mAPROVADO\033[m')
#     print('\033[1;32mPARABÉNS\033[m')
#desafio 37 QEF (desafio 41 NOG)
# from datetime import datetime
# ano = int(input('\033[4;35mDigite o ano do seu nascimento para a confederação nacional de natação:\033[m '))
# idade = datetime.now().year - ano
# if idade <= 9:
#     print('\033[1;36mVOCÊ É DA CATEGORIA \033[4;36mNADADOR MIRIM\033[m')
# elif idade <= 14:
#     print('\033[1;36mVOCÊ É DA CATEGORIA \033[4;36mNADADOR INFANTIL\033[m')
# elif idade <= 19:
#     print('\033[1;36mVOCÊ É DA CATEGORIA \033[4;36mNADADOR JÚNIOR\033[m')
# elif idade == 20:
#     print('\033[1;36mVOCÊ É DA CATEGORIA \033[4;36mNADADOR SÊNIOR\033[m')
# else:
#     print('\033[1;36mVOCÊ É DA CATEGORIA \033[4;36mNADADOR MASTER\033[m')

#desafio 38 QEF (desafio 42 NOG)
# reta_1 = float(input('\033[1;36mDigite um tamanho de segmento de reta: '))
# reta_2 = float(input('\033[1;36mDigite outro tamanho de segmento de reta: '))
# reta_3 = float(input('\033[1;36mDigite outro tamanho de segmento de reta: '))
# if reta_1 + reta_2 > reta_3:
#     if reta_1 + reta_3 > reta_2:
#         if reta_2 + reta_3 > reta_1:
#             print('\033[m\033[1;32mSIM é possível formar um triângulo com essas retas que me informou\033[m')
#             if reta_1 == reta_2 == reta_3:
#                 print('\033[1;34mSeu triângulo é \033[4;34mEQUILÁTERO\033[m')
#             elif reta_1 != reta_2 and reta_1 != reta_3 and reta_2 != reta_3:
#                 print('\033[1;34mSeu triângulo é \033[4;34mESCALENO\033[m')
#             elif reta_1 == reta_2 and reta_1 != reta_3 or reta_1 != reta_2 and reta_1 == reta_3 or reta_3 == reta_2 and reta_1 != reta_3 or reta_1 != reta_2:
#                         print('\033[1;34mSeu triângulo é \033[4;34mISÓSCELES\033[m')
#             else:
#                 print('\033[1;31m\033[m4;31ERRO ):\033[m')
#         else:
#             print(f'\033[m\033[1;31mNÃO é possível formar um triângulo com as seguintes retas pois {reta_2} + {reta_3} não é maior que {reta_1}\033[m')
#     else:
#         print(f'\033[m\033[1;31mNÃO é possível formar um triângulo com as seguintes retas pois {reta_1} + {reta_3} não é maior que {reta_2}\033[m')
# else:
#     print(f'\033[m\033[1;31mNÃO é possível formar um triângulo com as seguintes retas pois {reta_1} + {reta_2} não é maior que {reta_3}')

# desafio 39 QEF(desafio 43 NOG)
# print('\033[1;36mDeixe-me calcular seu IMC\033[m')
# peso = float(input('\033[1;36mQual seu peso?: '))
# altura = float(input('Me diga sua altura em metros: '))
# imc = peso/(altura**2)
# if imc <= 18.5:
#     print(f'\033[m\033[0;37m{imc:.2f} Abaixo do peso!\033[m')
#     print('\033[0;37mEra bom dar uma ajustada nesse peso\033[m')
# elif imc < 25:
#     print(f'\033[m\033[1;32m{imc:.2f} Peso ideal/normal!')
#     print('Continue assim (;\033[m')
# elif imc < 30 :
#     print(f'\033[m\033[1;36m{imc:.2f} Sobrepeso!')
#     print(f'acima do normal!\033[m')
# elif imc < 40:
#     print(f'\033[m\033[1;33m{imc:.2f} Obesidade!')
#     print(f'\033[4;33mPREOCUPANTE\033[m')
# else:
#     print(f'\033[m\033[4;31m\033[1;31m{imc:.2f} OBESIDADE MÓRBIDA')
#     print(f'\033[4;31m\033[1;31mCUIDADO, RISCO DE MORTE\033[m')

#desafio 40 QEF (desafio 44 NOG)
# print('\033[1;34m=' * 10 , 'Supermercado Atacadão' , '=' * 10)
# valor = float(input('Qual foi o valor da sua compra?:R$'))
# print('''Formas de pagamento
# [ 1 ] á vista dinheiro/cheque
# [ 2 ] á vista no cartão
# [ 3 ] 2x no cartão SEM JUROS
# [ 4 ] 3x ou mais no cartão COM JUROS''')
# forma_de_pagamento = int(input('\033[1;36mQual das opções?: '))
# desconto10 = (valor * 10 / 100) 
# desconto10 = valor - desconto10
# desconto5 = (valor * 5 / 100)
# desconto5 = valor - desconto5
# if forma_de_pagamento == 1:
#     print(f'\033[m\033[1;32mComo você escolheu pagar á vista em dinheiro, ganhará um desconto de 10%\nEntão sua compra fica no preço de R${desconto10:.2f}\033[m')
# elif forma_de_pagamento == 2:
#     print(f'\033[m\033[1;32mComo você escolheu pagar á vista no cartão, ganhará um desconto de 5% em sua compra\nO valor da sua compra será de R${desconto5:.2f}\033[m')
# elif forma_de_pagamento == 3:
#     print(f'\033[m\033[1;32mPagando parcelado em 2X fica totalmente sem juros, ficando a primeira parcela em R${valor / 2:.2f}\033[m')
# elif forma_de_pagamento == 4:
#     parcelas = int(input('\033[m\033[1;36mQuantas parcelas?: '))
#     print(f'\033[m\033[1;32mSua primeira parcela vai ser no preço de R${((valor / parcelas)* 20 / 100) + valor / parcelas:.2f} COM JUROS e no final você terá pagado R${(valor *  20 / 100) + valor}')
# else:
#     print('\033[m\033[1;31mEsta não é uma forma de pagamento válida por favor tente novamente\033[m')

#desafio 41 QEF(desafio 45 NOG)
# from time import sleep
# from random import randint
# print('''\033[1;34mSuas opções
# [ 0 ] PEDRA
# [ 1 ] PAPEL
# [ 2 ] TESOURA''')
# jogada_usuario = int(input('Qual sua jogada?: '))
# jogada_computador = randint(0,2)
# if jogada_usuario >= 3:
#     print('\033[m\033[1;31mEstá não é uma resposta válida, por favor tente novamente\033[m')
# jogadas = ['PEDRA' , 'PAPEL' , 'TESOURA']
# if jogada_usuario < 3:           
#     print('JO') 
#     sleep(0.5)
#     print('KEN')
#     sleep(0.5)
#     print('PO!!!')
#     print('\033[1;36m-=-' * 10)
#     print(f'''Computador jogou {jogadas[jogada_computador]}
# Jogador jogou {jogadas[jogada_usuario]}''')
#     print('-=-' * 10)
# if jogada_computador == 0:
#     if jogada_usuario == 0:
#         print('\033[m\033[1;33mEMPATE\033[m')
#     elif jogada_usuario == 1:
#         print('\033[m\033[1;32mJOGADOR VENCE\033[m')
#     elif jogada_usuario == 2:
#         print('\033[m\033[1;31mCOMPUTADOR VENCE\033[m')
# elif jogada_computador == 1:
#     if jogada_usuario == 0:
#         print('\033[m\033[1;31mCOMPUTADOR VENCE\033[m')
#     elif jogada_usuario == 1:
#         print('\033[m\033[1;33mEMPATE\033[m')
#     elif jogada_usuario == 2:
#         print('\033[m\033[1;32mJOGADOR VENCE\033[m')
# elif jogada_computador == 2:
#     if jogada_usuario == 0:
#         print('\033[m\033[1;32mJOGADOR VENCE\033[m')
#     elif jogada_usuario == 1:
#         print('\033[m\033[1;31mCOMPUTADOR VENCE\033[m')
#     elif jogada_usuario == 2:
#         print('\033[m\033[1;33mEMPATE\033[m')