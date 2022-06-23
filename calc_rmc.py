import math
from matplotlib.pyplot import *
from numpy import *

def menu(opcoes, legendas):
    opcao = ''
    while opcao not in opcoes:
        print('Escolha uma opção: ')
        for legenda in legendas:
            print(legenda)
        try:
            opcao = int(input())
        except:
            print('Valor inválido')
    return opcao

def calc_raiz(a,b,c):
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = round((-b + math.sqrt(delta))/(2*a),3)
        x2 = round((-b - math.sqrt(delta))/(2*a),3)
        print(f'x\' = {x1}')
        print(f'x\'\' = {x2}')
        return [x1,x2]
    elif delta == 0:
        x = round(-b/(2*a),3)
        print(f'x = {x}')
        return [x1]
    else:
        x1 = complex(round(-b/(2*a), 3),+ round(math.sqrt(-delta)/(2*a) ,3))
        x2 = complex(round(-b/(2*a), 3),- round(math.sqrt(-delta)/(2*a) ,3))

        print(f'x\' = {x1}')
        print(f'x\'\' = {x2}')
        return []

def calc_func_2_grau(a, b, c):
    x = ''
    while type(x) == str:
        try:
            x = float(input('Informe o valor de X: '))
        except:
            print('Precisa ser um número')
    print(f'F(x): {a}x² + {b}x + {c} ')
    fx = a * x**2 + b*x + c
    print(f'F({x}) = {fx} ')

def calc_vertice(a,b,c):
    delta = b**2 - 4*a*c
    xv = -b/2*a
    yv = -delta/(4*a)
    print(f'Xv = {xv} ')
    print(f'Yv = {yv} ')

def gera_grafico_2_grau(a,b,c):
    raizes = calc_raiz(a,b,c)
    if len(raizes) == 2:
        x1,x2 = raizes
        x = linspace(x2-1,x1+1,5000)
    elif len(raizes) == 1:
        x1 = raizes[0]
        x = linspace(x1-1,x1+1,5000)
    else:
        print('Não é possível fazer gráfico de raizes complexas.')
        return

    y = a*x**2 + b*x + c
    plot(x,y)
    xlabel("x axis")
    ylabel("y axis")
    show()

def menu_func_2_grau():
    print('ax² + bx + c = 0')
    a = b = c = ''
    while type(a) == str or type(b) == str or type(c) == str or a == 0:
        try:
            a = float(input('Informe o valor de \'a\': '))
            b = float(input('Informe o valor de \'b\': '))
            c = float(input('Informe o valor de \'c\': '))
        except:
            print('Precisa ser um número e \'a\' precisa ser diferente de 0')

    while True:
        opcao = menu([1,2,3,4,5], ['1 - Calcular Raízes','2 - Calcular Função em X informado','3 - Calcular Vértice','4 - Gerar Gráfico','5 - Sair'])
        if(opcao == 1):
            calc_raiz(a, b, c)
        elif(opcao == 2):
            calc_func_2_grau(a,b,c)
        elif(opcao == 3):
            calc_vertice(a,b,c)
        elif(opcao == 4):
            gera_grafico_2_grau(a,b,c)
        else:
            break

def tipo_funcao_exp(b):
    if b > 0 and b < 1:
        print('Essa é uma função decrescente.')
    elif b >= 1 :
        print('Essa é uma função crescente.')

def calc_func_exp(a,b):
    x = ''
    while type(x) == str:
        try:
            x = float(input('Informe o valor de X: '))
        except:
            print('Precisa ser um número')
    print(f'f({x}) = {a} * {b}^{x} = {a * b ** x}')

def gera_grafico_exp(a,b):
    x = linspace(1,10,40)
    y = a * b ** x
    fig, ax = subplots(1)
    ax.plot(x,y)

    show()

def menu_func_exp():
    print('f(x) = ab^x')
    a = b = ''
    while type(a) == str or type(b) == str or b == 1 or a == 0:
        try:
            a = float(input('Digite o valor de "a":  '))
            b = float(input('Digite o valor de "b":  '))
        except:
            print('Precisa ser um número, \'b\' precisa ser diferente de 1 e \'a\' precisa ser diferente de 0')
    
    while True:
        opcao = menu([1,2,3,4],['1 - Verificar se é crescente ou decrescente','2 - Calcular função em x pedido','3 - Gerar gráfico','4 - Sair'])
        if opcao == 1:
            tipo_funcao_exp(b)
        elif opcao == 2:
            calc_func_exp(a,b)
        elif opcao == 3:
            gera_grafico_exp(a,b)
        else:
            break

