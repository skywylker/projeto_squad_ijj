import time

print('Olá, seja bem-vindo à calculadora canina da PetMaster!')
time.sleep(3)
print('vamos descobrir a idade do seu cachorro em idades humanos!')
time.sleep(3)
print('Lembre-se: 1 ano humano é equivalente a 7 anos caninos.')
time.sleep(3)

nomeCachorro = input('Qual é o nome do seu cachorro?:')
idadePet = int(input('Agora digite a idade do seu pet:'))
idadeReal = idadePet * 7
print(f'A idade do seu pet, em idade humana é de {idadeReal} anos:')

banhoGrandePorte = 75.00
custoBanhoGrandePorte = 20.00
lucroBanhoGrandePorte = banhoGrandePorte - custoBanhoGrandePorte
banhoMedioPorte = 60.00
custoBanhoMedioPorte = 15.00
lucroBanhoMedioPorte = banhoMedioPorte - custoBanhoMedioPorte
banhoPequenoPorte = 50.00
custobanhoPequenoPorte = 5.00
lucroBanhoPequenoPorte = banhoPequenoPorte - custobanhoPequenoPorte


print('\nAgora vamos calcular p lucro obtido com os banhos do seu cachorro nos últimos 12 meses.')
time.sleep (4)
quantidadesDeBanhos = int(input('Quantos banhos foi dado a o seu pet nos últimos 12 meses?'))
tamanhoCachorro = input('Qual o tamanho do seu pet? (Grande, Médio ou Pequeno): ').strip().lower()

if tamanhoCachorro == 'grande':
    lucro = quantidadesDeBanhos * lucroBanhoGrandePorte
    print(f'{nomeCachorro} tem {idadeReal} anos e o lucro de banho nos últimos 12 meses foi de R$ {lucro:.2f}')
elif tamanhoCachorro in ['médio', 'medio']:
    lucro = quantidadesDeBanhos * lucroBanhoMedioPorte
    print(f'{nomeCachorro} tem {idadeReal} anos e o lucro de banho nos últimos 12 meses foi de R$ {lucro:.2f}')
elif tamanhoCachorro == 'pequeno':
    lucro = quantidadesDeBanhos * lucroBanhoPequenoPorte
    print(f'{nomeCachorro} tem {idadeReal} anos e o lucro de banho nos últimos 12 meses foi de R$ {lucro:.2f}')
else:
    print('tamanho de cachorro inválido.')