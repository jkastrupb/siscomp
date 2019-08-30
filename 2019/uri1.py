idade_dias = int(input())
dia = 1
mes = 30
ano = 365

anos = idade_dias // ano
resto = idade_dias % ano
meses = resto//mes
dias = resto % mes
 
print("%d ano(s)" %anos)
print("%d mes(es)" %meses)
print("%d dia(s)" %dias)