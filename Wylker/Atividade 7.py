numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def processarLista(numeros):
    pares = []
    for elemento in numeros:
        if elemento % 2 == 0:
            pares.append(elemento)

    multiplicados = []
    for elemento in pares:
        multiplicados.append(elemento * 2)

    resultado = sorted(multiplicados, reverse=True)
    return resultado

print(processarLista(numeros))