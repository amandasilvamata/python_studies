# exercicio 1 e 2

gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

soma = sum(gastos)
quantidade = len(gastos)

media = soma / quantidade

print(media)
totalCompras = 0

for gasto in gastos:
    if gasto > 3000:
        totalCompras += gasto

porcentagemTotal = (totalCompras / soma) * 100
print (round(porcentagemTotal,2))

# exercicio 3 e 4
import random 

numeros = [ 29, 49, 9, 76, 19, 1, 86, 97, 15, 34]
sorteados = []

for _ in range(5):
    numero = (random.choice(numeros))
    sorteados.append(numero)

print(sorteados)

print(sorteados[::-1])