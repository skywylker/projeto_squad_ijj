# 3 - Filtragem e Transformações de Sets

palavras = {'banana', 'Abacate', 'pera', 'amora', 'uva', 'aveia'}
a = set(filter(lambda x: x.upper() .startwith('A'), palavras))
maiscula = set(map(lambda x: x.upper(), a))
ordem = set(sorted(maiscula, reverse= False))

print (a)
print (maiscula)
print (ordem)


# Conjunto de palavras (strings)
palavras = {'banana', 'Abacate', 'pera', 'amora', 'uva', 'aveia'}

# TODO: Filtrar palavras que começam com a letra 'A' (ignorando maiúsculas/minúsculas)
a = set(filter(lambda x: x.upper().startswith('A'), palavras))

# TODO: Transformar todas as palavras filtradas em letras maiúsculas
maiuscula = set(map(lambda x: x.upper(), a))

# TODO: Ordenar as palavras em ordem alfabética (mesmo que o resultado seja convertido de volta em set)
ordem = set(sorted(maiuscula, reverse=False))

# TODO: Imprimir o set com palavras que começam com A
print(a)

# TODO: Imprimir o set com palavras em maiúsculo
print(maiuscula)

# TODO: Imprimir o set com palavras ordenadas (lembrando que sets não mantêm ordem)
print(ordem)
