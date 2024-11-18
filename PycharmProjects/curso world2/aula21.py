#def voto(ano):
 #  from datetime import date
 #  atual = date.today().year
 #  idade = atual - ano
 #  if idade >= 18:
 #     return f'COM {idade} anos ,VOTO OBRIGATÓRIO'
 #  if idade< 16:
 #     return f'com {idade} anos ,AINDA NÃO VOTA'
 #  elif 16 <= idade < 18 or idade > 65:
 #     return f'Com {idade} anos , VOTO OPCIONAL'
from ctypes.wintypes import tagMSG
from http.client import responses
from lib2to3.fixes.fix_map import FixMap
from turtle import TurtleGraphicsError


#print(voto(2000))

#def fatorial(n,show=False):
#    f = 1
#    for c in range(n , 0 , -1):
#        if show:
#            print(c,end='')
#            if c > 1:
##                print(' x ',end='')
 #           else:
 #               print(' = ',end='')
 ##       f *= c
  #  return f

#print(fatorial(10,show=True))

#def ficha(jog='<desconhecido>',gols=0 ):
   # print(f'O jogador {jog} marcou {gols} gols')

#n = str(input('Nome do Atleta: '))
#g = str(input('Quantos gols ele marcou: '))
#if g.isnumeric():
#    g =int(g)
#else:
#    g = 0
#if n.strip() == '':
#    ficha(gols=g)
#else:
#    ficha(n,g)

#def Leiaint(msg):
#    ok = False
#    valor = 0
#    while True:
#        n = str(input(msg))
#        if n.isnumeric():
#            valor = int(n)
#            ok = True
#        else:
##            print('ERRO, DIGITE UM NÚMERO INTEIRO VÁLIDO')
#        if ok:
#            break
#    return valor
#n = Leiaint('Digite um número: ')
#print(f'Você digitou o número {n}')

#def notas(*num,sit = False):
#    """
#    -> Função para analisar notas
#    :param num: número de notas(uma ou várias)
#    :param sit: situação do aluno
#    :return: dict com informações do aluno.
##    """
#   r = dict()
#    r['total'] = len(num)
#    r['maior'] = max(num)
#    r['menor'] = min(num)
#    r['media'] = sum(num) / len(num)
#    if sit:
#        if r['media'] >= 7 :
#            r['situação'] = 'BOA'
#        elif r['media'] >= 5:
#            r['situação'] ='RAZOÁVEL'
#        else:
#            r['situação'] = 'RUIM'
#    return r


#resp =notas(10,6,1,sit=True)
#print(resp)
#help(notas)

c =('\033[m,' ,         # 0 - sem cor
    '\033[0;30;41m',    # 1 - vermelho
    '\033[0;30;42m')     # 2 - verde



def ajuda(com):
    help(com)

def titulo(msg,cor =0):
    tam =len(msg) + 4
    print(c[cor], end ='')
    print('=-'* tam)
    print(f'  {msg}')
    print('-='* tam)
    print(c[0], end ='')



comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYTHON',1)
    comando = str(input('COMANDO OU BIBLIOTECA > '))
    if comando.upper() == 'FIM':
        print('=-'* 20)
        titulo('VOLTE SEMPRE!',2)
        print('=-' * 20)
        break
    else:
        ajuda(comando)