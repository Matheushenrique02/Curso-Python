#soma = 0
#for c in range(0,6):
 #   n=int(input(f'Digite o {c} valor: '))
  #  if n % 2 == 0:
  #      soma = soma + n
#print(f'A soma dos números pares é {soma}')

#pri=int(input('Digite o primeiro termo da progressão: '))
#razao=int(input('Digite o valor da razão: '))
#decimo = pri + (10 -1) * razao
#for c in range (pri,decimo + razao, razao):
 #   print(f'{c}' , end= ' - ')
#print('ACABOU')

#tot = 0
#n =int(input('Digite um valor para saber se é PRIMO:'))
#for c in range(1, n+1):
 #   if n % c == 0:
  #      print('\033[34m' ,end = ' ')
  #      tot += 1
  #  else:
   #     print('\033[m', end = ' ')
   # print(f'{c}', end = ' ')
#if tot <= 2:
 #   print('\n\033[mEste número é primo')
#else:
 #   print('\n\033[mEste número não é primo')
#print(f'\n\033[mO {n} foi divisível {tot} vezes ')

#import time
#frase =str(input('Digite uma frase: ')).strip().upper()
#palavras = frase.split()
#junto = ''.join(palavras)
#inverso = ''
#print('VERIFICADOR DE PALINDROMOS...')
#time.sleep(1)
#print('...')
#for letra in range(len(junto)-1 , -1 ,-1):
 #   inverso = inverso + junto[letra]
#print(junto, inverso)
#if junto == inverso:
 #   print('Esta palavra é um palindromo')
#else:
 #   print('Esta palavra não é um palindromo')

#from datetime import date
#totmaior = 0
#totmenor = 0
#atual = date.today().year
#for c in range(1,8):
 #   ano =int(input(F'Em que a pessoa {c} nasceu: '))
  #  idade = atual - ano
   # if idade >= 18:
    #    print('Esta pessoa é de maior')
     #   totmaior +=1
    #else:
    #    print('Esta pessoa é menor de idade')
     #   totmenor += 1
#print(f'Ao todo você citou 7 pessoas e contei {totmaior} maiores de idade e {totmenor} menores de idade')

#maior = 0
#menor = 0
#for c in range (1,6):
  #  peso = float(input(f'Digite o peso da pessoa {c}: '))
   # if c == 1:
    #    maior = peso
     #   menor = peso
    #else:
     #   if peso > maior:
      #      maior = peso
       # if peso < menor:
        #    menor = peso
#print(f'O maior peso lido foi {maior}KG e o menor foi {menor}KG')

somaid = 0
contm= 0
mediaidade = 0
maiorhomem = 0
nomevelho = ''
for c in range (1,5):
    print(f'----PESSOA {c}-----')
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO: ')).strip()
    somaid+= idade
    if c == 1 and sexo in 'mM':
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'mM' and idade > maiorhomem:
        maiorhomem = idade
        nomevelho = nome
print(f'O homem mais velho do grupo é o {nomevelho} com {maiorhomem} anos')
if sexo in 'Ff'  and idade <20:
    contm += 1
mediaidade = somaid / 4
print(f'{contm} mulheres tem menos de 20 anos')
print(f'A MÉDIA DE IDADE DO GRUPO É DE {mediaidade} ANOS')


#somaidade = 0
#mediaidade = 0
#maioridadehomem = 0
#nomevelho = ''
#totmulher20 = 0
#for c in range (1,5):
 #   print(f'<<<<<PESSOA {c}>>>>>')
  #  nome =str(input('NOME: ')).strip()
   # sexo = str(input('SEXO [M ou F]: ')).strip()
    #idade = int(input('IDADE: '))
    #if c == 1 and sexo in 'Mm':
     #   maioridadehomem = idade
      #  nomevelho = nome
   # if sexo in'mM' and idade > maioridadehomem:
    #    maioridadehomem = idade
     #   nomevelho = nome
    #somaidade += idade
   # mediaidade = somaidade / 4
    #if sexo in 'Ff' and idade < 20:
     #   totmulher20 = totmulher20 + 1
#print(f'O homem mais velho do grupo é o {nomevelho} com {maioridadehomem} anos')
#print(f'{totmulher20} mulheres tem abaixo de 20 anos')
#print(f'A média de idade do grupo é de {mediaidade} anos')
