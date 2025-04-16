# 1 - Filtragem e Transformações de Listas

numeros = [1, 2 , 3, 4, 5, 6, 7, 8, 9, 10]
par = list(filter(lambda x: x % 2 == 0, numeros))
dobro = list(map(lambda x: x * 2, par))
ordem = list(sorted(dobro,reverse=True))

print (ordem)

# Lista inicial de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# TODO: Filtrar apenas os números pares da lista
par = list(filter(lambda x: x % 2 == 0, numeros))

# TODO: Dobrar o valor de cada número par
dobro = list(map(lambda x: x * 2, par))

# TODO: Ordenar os valores em ordem decrescente
ordem = list(sorted(dobro, reverse=True))

# TODO: Imprimir a lista resultante
print(ordem)
