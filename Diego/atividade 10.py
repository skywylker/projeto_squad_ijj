# 4 Filtragem e Tranformação de Valores de Dicionários

dicionario = {'a': 10, 'b': 'banana', 'c': 'abacaxi', 'd': 5, 'e': 'uva', 'f': 'melancia'}

texto3 = dict(filter(lambda x: isinstance(x[1], str) and len(x[1]) > 3, dicionario.items()))
maiuscula = dict(map(lambda x: (x[0], x[1].upper()), texto3.items()))
ordem = dict(sorted(maiuscula.items(), reverse= False))

print (ordem)


# Dicionário com valores mistos (strings e inteiros)
dicionario = {'a': 10, 'b': 'banana', 'c': 'abacaxi', 'd': 5, 'e': 'uva', 'f': 'melancia'}

# TODO: Filtrar apenas os pares cuja chave tem valor do tipo string com mais de 3 caracteres
texto3 = dict(filter(lambda x: isinstance(x[1], str) and len(x[1]) > 3, dicionario.items()))

# TODO: Transformar os valores dessas chaves em letras maiúsculas
maiuscula = dict(map(lambda x: (x[0], x[1].upper()), texto3.items()))

# TODO: Ordenar os itens do dicionário por chave em ordem crescente
ordem = dict(sorted(maiuscula.items(), reverse=False))

# TODO: Imprimir o dicionário resultante
print(ordem)
