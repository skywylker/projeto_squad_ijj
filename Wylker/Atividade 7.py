numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def numerosPares(x):
    return x % 2 == 0

def dobro(x):
    return x * 2

# A função filter(numerosPares, numeros) filtra os números pares da lista numeros.
filtro = filter(numerosPares, numeros)

# A função map(dobro, filtro) aplica a função dobro a cada elemento da lista filtrada.
numeroDobrado = map(dobro, filtro)

# A função sorted(numeroDobrado, reverse=True) ordena os números dobrados em ordem decrescente.
resultado = sorted(numeroDobrado, reverse=True)

print(resultado)


# resultado = sorted(
#     list(map(dobro, list(filter(numerosPares, numeros)))), reverse=True)

# A função map(dobro) pega item por item da lista numeros, multiplica por 2 e retorna 
# filter numerosPares, numero, filtra a lista numero por numeros pares
# A função filter(numerosPares, numeros), pega item por item da lista numeros e aplica a função numerosPares e retorna True ou False.
