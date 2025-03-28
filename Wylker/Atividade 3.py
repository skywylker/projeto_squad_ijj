# Programa simples para entrada de dados

# Input do nome
nome = input("Digite seu nome: ")

# Input da altura
altura = input("Digite sua altura em metros: ")

# Mostra os dados
print(f"Usuário: {nome}, Altura: {altura} m")

# Entrada de notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Cálculo da soma e média
soma_notas = nota1 + nota2
media_notas = soma_notas / 2

# Mostra resultados
print(f"Soma das notas: {soma_notas:.2f}")
print(f"Média das notas: {media_notas:.2f}")