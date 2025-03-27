Cliente = "Paula Martins"
Primeiro_nome = Cliente.split()[0].upper()
Mes = "Janeiro"
Valor = 500.00
Desconto = 10
Cupom = f"{Primeiro_nome}É{Desconto}"

print(f"Olá {Cliente}. Em {Mes}, você realizou uma compra no valor de R${Valor} e ganhou um desconto de {Desconto}% em sua próxima compra. Use o cupom {Cupom}.") 