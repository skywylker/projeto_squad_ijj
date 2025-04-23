def processar_tupla(dados):
    return tuple(sorted(
        map(str.upper, filter(lambda x: isinstance(x, str), dados))
    ))

# Exemplo
dados = ("maçã", 10, "banana", 5, "laranja", "uva", 20)
print(processar_tupla(dados))  # ('BANANA', 'LARANJA', 'MAÇÃ', 'UVA')

map,str.upper,                               # Transforma: deixa tudo em MAIÚSCULO
filter,lambda x: isinstance(x, str),         # Filtra: apenas strings
dados                                        # Fonte: tupla original