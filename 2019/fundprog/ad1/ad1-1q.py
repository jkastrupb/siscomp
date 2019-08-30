numeros = []
numero = 0

while numero != "":
    numero = input()
    if numero != "":
        numeros.append(numero)

qtd_num = len(numeros)

print(f"Quantidade de Números: {qtd_num}")
if qtd_num != 0:
    numeros = [float(numero) for numero in numeros]
    media = sum(numeros) / qtd_num
    numeros.sort()
    maior_numero = numeros[-1]
    print(f"Média dos Números: {media}")
    print(f"Maior: {maior_numero}")

