import pandas as pd

df = pd.read_csv('Diego\dados.csv')

print('Digite 1 para mostrar os nomes das pessoas com mais de 40 anos:\n Digite 2 para saber os quem tem as rendas maiores que 5 mil:\n Digite 3 para saber os quem tem as rendas maiores que 15 mil:')


#print("Dados iniciais:")
#print(df.head())

filtro_idade = df[df['idade'] > 40]
#print("\nPessoas com mais de 40 anos:")
#print(filtro_idade)

filtro_renda = df[df['renda'] > 5000.00]
#print("\nPessoas com mais de 5 mil de renda:")
#print(filtro_renda)

filtro_renda2 = df[df['renda'] > 15000.00]
#print("\nPessoas com mais de 15 mil de renda:")
#print(filtro_renda)

opcao = int(input('digite a opção desejada: '))

if opcao == 1:
    print(filtro_idade)
elif opcao == 2:
    print(filtro_renda)
elif opcao == 3:
    print(filtro_renda2)

df_ordenado = df.sort_values(by='idade', ascending=False)

df_ordenado.to_csv('Diego\dados_processados.csv', index=False)

print("\nArquivo 'dados_processados.csv' gerado com sucesso!")
