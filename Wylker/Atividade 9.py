palavras = {"banana", "aVeLã", "Abacate", "pera", "Amora", "UVA", "aveia"}

def processarStrings(palavras):
    palavrasComA = []
    for elemento in palavras:
        if elemento.lower().startswith("a"):
            palavrasComA.append(elemento)

    maiusculas = []
    for elemento in palavrasComA:
        maiusculas.append(elemento.upper())

    ordenadas = sorted(maiusculas)
    return set(ordenadas)


print(processarStrings(palavras))
