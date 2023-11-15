import sys 
import os 
os.system('cls')
enter = "ckas"

path = "livro_lista.txt"
path2 = "livro_desejo.txt"

def listar_generos():
    with open(path, 'r', encoding='utf-8') as file:
        linhas = file.readlines()

    generos_unicos = set()
    for linha in linhas:
        genero = (linha.split(';'))[2]
        generos_unicos.add(genero)

    print("\033[1;35;49mGêneros presentes no arquivo:\033[m")
    for genero in generos_unicos:
        print(genero.title())
        
def visualizar():
    listar_generos()
    op = 0
    f = open(path,'r', encoding='utf-8')
    filtro = input('\033[1;34;49mColoque o gênero que você deseja filtar:\033[m ').strip().lower()
    for l in f:
        nome = (l.split(';'))[0]
        autor = (l.split(';'))[1]
        genero = (l.split(';'))[2]
        valor = (l.split(';'))[3]
        if filtro == genero:
            print(f'\033[0;32;49mNome:\033[m {nome.title()}, \033[0;32;49mAutor:\033[m {autor.title()}, \033[0;32;49mGênero:\033[m {genero.title()} \033[0;32;49mPreço:\033[m {valor}')
            op += 1
    f.close()
    voltar = input("\033[1;36;49mPressione ENTER pra voltar ao Menu\n\033[m")
    if op == 0:
        return "\033[1;31;49mNão há livros nessa categoria\033[m"
    else:
        return ""

def adicionar():
    f = open(path, 'a', encoding='utf-8')
    livro = input("\033[1;34;49mColoque o nome do livro: \033[m ").strip().lower()
    autor = input("\033[1;32;49mColoque o nome do autor: \033[m ").strip().lower()
    genero = input("\033[1;35;49mColoque o gênero do livro: \033[m ").strip().lower()
    valor = float(input("\033[1;33;49mColoque o valor do livro: \033[m "))
    f.write(f"{livro};{autor};{genero};{valor}\n")
    f.close()
    return "\033[1;32;49mLivro Adicionado!\033[m"

def remover():
    op = 0
    f = open(path, 'r', encoding='utf-8')
    fr = f.readlines()
    f.close()

    f = open(path, 'w', encoding='utf-8')
    removed = input("\033[1;36;49mQual livro você deseja remover: \033[m ").strip().lower()
    for l in fr:
        if removed != (l.split(';'))[0]:
            f.write(f'{l.rstrip()}\n')
        else:
            op += 1
    f.close()
    if op >= 1:
        return "\033[1;33;49mLivro Removido!\033[m"   
    else:
        return "\033[1;31;43mEsse livro não está na biblioteca\033[m"


def atualizar():
    op = 0
    f = open(path, 'r', encoding='utf-8')
    fr = f.readlines()
    f.close()

    f = open(path, 'w', encoding='utf-8')
    nome = input("\033[1;34;49mColoque o nome do livro que você deseja atualizar: \033[m ").strip().lower()
    for l in fr:
        if nome == (l.split(';'))[0]:
            autor = input("\033[1;32;49mColoque o nome do autor: \033[m ").strip().lower()
            genero = input("\033[1;35;49mColoque o gênero do livro:\033[m ").strip().lower()
            valor = float(input("\033[1;33;49mColoque o valor do livro: \033[m "))
            f.write(f'{nome};{autor};{genero};{valor}\n')
            op += 1
        else:
            f.write(f'{l.rstrip()}\n')
    f.close()
    if op >= 1:
        return "\033[1;32;49mLivro Atualizado!\033[m"
    else:
        return "\033[1;31;43mEsse livro não está na biblioteca\033[m"

    
def desejar():
    escolha = int(input('\033[1;34;49mEscolha entre as opções abaixo:\n 1- Visualizar Lista de Desejos\n 2- Adicionar a Lista de Desejos\n> \033[m'))
    if escolha == 1: 
        f = open(path2, 'r', encoding='utf-8')
        for l in f:
            nome = (l.split(';'))[0]
            autor = (l.split(';'))[1]
            genero = (l.split(';'))[2]
            valor = (l.split(';'))[3]
            print(f'\033[0;32;49mNome:\033[m {nome.title()}, \033[0;32;49mAutor:\033[m {autor.title()}, \033[0;32;49mGênero:\033[m {genero.title()} \033[0;32;49mPreço:\033[m {valor}')
        retornar = (input("\033[1;36;49mPressione ENTER para retornar ao Menu\033[m\n"))
        return "" 
    elif escolha == 2:
        f = open(path2, 'a', encoding='utf-8')
        livro = input("\033[1;34;49mColoque o nome do livro: \033[m ").strip().lower()
        autor = input("\033[1;32;49mColoque o nome do autor: \033[m ").strip().lower()
        genero = input("\033[1;35;49mColoque o gênero do livro: \033[m ").strip().lower()
        valor = float(input("\033[1;33;49mColoque o valor do livro: \033[m "))
        f.write(f"{livro};{autor};{genero};{valor}\n")
        f.close()
        return "\033[1;32;49mLivro Desejado!\033[m"
        retornar = (input("\033[1;36;49mPressione ENTER para retornar ao Menu\033[m\n"))



def extrato():
    total_valor = 0
    extrato_texto = []
    
    with open(path, 'r', encoding='utf-8') as file:
        for linha in file:
            nome = (linha.split(';'))[0]
            valor = float((linha.split(';'))[3])
            
            total_valor += valor
            extrato_texto.append(f'{nome.title()} - Valor: {valor}')
    file.close()

    print("\033[1;33;49mExtrato da conta:\033[m")
    for t in extrato_texto:
        print(t)
    
    print(f'Total: {total_valor}\n')
    retornar = (input("\033[1;36;49mPressione ENTER para retornar ao Menu\033[m\n"))
    return ""

def inicio():
    print ("\033[1;32;49m//////Escolha o caminho//////\033[m")
    print ("1- \033[0;33;49mVisualizar Livros\n\033[m2- \033[0;36;49mAdicionar Livro\n\033[m3- \033[0;31;49mRemover Livro\n\033[m4- \033[0;32;49mAtualizar Livro\n\033[m5- \033[0;31;49mLista de Desejos\n\033[m6- \033[0;33;49mExtrato\n\033[m7- \033[0;31;49mEncerrar\033[m")
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
    elif escolha == 7:
        print("\033[1;31;49mPrograma encerrado\033[m")
        sys.exit()
    else:
        print("\033[0;33;41mValor inválido\033[m")
        cetras = input("\033[1;36;49mPressione ENTER\033[m")
        if cetras != enter:
            inicio()

while True:
    inicio()
