dicionario = {"a": 10, "b": "banana", "c": "abacaxi", "d": 5, "e": "uva", "f": "melancia"}

def processarDicionario(dicionario):
    strings = []
    for elemento in dicionario.values():
        if isinstance(elemento, str) and len(elemento) > 3:
            strings.append(elemento)

    minusculas = []
    for elemento in strings:
        minusculas.append(elemento.lower())

    ordenadas = sorted(minusculas)
    return ordenadas

print(processarDicionario(dicionario))