def cria_matriz():
    nLinha = nColuna = ''
    while type(nLinha) == str or type(nColuna) == str:
        try:
            nLinha = int(input('Informe o número de linhas: '))
            nColuna = int(input('Informe o número de colunas: '))
            if(nLinha <= 0 or nColuna <= 0):
                raise IndexError
        except:
            nLinha = nColuna = ''
            print('Precisa ser um número inteiro e maior que 0.')

    matriz = [0] * nLinha
    for linha in range(nLinha):
        matriz[linha] = [0] * nColuna

    linha = coluna = 0
    while linha < nLinha:
        while coluna < nColuna:
            try:
                matriz[linha][coluna] = round(float(input(f'Informe o elemento [{linha}][{coluna}]: ')), 2)
                coluna += 1
            except:
                print('Informe um número')
        coluna = 0
        linha += 1
    
    for i in range(nLinha):
        print(matriz[i])

    return matriz

def determinante(matriz):
    if(len(matriz) != len(matriz[0])):
        print('Não é possível fazer o determinante dessa matriz, ela precisa ser quadrada.')
    else:        
        if len(matriz) == 1:
            print(f'O determinante é {matriz[0][0]} ')
        elif len(matriz) == 2 :
            determinante = matriz[0][0] * matriz[1][1] - matriz[1][0] * matriz[0][1]
            print(f'O determinante é {determinante} ')
        elif len(matriz) == 3 :
            determinante = matriz[0][0] * matriz[1][1] * matriz[2][2] + matriz[0][1] * matriz[1][2] * matriz [2][0] + matriz[0][2] * matriz[1][0] * matriz[2][1] - matriz[0][2] * matriz[1][1] * matriz[2][0] - matriz[0][1] * matriz[1][0] * matriz[2][2] - matriz[0][0] * matriz[1][2] * matriz[2][1]
            print(f'O determinante é {determinante} ')

def mult_matriz(matriz_1):
    matriz_2 = cria_matriz()

    nLinha_matriz_1, nColuna_matriz_1 = len(matriz_1), len(matriz_1[0])
    nLinha_matriz_2, nColuna_matriz_2 = len(matriz_2), len(matriz_2[0])

    if nColuna_matriz_1 != nLinha_matriz_2:
        print('O produto dessa matriz não existe.')
    else:
        matriz_produto = []
        for linha in range(nLinha_matriz_1):
            matriz_produto.append([])
            for coluna in range(nColuna_matriz_2):
                matriz_produto[linha].append(0)
                for k in range(nColuna_matriz_1):
                    matriz_produto[linha][coluna] += matriz_1[linha][k] * matriz_2[k][coluna]
        print()
        for i in range(nLinha_matriz_1):
            print(matriz_produto[i])

def matriz_transposta(matriz):
    num_linha, num_coluna = len(matriz), len(matriz[0])
    matriz_transposta = []
    for linha in range(num_coluna):
        matriz_transposta.append([])
        for coluna in range(num_linha):
            matriz_transposta[linha].append(matriz[coluna][linha])
    print()
    for i in range(num_linha):
        print(matriz_transposta[i])

def menu_matriz():
    matriz_1 = cria_matriz()

    while True:
        opcao = menu([1,2,3,4],['1 - Determinante (2X2 ou 3x3)','2 - Multiplicação','3 - Matriz transposta','4 - Sair'])
        if(opcao == 1):
            determinante(matriz_1)
        elif(opcao == 2):
            mult_matriz(matriz_1)
        elif(opcao == 3):
            matriz_transposta(matriz_1)
        else:
            break

while True:
    opcao = menu([1,2,3,4],['1 - Funções do segundo grau','2 - Funções exponenciais','3 - Matrizes','4 - Sair'])

    if(opcao == 1):
        menu_func_2_grau()
    elif(opcao == 2):
        menu_func_exp()
    elif(opcao == 3):
        menu_matriz()
    elif(opcao == 4):
        break
