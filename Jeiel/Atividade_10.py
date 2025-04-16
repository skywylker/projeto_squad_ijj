# 4 - Filtragem e Transformação de Valores de Dicionário

dicionario = {"a": 10, "b": "banana", "c": "abacaxi", "d": 5, "e": "uva", "f": "melancia"}

texto3 = dict(filter(lambda x: isinstance(x[1], str) and len(x[1]) > 3, dicionario.items()))
maiuscula = dict(map(lambda x: (x[0], x[1].upper()), texto3.items()))
ordem = dict(sorted(maiuscula.items(), reverse= False))

print (ordem)


