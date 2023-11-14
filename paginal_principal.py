import sys 
import os
os.system('cls')
enter = "ckas"

path = "livro_lista.txt"

def listar_generos():
    with open(path, 'r', encoding='utf-8') as file:
        linhas = file.readlines()

    generos_unicos = set()
    for linha in linhas:
        genero = (linha.split(';'))[2]
        generos_unicos.add(genero)

    print("Gêneros presentes no arquivo:")
    for genero in generos_unicos:
        print(genero.title())
        
def visualizar():
    listar_generos()
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
    voltar = input("Prescione ENTER pra voltar ao Menu\n")
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
    f = open(path, 'r', encoding='utf-8')
    fr = f.readlines()
    f.close()

    f = open(path, 'w', encoding='utf-8')
    removed = input("\033[1;31;43mQual livro você deseja remover: \033[m ").strip().lower()
    for l in fr:
        if removed != (l.split(';'))[0]:
            f.write(f'{l.rstrip()}\n')
        else:
            op += 1
    f.close()
    if op >= 1:
        return "Livro Removido!"   
    else:
        return "Esse livro não está na biblioteca" 


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
            genero = input("Coloque o gênero do livro: ").strip().lower()
            valor = float(input("\033[1;33;49mColoque o valor do livro: \033[m "))
            f.write(f'{nome};{autor};{genero};{valor}\n')
            op += 1
        else:
            f.write(f'{l.rstrip()}\n')
    f.close()
    if op >= 1:
        return "Livro Atualizado!"
    else:
        return "Esse livro não está na biblioteca"

    
def desejar():
    return
def extrato():
    total_valor = 0
    extrato_texto = []
    
    with open(path, 'r', encoding='utf-8') as file:
        for linha in file:
            nome = (linha.split(';'))[0]
            valor = float((linha.split(';'))[3])
            
            total_valor += valor
            extrato_texto.append(f'{nome.title()} - Valor: {valor}')

    print("Extrato da conta:")
    for t in extrato_texto:
        print(t)
    
    print(f'Total: {total_valor}\n')
    retornar = (input("Prescione ENTER para retornar ao Menu\n"))
    return ""

def inicio():
    print ("\033[1;32;49m//////Escolha o caminho//////\033[m")
    print ("1- \033[0;33;49mVisualizar Livros\n\033[m2- \033[0;36;49mAdicionar Livro\n\033[m3- \033[0;31;49mRemover Livro\n\033[m 4- Atualizar Livro\n 5- Lista de Desejos\n 6- Extrato\n 7-Encerrar")
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
        print("Programa encerrado")
        sys.exit()
    else:
        print("\033[0;33;41mValor inválido\033[m")
        cetras = input("\033[1;36;49mPressione ENTER\033[m")
        if cetras != enter:
            inicio()

while True:
    inicio()

