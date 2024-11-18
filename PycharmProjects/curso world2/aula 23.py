#def leiaint(msg):
#    while True:
#        try:
#            n = int(input(msg))
#        except(ValueError,TypeError):
#            print('ERRO, DIGITE UM NÚMERO INTEIRO VÁLIDO.')
#            continue
#        else:
#            return n

#def leiafloat(msg):
#    while True:
#        try:
#            n = float(input(msg))
#        except(ValueError,TypeError):
#            print('ERRO,DIGITE APENAS NÚMEROS REAIS')
#            continue
#        else:
#            return n


#num=leiaint('NÚMERO INTEIRO: ')
#num0=leiafloat('NÚMERO REAL: ')
#rint(f'Você digitou os números {num} e {num0}')

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('httpwww.pudim.com.br')
except:
    print('fora do ar')
else:
    print('TUDO CERTO AMIGO')