conta_normal = True
conta_universitaria = False

saldo = 3000
saque = 2000
cheque_especial = 450

if conta_normal:
    if  saldo >= saque:
        print("Retire seu dinheiro no caixa.")
    
    elif saque <= ( saldo + cheque_especial):
        print("Retire seu dinheiro no caixa.")
    else:
        print("Não há dinheiro o suficiente na conta.")

elif conta_universitaria:
    if saldo >= saque:
        print("Retire seu dinheiro no caixa.")
    elif saque <= (saldo + cheque_especial):
        print("Retire seu dinheiro no caixa.")
    else:
        print("Não há dinheiro o suficiente na conta.")