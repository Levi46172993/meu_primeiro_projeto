"""
Setimo dia no curso do Luiz Otávio(Primeira semana)
Oque aprendemos?:
*Interpolação básica de strings(Um jeito diferente se inserir variaveis numa str, tipo um .format.[achei bem ínutil e dificil de se inserir]
    Se tiver somente uma variavel não precisa de parentêses{mas se quiser pode-se usar parênteses.})

*Formatação de strings com f-strings
 (s - string
 d - int
 f - float
 .<número de dígitos>f
 x ou X - Hexadecimal
 (Caractere)(><^)(quantidade)
 > - Esquerda
 < - Direita
 ^ - Centro
 = - Força o número a aparecer antes dos zeros
 Sinal - + ou -
 Ex.: 0>-100,.1f){Bagulho inutil}

 *Fatiamento de strings(É como se você estivesse cortando uma carne(Mas na verdade você vai cortar um objeto), você escolhe,
    aonde começa a cortar(Mas primeiro precisa colocar dois pontos entre os dois números{Dentro de colchetes}), o tamanho(O tamanho é 
    representado por um número) da carne e o final onde você termina.(O final tbm é representado por um número)de cortar.O primeiro número 
    a ser coloca vai ser o começo na hora de cortar a carne(Objeto) o segundo número será o final onde a carne(Objeto) vai parar de ser cortada.)

#Obs 1:O fatiamento de strings usa a numeração de strings iteráveis ou seja navegar objeto por objeto(elemento por elemento).Pode se usar os números
    negativos também.
     
#Obs 2:Se um dos dois números de fatiamento não aparecer o python vai pegar do ínicio (ou do final dependendo de qual dos dois está faltando) e 
    vai continuar até o outro número.(se tiver)Se não tiver nenhum dos dois números ele vai pegar a frase inteira.

#Obs 3:Para parar aonde você desejar terá que colocar 1+ no número final.Ex:na palavra 'Ola mundo' Se você quiser começar do 'O' e terminar no 'u'
    se colocar exatamente o número deles a mensagem vai sair 'Ola m' e não 'Ola mu'ou seja se 'u' for 7 terá de colocar 8 para sair 'Ola mu'.

*Len(Conta(Sem ser na forma de índice que começa pelo "0" ) a quantidade de caracteres numa string)

*Passo(Uma outra função de fatiamento de strings.(Eu só não coloquei junto porque a explicação já está muito grande)Se coloca um segundo ":" e um 
    terceiro número, esse número indica a quantidade de letras que ele irá pular(ou seja Pula um mostra outro na tela e por aí vai até a numeração
     do segundo número.(que é o final)))
"""
#Interpolação básica de strings
nome1 = 'marcos'
sobrenome = 24
variavel_1 = '%s tem uma idade de %i (ou seja idade de gay)' % (nome1, sobrenome)
print(variavel_1)

nome2 = 'marcos'
variavel_2 = '%s é gay ' % nome2
print(variavel_2)

#Formatação de strings com f-strings
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')

#Fatiamento de strings 
string = 'ola mundo'
print(string[4:9])

#Obs 2
string = 'Marcos viado'
print(string[:])
print(string[ :12])#Há 11 caracteres no FATO que 'Marcos viado'
print(string[0 : ])

#Obs 3 
string = 'Exemplo muito FODA'#Há 17 caracteres nessa frase 
print(string[0:17])#Exemplo muito FOD
print(string[0:18])

#Len
string = "Exemplo muito FODA"
print(len(string))
print(len(string[4:-9]))

#Passo
string = 'Exemplo muito FODA'
print(string[0 :len(string) : 1])
print(string[0:18:2])#Pula um mostra outro na tela e por aí vai até a numeração do segundo número(que é o final)
print(string[0:])