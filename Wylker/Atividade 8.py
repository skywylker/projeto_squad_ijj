dados = ("maçã", 10, "banana", 5, "laranja", "uva", 20)

def notNumber(x):
    return type(x) != int

def caixaAlta (s):
    return s.upper()

# A função filter(notNumber, dados) filtra os elementos que não são números inteiros.
strings = filter(notNumber, dados)

# A função map(caixaAlta, strings) transforma as strings em letras maiúsculas.
maiusculas = map(caixaAlta, strings)

# A função sorted(maiusculas) ordena as strings em ordem alfabetica.
ordenado = sorted(maiusculas)

# A função tuple(ordenado) converte a lista ordenada em uma tupla.
resultado = tuple(ordenado)

print (resultado)