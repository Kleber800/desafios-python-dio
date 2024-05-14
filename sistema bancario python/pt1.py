def extrato_action(extrato):
    print("O valor disponível na conta é de:", extrato)

def saque_action(extrato):
    if extrato <= 0:
        print("Você não tem valor disponível para saque.")
    else:
        saque = int(input("Digite aqui o valor do saque: "))
        extrato -= saque
    return extrato

def deposito_action(extrato):
    deposito = int(input("Digite aqui o valor do depósito: "))
    extrato += deposito
    return extrato

def sair_action():
    print("Saindo...")

def main():
    extrato = 0
    opcoes = {
        "1": extrato_action,
        "2": saque_action,
        "3": deposito_action,
        "4": sair_action
    }
    
    while True:
        menu = input("Escolha uma das opções abaixo:\n 1. Extrato\n 2. Saque\n 3. Depósito\n 4. Sair\n Digite a opção desejada: ").strip()
        
        if menu in opcoes:
            if menu == "2":
                extrato = opcoes[menu](extrato)
            else:
                opcoes[menu](extrato)
        else:
            print("Opção inválida")

main()
