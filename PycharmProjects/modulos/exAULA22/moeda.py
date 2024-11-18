def aumentar(preço=0,taxa=0,formato=False):
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)

def diminuir(preço =0,taxa = 0,formato=False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço=0,formato=False):
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço=0,formato=False):
    res = preço /2
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda ='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')

def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada.strip() =='':
            print(f'ERRO: {entrada}  PREÇO INVÁLIDO')
        else:
            valido = True
            return float(entrada)


def resumo(preço = 0,taxaau= 10,taxadim=5):
     print('---------RESUMO DOS VALORES--------'.center(20))
     print(f'PREÇO ANALISADO...:\t{moeda(preço)}')
     print(f'Dobro do preço:    \t{dobro(preço,True)}')
     print(f'Metade do preço:   \t{metade(preço,True)}')
     print(f'Aumento de {taxaau}%:    \t{aumentar(preço,taxaau, True)} ')
     print(f'Desconto de {taxadim}%:    \t{diminuir(preço,taxadim,True)}')