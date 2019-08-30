numeros = []

linha_numeros = input()
if linha_numeros == "":
    print("Nenhum número foi lido!!!")
else:
    numeros = linha_numeros.split(" ")
    numeros = [float(numero) for numero in numeros]
    frequencia = {numeros.count(numero):numero for numero in numeros}

def ordenar_frequencia:


    print(f"Valor que mais ocorreu: {numeros} que foi encontrado: {numeros[-1]} vez(es)")