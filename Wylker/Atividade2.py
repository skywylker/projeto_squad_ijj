import sys
from datetime import datetime
sys.stdout.reconfigure(encoding="utf-8")

nome_cliente = "Paula Martins"
primeiro_nome = nome_cliente.split()[0].upper()
mes = "Janeiro"
valor_compras = 500.00
desconto = 10
cupom_desconto = f"{primeiro_nome}É{desconto}"

print(f"Olá {nome_cliente}. Em {mes}, você fez compras no valor de R$ {valor_compras} e ganhou um desconto de {desconto}% em sua próxima compra. Use o cupom {cupom_desconto} para obter o desconto.")



# Perguntar sobre codificação UTF-8 e saída de texto com caracteres especiais.