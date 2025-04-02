# Programa simples para entrada de dados #

# Input do nome #
nome = input("Digite seu nome: ")

# Input da altura #
altura = input("Digite sua altura em metros: ")

# Mostra os dados #
print(f"Usuário: {nome}, Altura: {altura} m")

# Entrada de notas #
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Variável para determinar o tipo de variável #

tipoVariavelNota1 = type(nota1)
tipoVariavelNota2 = type(nota2)

# Cálculo da soma e média #

soma_notas = nota1 + nota2
media_notas = soma_notas / 2


# Mostra resultados #

print(f"A primeira nota é {nota1:.2f} e seu tipo é {tipoVariavelNota1}.")
print(f"A segunda nota é {nota2:.2f} e seu tipo é {tipoVariavelNota2}.")
print(f"Soma das notas: {soma_notas:.2f}.")
print(f"Média das notas: {media_notas:.2f}.")