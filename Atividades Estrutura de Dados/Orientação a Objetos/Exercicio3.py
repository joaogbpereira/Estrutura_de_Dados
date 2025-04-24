# Função para criar uma conta
def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

# Função para depositar um valor na conta
def deposita(conta, valor):
    if valor > 0:
        conta['saldo'] += valor
        print(f"Depósito de R${valor} realizado. Novo saldo: R${conta['saldo']}")
    else:
        print("Valor de depósito inválido. O valor deve ser positivo.")

# Função para sacar um valor da conta
def sacar(conta, valor):
    if valor > 0:
        if conta['saldo'] >= valor:
            conta['saldo'] -= valor
            print(f"Saque de R${valor} realizado. Novo saldo: R${conta['saldo']}")
        else:
            print("Saldo insuficiente para realizar o saque.")
    else:
        print("Valor de saque inválido. O valor deve ser positivo.")

def extrato(conta):
    print(f"Conta: {conta['numero']}")
    print(f"Titular: {conta['titular']}")
    print(f"Saldo: R${conta['saldo']}")
    print(f"Limite: R${conta['limite']}")
