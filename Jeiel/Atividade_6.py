nome_pet = input("Digite o nome do seu cachorro: ")
idade_pet = int(input("Digite a idade do seu cachorro: ")) 
anos_de_cachorro = idade_pet * 7

print (f'Seu cachorro tem {anos_de_cachorro} anos')

banho_grande = 75.00
banho_medio = 60.00
banho_pequeno = 50.00

custo_grande = 20.00
custo_medio = 15.00
custo_pequeno = 5.00

lucro_grande = banho_grande - custo_grande
lucro_medio = banho_medio - custo_medio
lucro_pequeno = banho_pequeno - custo_pequeno

qtd_banho = int(input(F'Quantos banhos foram dados no {nome_pet} em 1 ano?: '))
tamanho_pet = input(f'Qual tamanho do {nome_pet}? (Pequeno, Médio, Grande): ').lower

if tamanho_pet == 'grande':
    valor = lucro_grande * qtd_banho
    print (f'Olá, "{nome_pet}" tem {anos_de_cachorro} ano(s) e o lucro com este animal no ultimo ano foi de R${valor:.2f}')
elif tamanho_pet == 'médio' or 'medio':
    valor = lucro_medio * qtd_banho
    print (f'Olá, "{nome_pet}" tem {anos_de_cachorro} ano(s) ano(s) e o lucro com este animal no ultimo ano foi de R${valor:.2f}')
elif tamanho_pet == 'pequeno':
    valor = lucro_pequeno * qtd_banho
    print (f'Olá, "{nome_pet}" tem {anos_de_cachorro} ano(s) ano(s) e o lucro com este animal no ultimo ano foi de R${valor:.2f}')
else:
    print ('Tamanho incorreto')