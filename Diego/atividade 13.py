def processar_set(palavras):
    return set(sorted(
        map(str.upper, filter(lambda x: x.lower().startswith("a"), palavras))
    ))

# Exemplo
palavras = {"banana", "Abacate", "pera", "Amora", "uva", "aveia"}
print(processar_set(palavras))  # {'AMORA', 'ABACATE', 'AVEIA'}

map,str.upper,                                     # Transforma: deixa tudo em maiúsculo
filter,lambda x: x.lower().startswith("a"),        # Filtra: só palavras que começam com "a" (ou "A")
palavras                                           # Fonte: conjunto original