import sys 
import os 
os.system('cls')
enter = "ckas"

path = "livro_lista.txt"
path2 = "livro_desejo.txt"

def listar_generos():
    try:
        with open(path, 'r', encoding='utf-8') as file:
            linhas = file.readlines()
    except FileNotFoundError:
        open(path,'a',encoding='utf-8')
        return "\033[1;31;49mArquivo não encontrado!\033[m"
    except NameError as ne:
        return f"\033[1;31;49mErro de nome: {ne}\033[m"
    except Exception as e:
        return f"\033[1;31;49mErro: {e}\033[m"

    generos_unicos = set()
    for linha in linhas:
        genero = (linha.split(';'))[2]
        generos_unicos.add(genero)
    os.system('cls')
    print("\033[1;35;49mGêneros presentes no arquivo:\n\033[m")
    for genero in generos_unicos:
        print(genero.title())
    print("")
        
def visualizar():
    try:   
        listar_generos()
        operacao = 0
        f = open(path,'r', encoding='utf-8')
        filtro = input('\033[1;34;49mColoque o gênero que você deseja filtar:\033[m ').strip().lower()
        for l in f:
            nome = (l.split(';'))[0]
            autor = (l.split(';'))[1]
            genero = (l.split(';'))[2]
            valor = (l.split(';'))[3]
            if filtro == genero:
                print(f'\033[0;32;49mNome:\033[m {nome.title()}, \033[0;32;49mAutor:\033[m {autor.title()}, \033[0;32;49mGênero:\033[m {genero.title()} \033[0;32;49mPreço:\033[m {valor}')
                operacao += 1
        f.close()
        if operacao == 0:
            print("\033[1;31;49mNão há livros nessa categoria\n\033[m")
            return input("\033[1;36;49mPressione ENTER pra voltar ao Menu\n\033[m")
        else:
            return input("\033[1;36;49mPressione ENTER pra voltar ao Menu\n\033[m")
    except FileNotFoundError:
        return "\033[1;31;49mArquivo não encontrado!\033[m"
    except ValueError:
        return "\033[1;31;49mErro de valor!\033[m"
    except NameError as ne:
        return f"\033[1;31;49mErro de nome: {ne}\033[m"
    except TypeError as te:
        return f"\033;1;31;49mErro de tipo: {te}\033[m"
    except Exception as e:
        return f"\033[1;31;49mErro: {e}\033[m"

def adicionar():
    os.system('cls')
    try:
        f = open(path, 'a', encoding='utf-8')
        livro = input("\033[1;34;49mColoque o nome do livro: \033[m ").strip().lower()
        autor = input("\033[1;32;49mColoque o nome do autor: \033[m ").strip().lower()
        genero = input("\033[1;35;49mColoque o gênero do livro: \033[m ").strip().lower()
        while(True):
            try:
                valor = float(input("\033[1;33;49mColoque o valor do livro: \033[m "))
                if type(valor) == float:
                    break
            except ValueError:
                print("\033[1;31;49mErro de valor! Digite novamente\033[m")
        f.write(f"{livro};{autor};{genero};{valor}\n")
        f.close()
        "\033[1;32;49mLivro Adicionado!\033[m"
        return input("\033[1;36;49mPressione ENTER pra voltar ao Menu\n\033[m")


    except FileNotFoundError:
        return "\033[1;31;49mArquivo não encontrado!\033[m"
    except ValueError:
        return "\033[1;31;49mErro de valor!\033[m"
    except NameError as ne:
        return f"\033[1;31;49mErro de nome: {ne}\033[m"
    except TypeError as te:
        return f"\033;1;31;49mErro de tipo: {te}\033[m"
    except Exception as e:
        return f"\033[1;31;49mErro: {e}\033[m"

