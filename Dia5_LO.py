"""
Quinto dia no curso do Luiz Otávio!!!
Oque aprendemos?:
#obs 1:Na programação, and, or e not são operadores lógicos usados para combinar ou inverter expressões booleanas (que resultam em True ou False). Eles são comumente usados em linguagens como Python, JavaScript, C, etc.

*and(Usado para combinar duas expressões.O "and" dá prefêrencia para false ou seja se tiver uma variavel como: variavel_0 = 1 , 0.A variavel vai se considerada False.)

#obs 2: Em python "1" é considerado True e "0" é considerado False

*or(Usado para combinar duas expressões.O "or" dá prefêrencia para true ou seja se tiver uma variavel como: variavel_1 = 1 , 0.
    A variavel vai ser considerada true.)

*not(O not é um operador lógico que inverte o valor de uma expressão booleana. Ou seja:Se algo é True, o not transforma em False.Se algo é False,
    o not transforma em True.É muito usado em condições para testar o oposto de algo.)
"""
#and
x = 10
y = 20
if x > 5 and y < 30:
    print("Ambas as condições são verdadeiras")
variavel_0  = 1 and 0
print(variavel_0)
#or
x = 10
y = 5
if x > 5 or y > 10:
    print("Pelo menos uma condição é verdadeira")
variavel_1 = 1 or 0 
print(variavel_1)
#not
ativo = False

if not ativo:
    print("O usuário não está ativo.")
#Aqui, ativo é False, então not ativo é True, e o bloco dentro do if será executado.
numero = 0

if not numero:
    print("O número é zero.")
# Em Python, o número 0 é considerado False. Então not 0 vira True.

itens = []

if not itens:
    print("A lista está vazia.")
#Listas vazias são False. Então not itens é True.