'''
A dona de um petshop quer criar um programa para calcular a idade dos cachorros
de seus clientes em "anos de cachorro". Como os pets envelhecem de maneira diferente
dos humanos - cada ano humano representa 7 anos de cachorros.

>> Desafio: Crie um programa em Py que calcule a idade de cachorro com base na idade humana

O que o programa deve conter:
- Solicitar ao usuário a idade do pet, em número inteiro.
- Calcular a idade do pet levando em consideração a idade humana
'''

import time # Importa a biblioteca time para usar a função sleep

print("Olá, seja bem-vindo à calculadora de idade canina da PetMaster!")
time.sleep(2)
print("Vamos descobrir a idade do seu cachorro em anos humanos!")
time.sleep(2)
print("Lembre-se: 1 ano humano equivale a 7 anos caninos.")
time.sleep(2)

nomeCachorro = input("Qual o nome do cachorro? ")
idadePet = int(input("Agora digite a idade do seu doguíneo: "))
idadeReal = idadePet * 7

print(f"A idade do seu pet, em idade humana é de {idadeReal} anos")


################################################ FEATURE ################################################

'''
Além disso, a dona do pet shop deseja calcular, a cada 12 meses, o lucro obtido por banho
e por cachorro.

# Valores banhos
# Cachorro Grande Porte = Banho: R$ 75,00 | Custo: R$ 20,00
# Cachorro Médio Porte = Banho: R$ 60,00 | Custo: R$ 15,00
# Cachorro Pequeno Porte = Banho: R$ 50,00 | Custo: R$ 5,00

'''

print("\nAgora vamos calcular o lucro obtido com os banhos por cachorro nos últimos 12 meses.")
time.sleep(2)

quantidadeBanhos = int(input("Quantos banhos foram dados nos últimos 12 meses? "))
tamanhoCachorro = input("Qual o tamanho do cachorro? (Grande, Médio ou Pequeno): ").strip().lower()
time.sleep(2)

precoBanho = 0
custoBanho = 0
lucro = 0

if tamanhoCachorro == "grande":
    precoBanho  = 75.00
    custoBanho = 20.00

elif tamanhoCachorro in ["medio", "médio"]:
    precoBanho  = 60.00
    custoBanho = 15.00

elif tamanhoCachorro == "pequeno":
    precoBanho  = 50.00
    custoBanho = 5.00
    
else:
    print("Tamanho de cachorro inválido.")
    precoBanho  = 0
    custoBanho = 0

if precoBanho != 0:
    lucro = (precoBanho - custoBanho) * quantidadeBanhos
    mensagem = f"{nomeCachorro} tem {idadeReal} anos e o lucro de banho nos últimos 12 meses foi de R$ {lucro:.2f}"
    print(mensagem)



'''

banhoGrandePorte = 75.00
custoBanhoGrandePorte = 20.00
lucroBanhoGrandePorte = banhoGrandePorte - custoBanhoGrandePorte
banhoMedioPorte = 60.00
custoBanhoMedioPorte = 15.00
lucroBanhoMedioPorte = banhoMedioPorte - custoBanhoMedioPorte
banhoPequenoPorte = 50.00
custoBanhoPequenoPorte = 5.00
lucroBanhoPequenoPorte = banhoPequenoPorte - custoBanhoPequenoPorte

if tamanhoCachorro == "grande":
    lucro = quantidadeBanhos * lucroBanhoGrandePorte
    print(f"{nomeCachorro} tem {idadeReal} anos e o lucro de banho nos últimos 12 meses foi de R$ {lucro:.2f}")
elif tamanhoCachorro in ["medio", "médio"]:
    lucro = quantidadeBanhos * lucroBanhoMedioPorte
    print(f"{nomeCachorro} tem {idadeReal} anos e o lucro de banho nos últimos 12 meses foi de R$ {lucro:.2f}")
elif tamanhoCachorro == "pequeno":
    lucro = quantidadeBanhos * lucroBanhoPequenoPorte
    print(f"{nomeCachorro} tem {idadeReal} anos e o lucro de banho nos últimos 12 meses foi de R$ {lucro:.2f}")
else:
    print("Tamanho de cachorro inválido.")

'''

