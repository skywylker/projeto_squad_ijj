dados = ("maçã", 10, "banana", 5, "laranja", "uva", 20)

def processarTupla(dados):
    apenasStrings = []
    for elemento in dados:
        if isinstance(elemento, str):
            apenasStrings.append(elemento)

    maiusculas = []
    for elemento in apenasStrings:
        maiusculas.append(elemento.upper())

    ordenadas = sorted(maiusculas)
    return tuple(ordenadas)

print(processarTupla(dados))
