"""
Quarto dia no curso do Luiz Otávio!!!
Oque aprendemos?:
*.Format(Uma forma diferente de inserir variaveis numa string.)

*Parâmetro nomeado(É quando você dá um nome para os objetos dentro da chamada da função ou da criação das funções.Apartir do momento que 
    você nomear um objeto tudo que vier depois(A direita do objeto) dele terá que ser nomeado também)

*Input(Coleta um dado que o úsuario inserir na tela.Tudo que sair do input é transformado em str, ou seja se você pedir para ele somar 10 + 10 
    o resultado sairia 1010 que dá numa concatenação.Para resolver isso você coloca int antes de input)

*if,elif e else('if' significa 'se', 'elif' significa 'se não se', 'else' significa 'se não'.Se for usar else tem que usar o if antes,
     se não não vai funcionar.Se for usar essa função é necessário estar indentado, ou seja, tem que ter o mesmo número de espaços(4 espaços)
    ou tabulação(1 tab) para funcionar corretamente.)

*Pass(Serve para indicar tipo "O código não está completo mas pode passar que eu completo depois"e não mostra erro na tela)

#Obs 1: Ellipsis é quase a mesma coisa que pass

#obs 2:O interpretador do python lê de cima para baixo e da esquerda para a direita.

*Operadores de comparação (relacionais)

# OP      Significado         Exemplo (True)
# >       maior               2 > 1
# >=      maior ou igual      2 >= 2
# <       menor               1 < 2
# <=      menor ou igual      2 <= 2
# ==      igual               'a' == 'a'
# !=      diferente           'a' != 'b'

"""
#.format
a = 'AAAAAAAAA' 
b = 'BBBBBBBBBB' 
c = 'CCCCCCCCCC' 
print('{},{},{} '.format(a,b,c)) 
print('{},{},{}'.format(c,b,a)) 
#Parâmetro nomeado

print('{nome1},{nome2},{nome3}'.format( nome1 = a,nome2 = b,nome3 = c,)) 
print('{},{},{nome3}'.format(a,b,nome3 = c)) 

#input
input('Qual seu nome?:Marcosgay')
n1 = input('Digite um número: ')#1 
n2 = input('Digite outro número: ')#5 
print(f'A soma dos dois número é {n1 + n2}') 
# O resultado dá 15 
n3 = int(input('Digite um número: ')) 
n4 = int(input('Digite outro número: ')) 
print(f'A soma dos dois número é {n3 + n4}') 
# O resultado dá 6 

#if, elif e else
entrada = input('Você quer "entrar" ou "sair"? ') 
if entrada == 'entrar': 
    print('Você entrou no sistema') 
elif entrada == 'sair': 
    print('Você saiu do sistema') 
else: 
    print('Você não digitou nem entrar e nem sair.') 

#pass
pass 

#Operadores de comparação (relacionais)
maior = 2 > 1
maior_ou_igual = 2 >= 2
menor = 1 < 2 
menor_ou_igual = 2 <= 2 
igual = 'a' == 'a' 
diferente = 'a' != 'b' 
print(maior)
print(maior_ou_igual)
print(menor)
print(menor_ou_igual)
print(igual)
print(diferente)