def remover():
    os.system('cls')
    try:
        operacao = 0
        with open(path, 'r', encoding='utf-8') as f:
            fr = f.readlines()

        with open(path, 'w', encoding='utf-8') as f:
            removed = input("\033[1;36;49mQual livro você deseja remover: \033[m ").strip().lower()
            for l in fr:
                if removed != (l.split(';'))[0]:
                    f.write(f'{l.rstrip()}\n')
                else:
                    operacao += 1

        if operacao >= 1:
            print("\033[1;33;49mLivro Removido!\033[m")
            return input("\033[1;36;49mPressione ENTER pra voltar ao Menu\n\033[m")   
        else:
            return "\033[1;31;43mEsse livro não está na biblioteca\033[m"

    except FileNotFoundError:
        return "\033[1;31;49mArquivo não encontrado!\033[m"
    except NameError as ne:
        return f"\033[1;31;49mErro de nome: {ne}\033[m"
    except TypeError as te:
        return f"\033;1;31;49mErro de tipo: {te}\033[m"
    except Exception as e:
        return f"\033[1;31;49mErro: {e}\033[m"


def atualizar():
    os.system('cls')
    try:
        operacao = 0
        with open(path, 'r', encoding='utf-8') as f:
            fr = f.readlines()

        with open(path, 'w', encoding='utf-8') as f:
            nome = input("\033[1;34;49mColoque o nome do livro que você deseja atualizar: \033[m ").strip().lower()
            for l in fr:
                if nome == (l.split(';'))[0]:
                    autor = input("\033[1;32;49mColoque o nome do autor: \033[m ").strip().lower()
                    genero = input("\033[1;35;49mColoque o gênero do livro:\033[m ").strip().lower()
                    while(True):
                        try:
                            valor = float(input("\033[1;33;49mColoque o valor do livro: \033[m "))
                            if type(valor) == float:
                                break
                        except ValueError:
                            print("\033[1;31;49mErro de valor! Digite novamente\033[m")
                    f.write(f'{nome};{autor};{genero};{valor}\n')
                    operacao += 1
                else:
                    f.write(f'{l.rstrip()}\n')

        if operacao >= 1:
            return "\033[1;32;49mLivro Atualizado!\033[m"
        else:
            return "\033[1;31;43mEsse livro não está na biblioteca\033[m"

    except FileNotFoundError:
        return "\033[1;31;49mArquivo não encontrado!\033[m"
    except ValueError:
        return "\033[1;31;49mErro de valor!\033[m"
    except NameError as ne:
        return f"\033[1;31;49mErro de nome: {ne}\033[m"
    except TypeError as te:
        return f"\033;1;31;49mErro de tipo: {te}\033[m"
    except Exception as e:
        return f"\033[1;31;49mErro: {e}\033[m"

    
