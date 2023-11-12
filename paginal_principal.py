import os
os.system('cls')
import os
os.system('cls')
enter = "ckas"
## Colocar o inicar.

def adicionando():
    livro = input("\033[1;34;49mColoque o nome do livro:\033[m ")
    #livro.append(arquivo(txt))
    autor = input("\033[1;32;49mColoque o nome do autor:\033[m ")
    #autor.append(arquivo(txt))
    valor = float(input("\033[1;33;49mColoque o valor do livro:\033[m "))
    #valor.append(aquivo(txt))
    

def inicio():
    print ("\033[1;32;49m//////Escolha o caminho//////\033[m")
    print ("1- \033[0;33;49mLivros que você Possui\n\033[m2- \033[0;35;49mSua lista de desejos\n\033[m3- \033[0;31;49mChecar seus gastos\033[m")
    escolha = int(input("-"))

    if escolha == 1:
        #print(Lista_livros)    #manipulação de arquivos
        print("1- \033[0;36;49mAdicionar Livro\n\033[m2- \033[0;31;49mRemover Livro\033[m")
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
        print("\033[0;33;41mValor inválido\033[m")
        cetras = input("\033[1;36;49mPressione ENTER\033[m")
        if cetras != enter:
            inicio()
inicio()

def removendo():
    print("\033[1;31;43mQual produto você deseja remover:\033[m ")
    escolha_remover = int(input("-"))
    if escolha_remover == 1:
        print("\033[4;36;49mNada ainda\033[m")
