saldo_inicial = 1500
valor_produto = 450.50
taxa_servico = 10
custo_total = taxa_servico + valor_produto
saldo_inicial -= custo_total
print(saldo_inicial)
saldo = 1500.00
limite_cartao = 500.00
#REQUESITO 1 - O saldo em conta é suficiente?
saldo_suficiente = saldo >= valor_produto
#REQUESITO 2 - O valor está dentro do limite do cartão?
limite_ok = valor_produto <= limite_cartao
#REQUESITO 3 - A compra é aprovada se ambos forem true
aprovacao = saldo_suficiente and limite_ok
#TELA DE SAÍDA
print("\n--- Resultado do Teste Lógico")
print(f"Saldo Suficiente? {saldo_suficiente}")
print(f"Limite ok? {limite_ok}")
print(f"Aprovação Final (AND) : {aprovacao}")
carrinho = ["notebook" , "mouse" , "monitor" , "teclado"]
item_promocional = "monitor"
print(item_promocional in carrinho)
margem_de_lucro = 500.00
print(limite_cartao is margem_de_lucro)