def desejar():
    os.system('cls')
    try:
        escolha = int(input('\033[1;34;49mEscolha entre as opções abaixo:\n 1- Visualizar Lista de Desejos\n 2- Adicionar a Lista de Desejos\n 3- Remover livro da Lista de Desejos\n> \033[m'))
        if escolha == 1: 
            with open(path2, 'r', encoding='utf-8') as f:
                for l in f:
                    nome = (l.split(';'))[0]
                    autor = (l.split(';'))[1]
                    genero = (l.split(';'))[2]
                    valor = (l.split(';'))[3]
                    print(f'\033[0;32;49mNome:\033[m {nome.title()}, \033[0;32;49mAutor:\033[m {autor.title()}, \033[0;32;49mGênero:\033[m {genero.title()} \033[0;32;49mPreço:\033[m {valor}')
            return (input("\033[1;36;49mPressione ENTER para retornar ao Menu\033[m\n"))
            
        elif escolha == 2:
            with open(path2, 'a', encoding='utf-8') as f:
                livro = input("\033[1;34;49mColoque o nome do livro: \033[m ").strip().lower()
                autor = input("\033[1;32;49mColoque o nome do autor: \033[m ").strip().lower()
                genero = input("\033[1;35;49mColoque o gênero do livro: \033[m ").strip().lower()
                while(True):
                    try:
                        valor = float(input("\033[1;33;49mColoque o valor do livro: \033[m "))
                        if type(valor) == float:
                            break
                    except ValueError:
                        print("\033[1;31;49mErro de valor! Digite novamente\033[m")
                f.write(f"{livro};{autor};{genero};{valor}\n")
            print("\033[1;32;49mLivro Desejado!\033[m")
            return (input("\033[1;36;49mPressione ENTER para retornar ao Menu\033[m\n"))
        elif escolha == 3:
            operacao = 0
            with open(path2, 'r', encoding='utf-8') as f:
                fr = f.readlines()

            with open(path2, 'w', encoding='utf-8') as f:
                livro_remover = input("\033[1;36;49mQual livro você deseja remover: \033[m ").strip().lower()
                for l in fr:
                    if livro_remover != (l.split(';'))[0]:
                        f.write(f'{l.rstrip()}\n')
                    else:
                        operacao += 1

            if operacao >= 1:
                return "\033[1;33;49mLivro Removido da Lista de Desejos!\033[m"   
            else:
                print( "\033[1;31;43mEsse livro não está na Lista de Desejos\033[m")
                return (input("\033[1;36;49mPressione ENTER para retornar ao Menu\033[m\n"))

    except FileNotFoundError:
        return "\033[1;31;49mArquivo não encontrado!\033[m"
    except ValueError:
        return "\033[1;31;49mErro de valor!\033[m"
    except NameError as ne:
        return f"\033[1;31;49mErro de nome: {ne}\033[m"
    except TypeError as te:
        return f"\033;1;31;49mErro de tipo: {te}\033[m"
    except Exception as e:
        return f"\033[1;31;49mErro: {e}\033[m"


def extrato():
    os.system('cls')
    try:
        total_valor = 0
        extrato_texto = []
        
        with open(path, 'r', encoding='utf-8') as file:
            for linha in file:
                nome = (linha.split(';'))[0]
                valor = float((linha.split(';'))[3])

                total_valor += valor
                extrato_texto.append(f'{nome.title()} - Valor: {valor}')
        file.close()

        print("\033[1;33;49m\nExtrato da conta:\n\033[m")
        for t in extrato_texto:
            print(t)
        
        print(f'Total: R$ {total_valor}\n')
        return input("\033[1;36;49mPressione ENTER pra voltar ao Menu\n\033[m")

    except FileNotFoundError:
        return "\033[1;31;49mArquivo não encontrado!\033[m"
    except ValueError:
        return "\033[1;31;49mErro de valor!\033[m"
    except NameError as ne:
        return f"\033[1;31;49mErro de nome: {ne}\033[m"
    except TypeError as te:
        return f"\033;1;31;49mErro de tipo: {te}\033[m"
    except Exception as e:
        return f"\033[1;31;49mErro: {e}\033[m"

def inicio():
    os.system('cls')
    try:
        print ("\033[1;32;49m<=-====-=> Escolha o caminho <=-====-=>\033[m\n")
        print ("1- \033[0;33;49mVisualizar Livros\n\033[m2- \033[0;36;49mAdicionar Livro\n\033[m3- \033[0;31;49mRemover Livro\n\033[m4- \033[0;32;49mAtualizar Livro\n\033[m5- \033[0;31;49mLista de Desejos\n\033[m6- \033[0;33;49mExtrato\n\033[m7- \033[0;31;49mEncerrar\033[m")
        escolha = int(input("\n> "))
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

    except FileNotFoundError:
        print("\033[1;31;49mArquivo não encontrado!\033[m")
    except ValueError:
        print("\033[1;31;49mErro de valor!\033[m")
    except NameError as ne:
        return f"\033[1;31;49mErro de nome: {ne}\033[m"
    except TypeError as te:
        return f"\033;1;31;49mErro de tipo: {te}\033[m"
    except Exception as e:
        print(f"\033[1;31;49mErro inesperado: {e}\033[m")

while True:
    try:
        inicio()
    except Exception as e:
        print(f"\033[1;31;49mErro inesperado: {e}\033[m")
