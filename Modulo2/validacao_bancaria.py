#Definindo as váriáveis a serem usadas
usuario_correto = "elisa"
senha_correta = "123"
saldo = 1000.00
cheque_especial = 500.00
limite_total = saldo + cheque_especial
tentativas_maximas = 3
tentativas_atuais = 0
print("--- SISTEMA BANCÁRIO ---")
#O loop continua ENQUANTO as tentativas atuais forem menores que o limite.
while tentativas_atuais < tentativas_maximas:
    #1. Obter as entradas do usuário
    usuario_digitado = input("Usuário: ")
    senha_digitada = input("Senha: ")
    #2. Verificar sucesso do Login (Operador Lógico 'and')
    if  usuario_digitado == usuario_correto and senha_digitada == senha_correta:
        print ("Login bem-sucedido! Acesso liberado.")
        break
    #3. Se o login falhar
    else:
        tentativas_atuais += 1
        tentativas_restantes = tentativas_maximas - tentativas_atuais
    #4. Checar se o limite foi atingido
        if tentativas_restantes > 0:
            print(f"Usuário ou Senha Incorretos. Tentativas restantes {tentativas_restantes}")
        else:
            print ("Você excedeu o número máximo de tentativas. Conta bloqueada")
#Verificar se o loop terminou por sucesso ou falha
if tentativas_atuais >= tentativas_maximas:
   exit()
#Executar o saque apenas se o login for bem-sucedido
print("\n--- TRANSAÇÃO DE SAQUE ---")
saque = float(input("Informe o valor que deseja sacar: "))
#Possibilidade 1 - o valor do saque é menor ou igual ao saldo.
if saque <= saldo:
    saldo -= saque
    print(f"Saque de R$ {saque:.2f} autorizado com sucesso")
    print(f"novo saldo: R$ {saldo:.2f}")
elif saque <= limite_total:
    saldo -= saque
    uso_cheque = abs(saldo)
    print(f"Saque de R$ {saque:.2f} autorizado com USO DE CHEQUE ESPECIAL")
    print(f"Saldo atual: R$ {saldo:.2f}")
    print(f"Você utilizou R$ {uso_cheque:.2f} do seu limite.")
else:
    print(f"Transação Negada. Saldo insuficiente (R$ {saldo:.2f}) e limite de crédito (R$ {cheque_especial:.2f}) estourado.")
print("--- FIM DA TRANSAÇÃO ---")