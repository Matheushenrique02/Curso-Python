#lista =list()
#temp = list()
#maior = 0
#menor = 0
#while True:
#    temp.append(str(input('Nome: ')))
 #   temp.append(float(input('Peso: ')))
 #   if len(lista) ==0:
 #       maior = menor = temp [1]
 #   if temp[1] > maior:
 #       maior = temp[1]
 #   elif temp[1] < menor:
 #       menor = temp[1]
 #   lista.append(temp[:])
 #   temp.clear()
 #   resp = str(input('Quer continuar?[S/N]: ')).upper()
 #   if resp in 'N':
 #       break
#print('-=' *30)
#print(f'Você cadastrou {len(lista)} pessoas')
#print(f'O maior peso foi de {maior}Kg do(a) ', end ='')
#for p in lista:
 #   if p[1] == maior:
  #      print(f'{p[0]}')
#print()
#print(f'O menor peso foi de {menor}Kg do(a) ', end='')
#for p in lista:
#    if p[1] == menor:
#        print(f'{p[0]}')

#valor = 0
#lista= [[], []]
#for c in range(0,7):
#    valor =int(input(f'Digite o valor {c+1}: '))
#    if valor % 2 == 0:
#        lista[0].append(valor)
#    if valor % 2 != 0:
#        lista[1].append(valor)
#lista[0].sort()
#lista[1].sort()
#print(f'Os valores pares digitados foram {lista[0]}')
#print(f'Os valores impáres digitados foram {lista[1]}')


#matriz = [[0,0,0],[0,0,0],[0,0,0]]
#spar = mai = scol = 0
#for l in range(0,3):
#    for c in range(0,3):
#        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
#print('-=' *50)
#for l in range (0,3):
##    for c in range(0,3):
 #       print(f'[{matriz[l][c]: ^5}]',end='')
 #       if matriz[l][c] % 2 ==0:
 #           spar += matriz[l][c]
 #   print()
#for l in range(0,3):
  #  scol += matriz[l][2]
#for c in range(0,3):
#    if c ==0:
#        mai = matriz[1][c]
#    elif matriz[1][c] > mai:
#        mai = matriz[1][c]
#print('-=' * 50)
#print(f'A soma dos valores pares dessa matriz é {spar}')
#print(f'A soma dos valores referentes a terceira coluna é {scol}')
#print(f'O maior valor da segunda linha é {mai}')

#from time import sleep
#print('-=' *50)
#print('SORTEADOR DE JOGOS DA MEGASENA')
#print('-=' *50)
#q = int(input('Quantos jogos você deseja fazer?: '))
#from random import randint
#jogos = list()
#lista = list()
#tot = 0
#while q -1 >= tot:
#    cont = 0
#    while True:
#        num = randint(1, 60)
#        if num not in lista:
#            lista.append(num)
#            cont +=1
#        if cont >= 6:
#            break
#    jogos.append(lista[:])
#    lista.clear()
#    lista.sort()
#    tot += 1
#print('-=' *3,f'Sorteando {q} JOGOS','-='*3)
#for i , l in enumerate (jogos):
#    sleep(1)
#    print(f'JOGO {i+1}:{l}')

ficha = list()
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    ficha.append([nome,[n1, n2],media])
    resp = str(input('Deseja continuar?: ')).upper()
    if resp in 'N':
        break
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30 )
for i , a in enumerate(ficha):
    print(f'{i:<4} {a[0]:<10} {a[2]:>8.1f}')
while True:
    print('-=' * 30)
    opc=int(input('Você deseja ver as notas de qual aluno?:[999 PARA]'))
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
    if opc == 999:
        print('Finalizando....')
        break
    