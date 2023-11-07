import os
os.system('cls')
import os
os.system('cls')
enter = "ckas"
## Colocar o inicar.

def adicionando():
    livro = input("Coloque o nome do livro: ")
    #livro.append(arquivo(txt))
    autor = input("Coloque o nome do autor: ")
    #autor.append(arquivo(txt))
    valor = float(input("Coloque o valor do livro: "))
    #valor.append(aquivo(txt))
    

def inicio():
    print ("//////Escolha o caminho//////")
    print ("1- Livros que Possui\n2- Lista de desejos\n3- Checar gastos")
    escolha = int(input("-"))

    if escolha == 1:
        #print(Lista_livros)    #manipulação de arquivos
        print("1- Adicionar \n2-remover")
        escolha2 = int(input("-"))
        if escolha2 == 1:
            adicionando()
        elif escolha2 == 2:
            removendo()
        
        
        

    elif escolha == 2:
        print()

    elif escolha ==3:
        print()

    else:
        print("Valor invalido")
        cetras = input("Prescine enter")
        if cetras != enter:
            inicio()
inicio()

def removendo():
    print("Qual produto você deseja remover: ")
    escolha_remover = int(input("-"))
    if escolha_remover == 1:
        print("nada ainda")

