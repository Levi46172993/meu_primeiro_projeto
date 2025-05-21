'''
Aula bônus do Guanabara de como colocar cores no terminal!
Fonte de texto         |          Cor do texto              |      Cor do fundo do texto
   0 -> nenhum         |             30->Branco             |                 40
   1 -> negrito        |             31->Vermelho           |                 41                                      
   4 -> Sobre underline|             32->Verde              |                 42
   7 -> Invertido      |             33->Amarelo            |                 43      #As mesma cores de  
.                      |             34->Azul               |                 44    #Cor do texto
.                      |             35->Roxo               |                 45                                                       
.                      |             36->Ciano              |                 46                 
.                      |             37->Cinza              |                 47
*Layout de Colocar cor no texto(print('\033[x;x;xmMarcos viado')
'''
print('\033[1;31;45mOlá,Mundo!')#Coloque no final da string \033[m para fazer com que a cor pare
print('                                                                                                            ')
print('\033[1;31;45mMarcos viado\033[m')#Esse layout no final faz com que a cor pare 
nome = 'Levi'
print(f'Muito prazer te conhecer \33[1;31m{nome}\033[m')
print(f'É um prazer te conhecer {'\033[4;32m'}{nome}{'\033[m'}')