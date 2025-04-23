def processar_lista(numeros):
    return sorted(
        map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numeros)),
        reverse=True
    )

# Exemplo
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(processar_lista(numeros))  # [20, 16, 12, 8, 4]


map,lambda x: x * 2,               # Transforma: multiplica cada número por 2
filter(lambda x: x % 2 == 0,       # Filtra: mantém apenas os pares
numeros)                           # Fonte: lista original
reverse=True                       # Ordena em ordem decrescente