#desafio 32
pass

#desafio 33
pass

#desafio 34
# num_1 = int(input('Digite um número: '))
# num_2 = int(input('Digite outro número: '))
# if num_1 > num_2:
#     print(f'O valor {num_1} é maior que {num_2}!')
# elif num_1 < num_2:
#     print(f'O valor {num_2} é maior que {num_1}!')
# else: 
#     print('Eu não consigo identificar qual é maior e qual é menor, pois os dois números são igual')
# desafio 35
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

#desafio 36
# nota_1 = float(input('\033[4;35mMe diga sua primeira nota:\033[m '))
# nota_2 = float(input('\033[4;35mMe diga sua segunda:\033[m '))
# media = (nota_1 + nota_2) / 2
# if media < 5 :
#     print(f'\033[0;36mSua nota final foi {media}\033[m')
#     print('\033[1;31mREPROVADO\033[m')
#     print(f'\033[1;31m{media} SÉRIO?? VOCÊ FAZ MELHOR. ESTUDE MAIS\033[m')
# elif media < 6.9:
#     print(f'\033[0;36mSua nota final foi {media}\033[m')
#     print('\033[1;33mRECUPERAÇÃO\033[m')
#     print('\033[1;33mMEDIANO, ESTUDE MAIS\033[m')
# else:
#     print(f'\033[0;36mSua nota final foi {media}\033[m')
#     print('\033[1;32mAPROVADO\033[m')
#     print('\033[1;32mPARABÉNS\033[m')
#desafio 37
from datetime import datetime
ano = int(input('\033[4;35mDigite o ano do seu nascimento para a confederação nacional de natação:\033[m '))
idade = datetime.now().year - ano
if idade <= 9:
    print('\033[1;36mVOCÊ É DA CATEGORIA \033[4;36mNADADOR MIRIM\033[m')
elif idade <= 14:
    print('\033[1;36mVOCÊ É DA CATEGORIA \033[4;36mNADADOR INFANTIL\033[m')
elif idade <= 19:
    print('\033[1;36mVOCÊ É DA CATEGORIA \033[4;36mNADADOR JÚNIOR\033[m')
    