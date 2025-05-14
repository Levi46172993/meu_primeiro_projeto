# """
# Segundo dia no curso em vídeo do Guanabara!!!
# Oque aprendemos?:
# *Fatiamento de strings(Ja fiz um topico sobre isso, olhar nas aulas do Luiz Ótavio)

# Obs 1 :Tudo dentro de colchetes é considerado uma lista igual no desafio 15 e 16 e pode ser navegado 

# *Choice(Choice é uma função do modulo "random" que escolhe de forma aleatoria algo dentro de uma lista
#     (Eu acho que só pode ser usado em uma lista))

# *Analise de string

# #Len(Ja fiz um topico sobre isso olhar nas aulas do Luiz Ótavio)
# #.count(O ".count" conta a quantidade de vezes que uma certa letra(Objeto) aparecerá.É possivel fazer 
#     um fatiamento dentro do ".count")
# #.find(O ".find" encontra objetos dentro de uma string e lhe diz em que momento começou a numeração deles.
#     Se o ".find" não encontrar os objetos descritos ele não vai dizer "False" pois não é uma função
#     Boolena.Se ele não econtrar nada o false dele indicado como um "-1")
# #In(Ja fiz um topico sobre isso olhar nas aulas do Luiz Ótavio)

# *Transformação de string

# #.replace(Troca uma letra frase etc por outra(Igual no minecraft))
# #.upper(Upper é um método(Vou aprender mais para frente sobre isso) que deixa um ou mais objetos que 
#      estejam em minúsculo em maiúsculo.Colocar parênteses despois de digitar ".upper" é essencial
#       e eu não posso deixar sem)
# #.lower(O inverso de ".upper"(É também um método) deixa todos os objetos de maiúsculos para minúsculos.
#     Colocar parênteses também é essencial)
# #.capitalize(Faz com que todos os objetos fiquem minúsculos, e somente a primeira letra seja maiúscula.
#     Também é essencial os parênteses)
# #.title(Faz com que cada letra inicial da palavra seja maiúscula ao invés de que só a primeira letra 
#    seja maiúscula. também é essencial os parênteses)
# #.strip(Remove espaços desnecessarios no inicio e no fim da str, não remove espaços no meio da string.
#     Também é essencial os parênteses)
#     #rstrip(Apaga somente os espaços desnecessarios no fim da string ou seja a direita )
#     #lstrip(Apaga espaços desnecessarios no inicio da string ou seja a esquerda)

# *.split(Separa as palavras em ordem e numa lista(Provavelmente todas as funções com ponto precisa de
#     parênteses))
#     #.join(Junta os elementos a partir de um separador tipo "-"(Parecido com um topico de separador no 
#     curso do Luiz Ótavio))
# """
#choice
from random import choice
lista = [1,2,3,4,5,6,7,9]
print(choice(lista))

#Analise de string - .count
frase = 'Marcos viado'
print(frase.count('o'))#2
print(frase.count('o' , 6 , 13))#1

#Analise de string - .find
frase = 'Curso em vídeo python'
print(frase.find('víde'))
print(frase.find('marcos viado, ai meu cuzinho'))

#Transformação - .replace
frase = 'Função parecida com, um comando do minecraft'
print(frase.replace('Função parecida com' , 'Marcos viado'))

#Tranformação - .upper
frase = 'Exemplo Muito Foda'
print(frase.upper())

#Transformação - .lower
frase = 'EXEMPLO MUITO FODA'
print(frase.lower())

#Transformação - .capitalize
frase = 'eXeMpLo mUiTo fOdA'
print(frase.capitalize())

#Transformação - .title
frase = 'eXeMpLo mUiTo fOdA'
print(frase.title())

#Transformação - .strip
frase = '       Marcos        viado                '
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())

#.split
frase = 'Curso em vídeo python'
print(frase.split())
# print('-'.join())



