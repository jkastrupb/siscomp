def contar_frequencia(frequencia, numero_mais_frequente):
    freq = frequencia[numero_mais_frequente]
    return freq

def obter_num_mais_frequente(frequencia):
    numero_mais_frequente = 0
    quantas_vezes = 0
    for key, value in frequencia.items():
        if value > quantas_vezes:
            numero_mais_frequente = key
            quantas_vezes = value
    return numero_mais_frequente

numeros = []
linha_numeros = input()

if linha_numeros == "":
    print("Nenhum número foi lido!!!")
else:
    numeros = linha_numeros.split(" ")
    numeros = [float(numero) for numero in numeros]
    frequencia = {numero: numeros.count(numero) for numero in numeros}
    numero_mais_frequente = obter_num_mais_frequente(frequencia)
    quantas_vezes = contar_frequencia(frequencia, numero_mais_frequente)
    print(f"Valor que mais ocorreu: {numero_mais_frequente} que foi encontrado: {quantas_vezes} vez(es)")



