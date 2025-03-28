nome = input("Nome de usuario:")
altura = input("Altura (em metros):")

print (f"usuario: {nome}, Altura: {altura}")

PrimeiraNota = float(input("Digite sua primeira nota: "))
SegundaNota = float(input("Digite sua segunda nota: "))
soma = PrimeiraNota + SegundaNota
mediaNotas = soma / 2

print(f"A soma das notas é: {soma:.2f} e sua média foi de {mediaNotas:.2f}")