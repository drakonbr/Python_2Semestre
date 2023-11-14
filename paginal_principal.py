import os
os.system('cls')
enter = "ckas"


def visualizar():
    #autor.append(arquivo(txt)
    return

def adicionar():
    livro = input("\033[1;34;49mColoque o nome do livro:\033[m ")
    #livro.append(arquivo(txt))
    autor = input("\033[1;32;49mColoque o nome do autor:\033[m ")
    #autor.append(arquivo(txt))
    valor = float(input("\033[1;33;49mColoque o valor do livro:\033[m "))
    #valor.append(arquivo(txt))
    return "Livro Adicionado!"

def remover():
    print("\033[1;31;43mQual livro você deseja remover:\033[m ")
    return "Livro Removido!"

def atualizar():
    autor = input("\033[1;32;49mColoque o nome do autor:\033[m ")
    valor = float(input("\033[1;33;49mColoque o valor do livro:\033[m "))
    return "Livro Atualizado"

def desejar():
    return
def extrato():
    return

def inicio():
    print ("\033[1;32;49m//////Escolha o caminho//////\033[m")
    print ("1- \033[0;33;49mVisualizar Livros\n\033[m2- \033[0;36;49mAdicionar Livro\n\033[m3- \033[0;31;49mRemover Livro\033[m 4-Atualizar Livro\n 5- Lista de Desejos\n 6- Extrato")
    escolha = int(input("-"))

    if escolha == 1:
        visualizar()
    elif escolha == 2:
        adicionar()
    elif escolha ==3:
        remover()
    elif escolha == 4:
        atualizar()
    elif escolha == 5:
        desejar()
    elif escolha == 6:
        extrato()
    else:
        print("\033[0;33;41mValor inválido\033[m")
        cetras = input("\033[1;36;49mPressione ENTER\033[m")
        if cetras != enter:
            inicio()



inicio()