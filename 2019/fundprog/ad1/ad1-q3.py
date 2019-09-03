'''Utilizando subprogramação, faça um programa que leia da entrada padrão, em uma única
string, dois números inteiros separados por um espaço em branco, representando as duas
dimensões de uma matriz bidimensional.
Construa uma matriz bidimensional com as dimensões
lidas e com valores gerados aleatoriamente, via função randint importada do módulo
random, no intervalo 100 a 999.
Escreva:
(1) O conteúdo da matriz, onde cada linha a ser escrita possua apenas números inteiros, sem
vírgulas nem colchetes;
(2) A posição (linha, coluna) do maior valor sorteado e o seu respectivo valor;
(3) A soma de cada linha, de todas as linhas da matriz;
(4) A soma de cada coluna, de todas as colunas da matriz'''


# Programa Principal

print("Digite as dimensões da matriz, separados por um espaço em branco:")
dimensoes = input().split()
linhas = int(dimensoes[0])
colunas = int(dimensoes[1])


def gerarMatriz(linhas, colunas):
    from random import randint
    matriz = []
    for linha in range(linhas):
        itensLinha = []
        for coluna in range(colunas):
            itemColuna = randint(100, 999)
            itensLinha.append(itemColuna)
        matriz.append(itensLinha)
    return matriz

matriz = gerarMatriz(linhas, colunas)

'''(1) O conteúdo da matriz, onde cada linha 
a ser escrita possua apenas números inteiros, 
sem vírgulas nem colchetes;'''
def mostraMatrizFormatada(matriz):
    for linha in matriz:
        linha_str = ""
        for item in linha:
            item = str(item)
            linha_str += f"{item} "
        print(linha_str)


'''(2) A posição (linha, coluna) do maior 
valor sorteado e o seu respectivo valor;'''


def encontraMaiorValor(matriz):
    local = (0, 0)
    maior_valor = 0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if matriz[linha][coluna] > matriz[local[0]][local[1]]:
                local = (linha, coluna)
                maior_valor = matriz[linha][coluna]
    print(f"Posição do maior: {local} Maior valor: {maior_valor}")


'''(3) A soma de cada linha, 
de todas as linhas da matriz;'''

def somaItensLinhas(matriz):
    posLinha = 0
    for linha in matriz:
        posLinha = matriz.index(linha)
        soma = sum(linha)
        print(f"Soma da Linha {posLinha} = {soma}")


'''(4) A soma de cada coluna, 
de todas as colunas da matriz.'''


def somaItensColunas(matriz):
    numColunas = len(matriz[0])
    for posColuna in range(numColunas):
        totalColuna = 0
        for linha in matriz:
            totalColuna += linha[posColuna]
        print(f"Soma da Coluna {posColuna} = {totalColuna}")





mostraMatrizFormatada(matriz)
encontraMaiorValor(matriz)
somaItensLinhas(matriz)
somaItensColunas(matriz)
