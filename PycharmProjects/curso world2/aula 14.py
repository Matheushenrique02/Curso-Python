#sexo = str(input('POR FAVOR DIGITE SEU SEXO:[M/F]    ')).strip().upper()[0]
#while sexo not in 'MmFf':
 #   sexo = str(input('REVISE OS DADOS INFORMADOS E DIGITE SEU SEXO:[M/F]  '))
#print(f'Obrigado por informar que seu sexo é {sexo}')
from xml.sax import parse

#from random import randint

#cont = 0
#print('------GAME DA ADIVINHAÇÃO-----')
#print('DUVIDO VOCÊ ME VENCER')
#pc = randint(0,10)
#jogador = int(input('Em qual número você acha que estou pensando??: '))
#while jogador != pc:
 #   jogador = int(input('Errou!, tente novamente: '))
  ###    print(f'Você me venceu , eu pensei realmente no número {pc}')
#print(f'Foram necessárias {cont} tentivas para você ganhar')

#print('---BEM VINDO-----')
#print('*****CALCÚLOS EXATOS*****')
#valor1 = int(input('Digite o primeiro valor: '))
#valor2 = int(input('Digite o segundo valor: '))
#print('OPÇÕES: ')
#print('[1] SOMAR')
#print('[2] MULTIPLICAR')
#print('[3] MAIOR')
#print('[4] INSERIR NOVOS NÚMEROS')
#print('[5] SAIR DO PROGRAMA')
#escolha = 0
#while escolha != 5:
 #   escolha = int(input('O que você deseja fazer?: '))
  #  if escolha == 1:
   #     soma=valor1 + valor2
    #    print(f'A soma dos valores é {soma}')
    #if escolha == 2:
    #    produto=valor1 * valor2
    #    print(f'A multiplicação entre os valores da {produto}')
    #if escolha == 3:
     #   if valor1 > valor2:
      #      print(f'O {valor1} é o maior valor digitado')
       # else:
        #     print(f'O {valor2} é o maior valor digitado')
    #if escolha == 4:
     #   valor1 = int(input('Digite o primeiro valor: '))
      #  valor2 = int(input('Digite o segundo valor: '))
    #if escolha not in (1,2,3,4,5):
     #   print('OPÇÃO INVÁLIDA , TENTE NOVAMENTE')
#print('----FIM-----')


#from math import factorial

#print('----CALCULO DE FATORIAL')
#n = int(input('Digite um valor: '))
#fat = (factorial(n))
#print(f'O fatorial do {n} é {fat}')

#primeiro = int(input('Digite o primeiro termo da P.A:'))
#razao = int(input('Digite a razão da P.A: '))
#termo = primeiro
#cont = 1
#while cont <=10:
 #   print(f'{termo} -',end = '')
  #  termo += razao
   # cont +=1
#total = 0
#mais = 10
#primeiro = int(input('Digite o primeiro termo da P.A:'))
#razao = int(input('Digite a razão da P.A: '))
#termo = primeiro
#cont = 1
#while mais != 0:
 #   total = total + mais
  #  while cont <=total:
   #     print(f'{termo} -',end = '')
    #    termo += razao
     #   cont +=1
    #print('PAUSA')
    #mais = int(input('Quantos termos você quer mostrar a mais?: '))
#print('FIM')

#print('-'*30)
#print('SEQUENCIA DE FIBONACCI')
#print('-'*30)
#n = int(input('Quantos termos você deseja mostrar: '))
#t1 = 0
#t2 = 1
#print('*' *30)
#print(f'{t1} - {t2}', end ='')
#cont = 3
#while cont <= n:
 #   t3 = t1 + t2
  #  print(f'- {t3}',end ='')
   ##t2 = t3
    #cont += 1
#print('- FINALIZANDO...')

#s = 0
#cont = 0
#n = 0
#while n != 999:
  #  n = int(input('DIGITE UM VALOR[999 PARA FINALIZAR]: '))
 #   if n != 999:
   #     cont += 1
    #    s += n
#print('FINALIZANDO.....')
#print(f'Você informou {cont} valores e a soma entre eles foi {s}')

