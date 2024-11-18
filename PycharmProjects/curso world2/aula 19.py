#estado = dict()
#brasil = list()
#for c in range(0,3):
#    estado['UF'] = str(input('Unidade federativa: '))
#    estado['SIGLA'] = str(input('SIGLA: '))
#    brasil.append(estado.copy())
#for e in brasil:
#    for k , v in e.items():
#        print(f'O campo {k} tem valor {v}')

#aluno = dict()

#aluno['nome'] = str(input('nome: '))
#aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
#if aluno['media'] >= 7:
#    aluno['situação'] ='Aprovado'
#elif 5 <= aluno['media'] < 7:
##    aluno['situação'] = 'Recuperação'
##else:
 #   aluno['situação'] = 'Reprovado'
#print('=-' * 50)
#print(aluno['nome'])
#print(aluno['media'])
#print(f'{aluno['nome']} está em ', end ='')
#print(aluno['situação'])

#from time import sleep
#from random import randint
#from operator import itemgetter
#jogadores = dict()
#jogadores['JOGADOR1'] = randint(1,6)
#jogadores['JOGADOR2'] = randint(1,6)
#jogadores['JOGADOR3'] = randint(1,6)
#jogadores['JOGADOR4'] = randint(1,6)
#for k , v in jogadores.items():
#    print(f'{k} tirou {v} no dado.')
#    sleep(1)
#ranking = list()
#ranking = list()
#ranking = sorted(jogadores.items(), key =itemgetter(1),reverse = True)
#for i , v in enumerate(ranking):
#    print(f'{i+1} lugar: {v[0]} com {v[1]}.')
#    sleep(1)

#from datetime import datetime
#trabalhador = dict()
#trabalhador['nome'] = str(input('Nome: '))
#trabalhador['anonasc'] = int(input('Ano nascimento: '))
#trabalhador['carteira'] = int(input('Carteira de trabalho[0 se não possui]: '))
#if trabalhador['carteira'] == 0:
#    print('-=' * 40)
#    print(trabalhador['nome'])
#    print(trabalhador['anonasc'])
#    idade = datetime.now().year - trabalhador['anonasc']
##    print(f'Idade: {idade} anos')
#idade = datetime.now().year - trabalhador['anonasc']
#trabalhador['Ano de contratação'] = int(input('Ano de contratação: '))
#trabalhador['salario'] = float(input('Sálario: '))
#trabalhador['aposenta'] = idade +((trabalhador['Ano de contratação'] + 35) - datetime.now().year)
##print('-=' * 40)
#print(trabalhador['nome'])
#print(trabalhador['anonasc'])
#print(trabalhador['carteira'])
#print(trabalhador['salario'])
#print(f'Idade: {idade} anos')
#print(trabalhador['aposenta'])
#for k, v in trabalhador.items():
#    print(f'{k} tem o valor {v}')

#jogador = dict()
#partidas = list()
#jogador['nome']: str(input('Nome do atleta: '))
#tot = int(input('Quantas partidas o atleta jogou?: '))
#for c in range(0,tot):
#    gols = int(input(f'Quantos gols na partida {c+1}: '))
#    partidas.append(gols)
#jogador['gols'] = partidas[:]
#jogador['total'] = sum(partidas)
#print('-=' * 50)
#print(jogador)
#print('-=' * 50)
#for k , v in jogador.items():
#    print(f'{k} tem o valor {v}')
#print('-=' * 50)

#soma = media = 0
#mulher = list()
#acima = list()
#cont = 0
#pessoa = dict()
#lista = list()
#while True:
    #pessoa.clear()
    #pessoa['nome'] = str(input('Nome: '))
    #cont += 1
    #while True:
      #  pessoa['sexo'] = str(input('Sexo[M/F]: ')).upper()[0]
      #  if pessoa['sexo'] == 'F':
      #      mulher.append(pessoa['nome'])
     #   if pessoa['sexo'] in 'MF':
     #       break
    #    print('Apenas M OU F !!')
    #pessoa['idade'] = int(input('Idade: '))
    #soma += pessoa['idade']
   # lista.append(pessoa.copy())
   # while True:
  #      resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
  #      if resp in 'NS':
  #          break
 #       print('Apenas S OU N !!!')
 #   if resp in 'N':
 #       break
#media = soma / len(lista)
#if pessoa['idade']> media:
 #   acima.append(pessoa)

#print('-=' * 40)
#print(f'O total de pessoas cadastradas foram {cont}')
#print(f'A média de idade é {media}')
#print(f'As mulheres cadastradas são {mulher}')
#print(f'As pessoas acima da média de idade são')
#print(acima)

times = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome']: str(input('Nome do atleta: '))
    tot = int(input(f'Quantas partidas o atleta jogou?: '))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    times.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('Apenas S ou N !!')
    if resp in 'N':
        break
print('-='*40)
print(' cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end ='')
print()
print('-='*40)
for k , v in enumerate(times):
    print(f'{k:>3} ', end ='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*40)
while True:
    busca = int(input('Mostrar dados de qual atleta [99 PARA]'))
    if busca == 99:
        break
    if busca >= len(times):
        print('Dado Inválido')
    else:
        print(f'______LEVANTAMENTO DO JOGADOR {times[busca]['nome']}________')
        for i , g in enumerate(times[busca]['gols']):
            print(f'    No Jogo{i+1} fez {g} gols')
            print('-=' *40)
print('fim')








