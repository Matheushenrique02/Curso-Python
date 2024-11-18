from ex115.lib.interface import*
from ex115.lib.arquivo import*
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criarArquivo(arq)

while True:
    resposta =menu(['Ver pessoas cadastradas','Cadastrar Novas pessoas','Sair Do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaint('idade: ')
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        print('FINALIZANDO O SISTEMA....')
        break
    else:
        print('ERRO,POR FAVOR SOMENTE OPÇÕES VÁLIDAS.')
    sleep(2)