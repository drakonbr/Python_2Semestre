import os
os.system('cls')
enter = "ckas"

path = "livro_lista.txt"

def visualizar():
    op = 0
    f = open(path,'r', encoding='utf-8')
    filtro = input('Coloque o gênero que você deseja filtar: ').strip().lower()
    for l in f:
        nome = (l.split(';'))[0]
        autor = (l.split(';'))[1]
        genero = (l.split(';'))[2]
        valor = (l.split(';'))[3]
        if filtro == genero:
            print(f'Nome: {nome.title()}, Autor: {autor.title()}, Gênero: {genero.title()} Preço: {valor}')
            op += 1
    f.close()

    if op == 0:
        return "Não há livros nessa categoria"
    else:
        return ""

def adicionar():
    f = open(path, 'a', encoding='utf-8')
    livro = input("\033[1;34;49mColoque o nome do livro: \033[m ").strip().lower()
    autor = input("\033[1;32;49mColoque o nome do autor: \033[m ").strip().lower()
    genero = input("Coloque o gênero do livro: ").strip().lower()
    valor = float(input("\033[1;33;49mColoque o valor do livro: \033[m "))
    f.write(f"{livro};{autor};{genero};{valor}\n")
    f.close()
    return "Livro Adicionado!"

def remover():
    op = 0
    f = open(path,'r')
    fr = f.readlines()
    f.close()

    f = open(path, 'w', encoding='utf-8')
    removed = input("\033[1;31;43mQual livro você deseja remover: \033[m ").strip().lower()
    for l in fr:
        if removed != (l.split(';'))[0]:
            f.write(f'{l}\n')
        else:
            op += 1
    f.close()
    if op >= 1:
        return "Livro Removido!"   
    else:
        return "Esse livro não está na biblioteca" 

def atualizar():
    op = 0
    f = open(path,'r')
    fr = f.readlines()
    f.close()

    f = open(path, 'w', encoding='utf-8')
    nome = input("\033[1;34;49mColoque o nome do livro que você deseja atualizar: \033[m ").strip().lower()
    for l in fr:
        if nome == (l.split(';'))[0]:
            autor = input("\033[1;32;49mColoque o nome do autor: \033[m ").strip().lower()
            genero = input("Coloque o gênero do livro: ").strip().lower()
            valor = float(input("\033[1;33;49mColoque o valor do livro: \033[m "))
            f.write(f'{nome};{autor};{genero};{valor}')
            op += 1
        else:
            f.write(f'{l}\n')
    f.close()
    if op >= 1:
        return "Livro Atualizado!"
    else:
        return "Esse livro não está na biblioteca" 
    
def desejar():
    return
def extrato():
    return

def inicio():
    print ("\033[1;32;49m//////Escolha o caminho//////\033[m")
    print ("1- \033[0;33;49mVisualizar Livros\n\033[m2- \033[0;36;49mAdicionar Livro\n\033[m3- \033[0;31;49mRemover Livro\n\033[m 4- Atualizar Livro\n 5- Lista de Desejos\n 6- Extrato")
    escolha = int(input("> "))
    if escolha == 1:
        print(visualizar())
    elif escolha == 2:
        print(adicionar())
    elif escolha ==3:
        print(remover())
    elif escolha == 4:
        print(atualizar())
    elif escolha == 5:
        print(desejar())
    elif escolha == 6:
        print(extrato())
    else:
        print("\033[0;33;41mValor inválido\033[m")
        cetras = input("\033[1;36;49mPressione ENTER\033[m")
        if cetras != enter:
            inicio()

while True:
    inicio()