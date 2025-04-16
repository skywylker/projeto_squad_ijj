# 2 - Filtragem e Transformações de Tuplas (Strings e Interiores)

dados = ('maçã', 10, 'banana', 5, 'laranja', 'uva', 20)

texto = list(filter(lambda x: isinstance(x, str), dados))
maiuscula = list(map(lambda x: x.upper(), texto))
ordem = list(sorted(maiuscula, reverse = False))

print (ordem)


# Tupla contendo dados mistos (strings e números)
dados = ('maçã', 10, 'banana', 5, 'laranja', 'uva', 20)

# TODO: Filtrar apenas os elementos que são do tipo string
texto = list(filter(lambda x: isinstance(x, str), dados))

# TODO: Transformar todas as strings para letras maiúsculas
maiuscula = list(map(lambda x: x.upper(), texto))

# TODO: Ordenar as strings em ordem alfabética crescente
ordem = list(sorted(maiuscula, reverse=False))

# TODO: Imprimir a lista resultante
print(ordem)
