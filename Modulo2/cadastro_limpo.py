#1. Obter os dados:
nome_completo_entrada = input("Informe o nome completo do produto:")
id_produto_entrada = input("Informe o ID do Produto:")
#2. Limpar e Normatizar o nome
produto_formatado = nome_completo_entrada.strip().title()
#3. Padronizar o ID do Produto
id_formatado = id_produto_entrada.upper().center(10, '*')
#4. Gerar Log de Confirmação (F-string)
mensagem = f"""
--- LOG DE CADASTRO ---
Produto: {produto_formatado}
ID: {id_formatado}
"""
print(mensagem.strip())