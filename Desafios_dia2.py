# desafio 18 QEF (desafio 22 NOG)
# nome1 = input('Digite seu nome completo: ')
# print(f'O seu nome somente com letras maiúsculas é:{nome1.upper()}')
# print(f'O seu nome somente com letras minúsculas é:{nome1.lower()}')
# nome2 = nome1.replace(' ' , '')
# print(f'A quantidade de letras no seu nome é:{len(nome2)} ')
# nome = nome1.split()
# print(f'A quantidade de letras que tem no seu primeiro nome é:{len(nome[0])}')

#desafio 19 QEF (desafio 23 NOG)
# num = input('Digite um número com 4 dígitos: ')
# print(f'Unidade:{num[3]}')
# print(f'Dezena:{num[2]}')#Jeito com str porém da erro se for com menos de um dígito
# print(f'Centena:{num[1]}')
# print(f'Milhar:{num[0]}')

# desafio 19,5 QEF (desafio 23,5 NOG)
# num = int(input('Digite um número com 4 dígitos: '))
# u = num // 1 %10
# d = num // 10 % 10
# c = num // 100 % 10
# m = num // 1000 % 10
# print(f'Unidade:{u}')
# print(f'Dezena:{d}')#Jeito matématico de fazer que não dá erro
# print(f'Centena:{c}')
# print(f'Milhar:{m}')


#desafio 20 QEF (desafio 24 NOG)
# cidade = input('Digite o nome da cidade que você nasceu: ')
# cidade = cidade.title()
# cidade = cidade.strip()
# cidade1 = cidade.split()
# if 'Santo' in cidade1[0]:
#     print(f'A cidade {cidade} contém a palavra Santo no primeiro nome!')
# else:
#     print(f'A cidade {cidade} NÃO tem a palavra Santo no primeiro nome!')

# desafio 21 QEF (desafio 25 NOG)
# nome = input('Digite seu nome completo: ')
# nome = nome.title()
# if 'Silva' in nome:
#     print('Parece que seu nome contém Silva')
# else:
#     print(f'Parece que seu nome não contém Silva ')

#desafio 22 QEF (desafio 26 NOG)
# frase = input('Digite uma frase motivacional: ').strip()
# letras_a = frase.count()
# quantas_a = letras_a.count('a')
# encontre_a = letras_a.find('a')
# encontre_a_pela_direita = letras_a.rfind('a')
# print(f'A Letra "a" aparece {quantas_a} vezes ')
# print(f'A primeira letra "a" aparece na {encontre_a + 1}° posição')
# print(f'O último "a" aparece na {encontre_a_pela_direita}° posição')

# #desafio 23 QEF (desafio 27 NOG)
# nome = input('Digite seu nome completo: ')
# nome = nome.split()
# print(f'O seu primeiro nome é:{nome[0]}')
# print(f'O seu último nome é:{nome[len(nome)-1]}')