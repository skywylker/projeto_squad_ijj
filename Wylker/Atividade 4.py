 # Sistema de cálculo de notas bimestrais #


# Entrada de notas #   
# O usuário deve inserir as notas de cada bimestre, que são armazenadas em variáveis #
# As notas devem ser do tipo float para permitir casas decimais #

notaPrimeiroBimestre = float(input("Digite a nota do primeiro bimestre: "))
notaSegundoBimestre = float(input("Digite a nota do segundo bimestre: "))
notaTerceiroBimestre = float(input("Digite a nota do terceiro bimestre: "))
notaQuartoBimestre = float(input("Digite a nota do quarto bimestre: "))

# Cálculo da média #
# A média é calculada somando as notas dos quatro bimestres e dividindo por 4 #

media = (notaPrimeiroBimestre + notaSegundoBimestre + notaTerceiroBimestre + notaQuartoBimestre) / 4


# Saída do resultado #

print(f"Olá Caíque! Sua Media é: {media:.2f}")

# O if-elif-else é usado para determinar a situação do aluno com base na média #
# Se a média for maior ou igual a 7, o aluno é aprovado #
# Se a média for maior ou igual a 6, o aluno é em recuperação #
# Se a média for menor que 6, o aluno é reprovado #

if media >= 66:
    print(f"Media: {media:.2f}. ALUNO APROVADO!")
elif media == 65:
    print(f"Media: {media:.2f}. ALUNO EM RECUPERAÇÃO!")
else:
    print(f"Media: {media:.2f}. ALUNO REPROVADO!")


