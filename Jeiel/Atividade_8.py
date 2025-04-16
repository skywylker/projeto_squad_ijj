# 2 - Filtragem e Transformação de Tuplas (Strings e Inteiros)

dados = ("maçã", 10, "banana", 5, "laranja", "uva", 20)

texto = list(filter(lambda x: isinstance(x, str), dados))
maiuscula = list(map(lambda x: x.upper(), texto))
ordem = list(sorted(maiuscula, reverse = False))

print (ordem)


