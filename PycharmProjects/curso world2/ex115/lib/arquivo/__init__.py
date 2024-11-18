from ex115.lib.interface import *

def arquivoexiste(nome):
    try:
        a = open(nome , 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com Sucesso!')

def lerArquivo(nome):
    try:
        a = open(nome,'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'Nome:{dado[0]}->Idade:{dado[1]}')
    finally:
        a.close()

def cadastrar(arq,nome='zumbi palmares',idade=52):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na execução do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao adicionar ')
        else:
            print(f'Novo registro de {nome} adicionado!')
            a.close()


