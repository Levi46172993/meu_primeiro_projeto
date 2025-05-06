"""
Terceiro dia no curso do Luiz otávio!!!
Oque aprendendemos?:
*Outras funcionalidades da adição e multiplicação

*concatenacao(Pode "somar" palavras e números que sejam considerados uma str.Pode também "multiplicar" palavras que sejam considerados uma string)

#a_dez_vezes = 'A' * 10

#tres_vezes_marcos_viado = 3 * 'Marcos viado'

*Precedência entre os operadores aritméticos(É a ordem em que cada função matemática irá funcionar,vou mostrar o ranking abaixo)

#1 (n + n)
#2 "**"(exponenciação ou Potenciação)
#3 "*"(Multiplicação), "/"(Divisão), //(Divisão inteira{ignora pontos e simplifica contas }),"%"(Resto da divisão).
#4 +, -

*Ellipsis(Geralmente indica que um código está incompleto e que a pessoa vai terminar o código mais tarde,
     mas pode fazer mais que isso, eu vou estudar mais na frente sobre suas outras funções.Não mostra nem um tipo de erro na tela )

*F-strings(Um jeito de inserir variáveis numa str colocando um "f" atrás das aspas e colocando a variável em chaves)

*Formatação de casas decimais(Você consegue diminuir o número de casas decimais de um número colocando exatamente assim 
    ":.xf(A letra x é so um exemplo não precisa colocar ele, mas o f precisa))
"""
#Outras funcionalidades da adição e da multiplicação
concatenacao = 'Marcos' + ' ' + 'Viado' 
print(concatenacao) 
a_dez_vezes = 'A' * 10 
tres_vezes_marcos_gay = 3 * 'marcosgay' 
print(a_dez_vezes) 
print(tres_vezes_marcos_gay) 

#Precedência entre os operadores aritméticos
print(1 + 1 ** 5 + 5) #7
print((1+1)** (5 + 5)) #1024 
print(2 * 2) #4
print(10 / 2 ) #5.0
print(12 // 10) #1
print(10 % 2) #0

#Ellipsis
print(...) 

#F-strings
n = 10 
print(f"Sabia que {n} é o tanto de rolas que o marcos viado engole de uma vez só") 

#Formatação de casas decimais
nn = 33.3453745324523495735 
print(f"Exemplo de formatação de casas decimais{nn}") 
print(f"Exemplo de formatação de casas decimais{nn:.1f}")
print(f"Exemplo de formatação de casas decimais{nn:.100f}") 
