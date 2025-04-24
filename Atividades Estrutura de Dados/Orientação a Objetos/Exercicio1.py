numero1 = '123-4'
titular1 = "João"
saldo1 = 120.0
limite1 = 1000.0

numero2 = '123-5'
titular2 = "José"
saldo2 = 200.0
limite2 = 1000.0

# Dicionário que representa uma conta bancária
conta = {"numero": '123-4', "titular": "João", "saldo": 120.0, "limite": 1000.0}

# Imprimindo os valores do dicionário
print(f'O número da conta é: {conta["numero"]}')
print(f'O titular da conta é: {conta["titular"]}')
print(f'O saldo da conta é: R${conta["saldo"]}')
print(f'O limite da conta é: R${conta["limite"]}')