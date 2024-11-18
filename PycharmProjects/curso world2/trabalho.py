cont = 0

while True:
    nome = str(input('NOME: '))
    idade = int(input('Idade: '))
    cont += 1
    resp = str(input('Quer continuar:[S/N]  ')).upper().strip()
    if resp == 'N':
        break
print(f'Ao todo foram cadastradas {cont} pessoas !')
