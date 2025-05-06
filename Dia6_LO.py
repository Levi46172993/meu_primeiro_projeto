"""
Sexto dia no curso do Luiz Otávio!!!
Oque aprendemos?:
*In(Usado para verificar se um elemento está presente em uma sequência.Retorna True se o elemento estiver presente, caso contrário retorna False.)

*Not in(Faz o oposto de in: verifica se um elemento não está presente em uma sequência.Retorna True se o elemento não estiver presente,
     e False se estiver.) 

#obs 1: strings em python são iteráveis, ou seja, significa que pode ser navegado item por item.(ou objeto por objeto)A contagem pelos objetos dessa 
    forma abaixo é chamada de contagem de índices.(012345678<-índices;1<-índice)A contagem de começa pelo "0" já uma contagem normal começa pelo "1"
#  012345678 
#  Marcosgay
# -987654321        
"""
#In
print('viado' in 'Marcos viado')# True
print(3 in [1, 2, 3, 4])      # True
print('chaves' in {'chaves': 1})# True (verifica as chaves)

#Not in  
print('Gay' not in 'Marcos viado') #True
print(5 not in [1,2,3,4]) #True
print('valor' not in {'chaves': 1}) #True (porque só olha as chaves, não os valores)

#obs 1 
nome = 'Marcosgay'
print(nome[2])
print(nome[-4])