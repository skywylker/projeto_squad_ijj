# Operadores de caso #

# Recebe um número do usuário #	
# Após, as variáveis são criadas e armazenam os resultados de operações matemáticas #

entradaDados = int(input("Digite um número inteiro de 1 a 20: "))
dobro = entradaDados * 2
triplo = entradaDados * 3
quadrado = entradaDados ** 2
raizQuadrada = entradaDados ** (1/2)
raizCubica = entradaDados ** (1/3)


# Imprime os resultados #

print(f"O número que você digitou: {entradaDados}")
print(f"O dobro do número escolhido é: {dobro}")
print(f"O triplo do número escolhido é: {triplo}")
print(f"O número escolhido elevado ao quadrado é: {quadrado}")
print(f"A raiz quadrada do número escolhido é: {raizQuadrada:.2f}")
print(f"A raiz cúbica do número escolhido é: {raizCubica:.2f}")


'''

# Variante do código #

entradaDados = int(input("Digite um número inteiro de 1 a 20: "))

# Imprime os resultados #

print(f"O número que você digitou: {entradaDados}")
print(f"O dobro do número escolhido é: {entradaDados * 2}")
print(f"O triplo do número escolhido é: {entradaDados * 3}")
print(f"O número escolhido elevado ao quadrado é: {entradaDados ** 2}")
print(f"A raiz quadrada do número escolhido é: {entradaDados ** (1/2)}")
print(f"A raiz cúbica do número escolhido é: {entradaDados ** (1/3)}")

'''

