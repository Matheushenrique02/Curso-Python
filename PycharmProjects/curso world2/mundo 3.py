#n = ('zero', 'um', 'dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
#while True:
 #   l = int(input('Digite um valor de 0 a 20 para ver escrito por extenso: '))
  #  if 0 <= l <= 20:
   #     break
   # print('Tente novamente.', end ='')
#print(f'Você digitou o número {n[l]}')
from unicodedata import numeric

#times = ('Corinthians','Palmeiras','Santos','Grêmio','Cruzeiro',
       #  'Flamengo','Vasco','Chapecoense','AtleticoMG','Botafogo'
      #   ,'AthleticoPR','Bahia','São Paulo','Fluminense','Sport','Vitória',
     #    'Coritiba','Avai','Ponte Preta','AtléticoGO')
#print('-=' *30)
#print(f'Lista de times {times}')
#print('-=' * 30)
#print(f'Os cinco primeiros colocados são {times[0:6]}')
##print(f'Os quatro últimos colocados são {times[-4:]}')
#print(f'Em Ordem alfabetica a lista fica {sorted(times)}')
#print(f'A chapecoense está na posição {times.index('Chapecoense')+1}')


#from random import randint
#numeros = (randint(0,10),randint(0,10), randint(0,10),
#randint(0,10), randint(0,10))
#print(f'Eu sorteei os valores:')
#for n in numeros :
 #   print(f'{n} ,', end ='')
#print(f'O maior valor sorteado foi {max(numeros)} e o menor valor foi {min(numeros)}')



#num = (int(input('Digite um número: ')) , int(input('Digite mais um número: ')) ,
#           int(input('Digite o penúltimo número: ')) , int(input('Digite o último número: ')))

#print(f'O número 9 apareceu {num.count(9)} vezes')
#if 3 in num:
 #   print(f'O valor 3 apareceu na posição {num.index(3) + 1}')
#else:
 #   print('O valor 3 não foi digitado')
#print(f'Dos números que você digitou ,são pares: ', end ='')
#for n in num:
 #   if n % 2 == 0:
  #      print(n)

#preços = ('Lápis' , 1.75,
 #         'Borracha', 2,
  #        'Caderno', 15.90,
   #       'Estojo', 25,
    #      'Transferidor', 4.20,
     ##    'Mochila', 120.32,
       #   'Canetas', 22.30,
        #  'Livro', 34.90)
#print('-' *30)
#print('LISTAGEM DE PREÇOS')
#for pos in range(0, len(preços)):
 #   if pos %2 == 0:
  #      print(f'{preços[pos]:.<30}',end ='')
   # else:
    #    print(f'R${preços[pos]:>7.2f}')

#vogais = 'a','e','i','o','u'
#palavras = ('APRENDER', 'PROGRAMAR','LINGUAGEM','PYTHON'
 #           ,'CURSO','GRATIS','ESTUDAR','PRATICAR','TRABALHAR',
  #          'MERCADO', 'PROGRAMADOR','FUTURO')
#for p in palavras:
 #   print(f'\nNa palavra {p} temos: ',end ='')
  #  for letra in p:
   #     if letra.lower() in 'aeiou':
    #        print(f'{letra}', end='')

#maior = menor = 0
#valores = list()
#for v in range(0,5):
 #   valores.append(int(input(f'Digite o {v} valor: ')))
 #   if v == 0:
  #      maior = menor = valores[v]
  #  else:
   #     if valores[v] > maior:
    #        maior = valores[v]
     #   if valores[v] < menor:
      #      menor = valores[v]
#print(f'Você digitou os valores {valores}')
#print(f'O maior valor digitado foi {maior} nas posições: ', end ='')
#for i , v in enumerate(valores):
 #   if v == maior:
  #      print(f'{i}...', end ='')
#print()
#print(f'O menor valor digitado foi {menor} nas posições: ', end='')
#for i ,v in enumerate(valores):
 #   if v == menor:
  #      print(f'{i}...', end ='')
#print()


#valores = list()
#while True:
 #   n=(int(input('Digite um valor: ')))
  #  if n not in valores:
   #     valores.append(n)
    #    print('Valor adicionado com sucesso!')
    #else:
     #   print('Valor duplicado... Não irei adicionar')
    #resp = str(input('Quer continuar?:[S/N] ')).upper().strip()[0]
    #if resp in 'Nn':
     #   break
#valores.sort()
#print(f'Os valores digitados foram {valores}')
#print('Obrigado por utilizar')

#valores = list()
#for c in range(0,5):
#    v = int(input('Digite um valor: '))
#    if c == 0 or v > valores[-1]:
#        valores.append(v)
#    else:
#        pos = 0
#        while pos < len(valores):
#            if v <= valores[pos]:
#                valores.insert(pos, v)
#                break
#                pos += 1
#print('-=' *30)
#print(f'Os valores digitados em ordem sãp {valores}')

#cont = 0
#lista = list()
#while True:
#    v= int(input('Digite um valor: '))
#    lista.append(v)
#    cont += 1
#    resp = str(input('Quer continuar?[S/N]: ')).upper()
#    if resp in 'Nn':
#        break
#lista.sort(reverse=True)
#print(f'Os valores digitados em ordem decrescentes são {lista}')
#print(f'Foram digitados {cont} valores')

#impar = list()
#pares = list()
#lista = list()
#while True:
#    v = int(input('Digite um valor: '))
#    lista.append(v)
#    if v % 2 == 0:
#        pares.append(v)
#    if v % 2 != 0:
#        impar.append(v)
#    resp = str(input('Quer continuar?[S/N]: ')).upper()
#    if resp in 'N':
 #       break
##print('-=' *30)
##print(f'Os valores digitados foram {lista}')
#print(f'Os valores pares são {pares}, E os valores impáres são {impar}')

#exp = str(input('Digite a expressão: '))
#pilha = list()
#for sim in exp:
#    if sim == '(':
#        pilha.append('(')
#    elif sim == ')':
#        if len(pilha) > 0:
#            pilha.pop()
#        else:
#            pilha.append(')')
#            break
#if len(pilha) == 0:
#    print('Sua expressão está valída')
#else:
#    print('Expressão Inválida')

galera = [['joao', 19],['Ana', 25],['Joaquim',44],['Maria', 13]]
for p in galera:
    print(f'O {p[0]} tem {p[1]} anos')


