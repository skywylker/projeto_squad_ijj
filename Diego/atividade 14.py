def processar_dicionario(dicionario):
    return sorted(
        map(str.lower, filter(lambda x: isinstance(x, str) and len(x) > 3, dicionario.values()))
    )

# Exemplo
dicionario = {"a": 10, "b": "banana", "c": "abacaxi", "d": 5, "e": "uva", "f": "melancia"}
print(processar_dicionario(dicionario))  # ['abacaxi', 'banana', 'melancia']


map,str.lower,                                              # Transforma: minúsculo
filter,lambda x: isinstance(x, str) and len(x) > 3,         # Filtra: só strings com mais de 3 caracteres
dicionario.values()                                         # Fonte: os valores do dicionário