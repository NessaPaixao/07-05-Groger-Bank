cliente = input("Digite seu nome completo: ")
idade = int(input("Digite sua idade: "))
saldo = float(input("Digite seu saldo: "))

def opcoes():
    print("Digite (1) para saque")
    print("Digite (2) para depósito")
    print("Digite (3) para empréstimo")
    print("Digite (4) para visualizar informações")
    print("Digite (Qualquer outro texto ou número) para sair")
    menu = float(input(""))

    if menu == "1":
        saque()

    elif menu == "2":
        deposito

if saldo:
    opcoes();

def saque():
    valor_saque = float(input("Digite o valor do saque"))
    if valor_saque > 1000 or saldo <= float(valor_saque):
        print("Valor solicitado negado")

    else:
         valor_atual = saque - valor_saque
         print("Seu saldo é:" + "R$" + (valor_atual))






def deposito():
    valor_deposito = float(input("Digite o valor do deposito"))
    if









