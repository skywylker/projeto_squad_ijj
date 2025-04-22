# 3 - Filtragem e Transformação de Sets

palavras = {"banana", "Abacate", "pera", "Amora", "uva", "aveia"}
a = set(filter(lambda x: x.upper().startswith("A"), palavras))
maiuscula = set(map(lambda x: x.upper(), a))
ordem = set(sorted(maiuscula, reverse= False))

print (a)
print (maiuscula)
print (ordem)

