palavras = {"banana", "Abacate", "pera", "Amora", "uva", "aveia", "abacate", "abacaxi", "abacate", "banana", "uva", "pera", "maçã"}

def comecaComA(palavra):
    return palavra.lower().startswith("a")

def caixaAlta(palavra):
    return palavra.upper()


# A função filter(comecaComA, palavras) filtra as palavras que começam com a letra "a" (ignorando maiúsculas e minúsculas).
filtro = filter(comecaComA, palavras)

# A função map(caixaAlta, filtro) transforma as palavras filtradas em letras maiúsculas.
maiusculas = map(caixaAlta, filtro)

# A função sorted(maiusculas) ordena as palavras em ordem alfabetica.
ordenado = sorted(maiusculas)

# A função set(ordenado) remove as palavras duplicadas.
resultado = set(ordenado)

print(resultado)



