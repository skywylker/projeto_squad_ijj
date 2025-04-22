# O que é função?

# Um bloco de código reutilizável que executa uma ou mais instruções quando é chamado
# Pode receber dados de entrada (parâmetros) e devolver um resultado (return)

# De maneira análoga:

# Função é como se fosse uma cafeteira.
# Se você ligar ela sem nada, não vai fazer café.
# Se você colocar água e cáfe (parâmetros) o resultado (return) será o café fresquito.

# Exemplo do código de uma função básica

def nome_da_funcao(parametros):
    # bloco de código
    return resultado

# def: diz pro Python que você tá criando uma função
# nome_da_funcao: é o nome que você dá pra chamar essa função depois
# (parametros): são os ingredientes que essa função precisa
# return: é o resultado que a função vai devolver pra você
    
### Exemplo 1 ###

def diga_ola():
    print("Olá mundo!")

diga_ola

### Exemplo 2 ###

def somar(a, b):
    resultado = a + b
    return resultado

print(somar(5, 3))  # Vai imprimir: 8


### Exemplo 3 ###

def classificar_idade(idade):
    if idade < 12:
        return "Criança"
    elif idade < 18:
        return "Adolescente"
    elif idade < 60:
        return "Adulto"
    else:
        return "Idoso"

print(classificar_idade(25))  # Vai imprimir: Adulto


### Exemplo 4 ###

def calcular_preco_com_desconto(preco, desconto_em_porcentagem):
    if desconto_em_porcentagem < 0 or desconto_em_porcentagem > 100:
        return "Desconto inválido."
    
    valor_do_desconto = preco * (desconto_em_porcentagem / 100)
    preco_final = preco - valor_do_desconto
    return preco_final

print(calcular_preco_com_desconto(100, 10))  # Vai imprimir: 90

