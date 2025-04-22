# 1 - Filtragem e Transformação de Listas

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
par = list(filter(lambda x: x % 2 == 0, numeros))
dobro = list(map(lambda x: x * 2, par))
ordem = list(sorted(dobro,reverse=True))

print (ordem)