#menor = 0
#maior = 0
#soma = 0
#media = 0
#c = 0
#resposta = 'S'
#while resposta in 'Ss':
 #   n =int(input('Digite um valor: '))
  #  c += 1
   # soma += n
   # if c == 1:
    #    maior = menor = n
   # if n > maior:
   #     maior = n
   # if n < menor:
   #     menor = n
   #resposta =str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
#media = soma / c
#print(f'Você digitou {c} números e a media entre eles foi {media :.2f}', end = '')
#print(f'O maior número digitado foi {maior} e o menor número digitado foi {menor}')

#c = 0
#soma = 0
#n = 0
#while True:
 #   n =int(input('Digite um valor [999 PARA FINALIZAR]: '))
  #  if n == 999:
   #     break
   # c += 1
   # soma += n
#print(f'Você digitou {c} números e a soma entre eles foi {soma} ')

#nome = str(input('Qual seu nome? :'))
#c = 0
#print('----->TABUADA V3<-------')
#while True:
 #   r = int(input('Quer ver a tabuada de qual número [999 PARA FINALIZAR]: '))
  #  if r == 999:
   #     break
   # c += 1
    #for c in range (1,11):
     #   print(f'{r} x {c} = {r * c}')
#print(f'Obrigado por utilizar meu programa {nome}')



#from random import randint
#v = 0
#print('------>PAR OU IMPAR?<------')
#while True:
 #   jogador = int(input('Digite um valor: '))
  #  pc = randint(0,10)
   # tot = jogador + pc
    #tipo = ' '
    #while tipo not in 'PI':
     #   tipo =str(input('Você escolhe PAR OU ÍMPAR? :')).strip().upper()[0]
   # print(f'Você jogou {jogador} e o computador jogou {pc} e isso deu um total de {tot}')
    #print(f'DEU PAR' if tot /2 ==0 else 'DEU ÍMPAR')
   # if tipo == 'P':
    ##       print('Você venceu!!!')
      #      v += 1
       # else:
       #     print('Você perdeu!!!')
     #       break
    #elif tipo == 'I':
       # if tot /2 == 1:
      #      print('Você venceu!!!!')
        #    v += 1
        #else:
         #   print('Você perdeu!!!')
          #  break
#print(f'Finalizando o GAME , você conseguiu me vencer {v} vezes')


#maior = cadhomem = mulher20 = 0
#print('----->CADASTRO<-----')
#while True:
  #   if id >= 18:
   #     maior += 1
   # sexo =' '
   # while sexo not in 'MF':
     #   sexo = str(input('SEXO[M/F]:')).strip().upper()[0]
    #    if sexo in 'M':
      #      cadhomem += 1
      #  if sexo == 'F' and id < 20:
      #      mulher20 += 1
    #resp = ' '
    #while resp not in 'SN':
     #   resp = str(input('Quer continuar?[S/N]: ')).upper().strip()[0]
   # if resp in 'N':
    #    break
#print(f'{maior} Pessoas que você cadastrou são maiores de idade')
#print(f'{cadhomem} Homens foram cadastrados')
#print(f'{mulher20} Mulheres tem menos de 20 anos')

#barato = ' '
#cont = 0
#menor = 0
#maior = 0
#tot = 0
#print('--------MARKETVISION--------')
#while True:
 #   nome = str(input('Nome do produto: '))
  #  valor = float(input('Preço do produto: '))
   # cont += 1
   # if valor > 1000:
    #    maior += 1
   # if cont == 1:
     #   menor = valor
    #    barato = nome
    #else:
     #  if valor < menor:
      #      menor = valor
       #     barato = nome

    #tot += valor
    #esc= ' '
    #while esc not in 'SN':
     #   esc=str(input('Você quer continuar:[S/N]')).upper().strip()[0]
    #if esc in 'N':
     #   break
#print(f'O total da compra foi {tot}')
#print(f'{maior} Produtos custaram mais de R$ 1000')
#print(f'O produto mais barato foi o {barato} e custou R$ {menor}')

print('--BANCO MH--')
valor = int(input('Qual valor você deseja sacar: R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced  = 0
        if total == 0:
            break






