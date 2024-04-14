# SISTEMA BANCÁRIO BÁSICO #

print("Olá! Seja bem vindo ao banco Dante_Cross\nO que faremos hoje?")

#Partindo da ideia que a pessoa possui 200 reais de saldo inicial
saldo = 200
sacar = True
saques_diarios = 3
ordem_saque = 1
operacoes = []

while True:
    opcao = int(input("Escolha a opção desejada:\n [1] Depósito\n [2] Saque\n [3] Extrato\n [4] Finalizar atendimento\n"))
    
    if opcao == 4:
        break

    if opcao == 1:
        try:
            deposito = float(input("Digite o valor de deposito: R$ "))
            saldo += deposito
            print(f"O saldo atual é de R$ {saldo}")
            operacoes.append("Depósito no valor de: R$" + f"{deposito:.2f}")
        except:
                print("Foi digitado uma opção inválida!\nTente novamente")
                
    if opcao == 2:
        if saques_diarios == 0 and sacar: 
            try: 
                valor_saque= float(input("Digite o valor de saque: R$ "))
                if valor_saque <= 0 and valor_saque > 500:
                    print("Valor de saque inválido!")
                elif saldo < valor_saque:
                    print("Você não possuir valor em conta para saque.")
                    print("Realize uma nova solicitação.")
                    break
                else:
                    print(f"O saque no valor de R$ {valor_saque:.2f} foi realizado com sucesso!")
                    saldo -= valor_saque
                    operacoes.append(f"Saque {ordem_saque} no valor de: R$" + f"{valor_saque:.2f}")
                saques_diarios -= 1
                ordem_saque += 1
                print(f"{saques_diarios} diários restantes.")
            except:
                print("Foi digitado uma opção inválida!\nTente novamente")
        else:
            print("Você não pode realizar mais saques hoje!\nTente novamente amanhã.")

    if opcao == 3:
        print(f"A conta atual possui: R$ {saldo}!")
        print("Operações realizadas no último atendimento:\n")
        for x in operacoes:
            print(x)
        print("\nDeseja realizar alguma nova consulta?\n")

print("O banco Dante_Cross agradeçe o seu contato, foi um prazer negociar com você!")
