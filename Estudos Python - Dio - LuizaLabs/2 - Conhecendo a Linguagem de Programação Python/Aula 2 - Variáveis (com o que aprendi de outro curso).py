# O Professos solicitou um programa de caixa, mas muito mais basico do que o a seguir que vou usar como exercício
saldo = 1000
idade = float(input("Favor inserir sua idade: "))

if idade < 18:
    print("Você é menor de idade, portanto não pode ter uma conta bancária.")
else:
    nome = input("Favor inserir o nome do usuário: ")
    print(f"Prezado usuário: {nome}, segue abaixo seu saldo:\nR$ {saldo:.2f}")

    opcao = 0

    while opcao != 3:
        print("\nFavor selecionar uma das opções abaixo:")
        print("1. Sacar")
        print("2. Depositar")
        print("3. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:  # SACAR
            if saldo > 0:
                saque = float(input("Quanto você deseja sacar da sua conta? R$ "))

                if saque > saldo:
                    print("Saldo insuficiente! Você não pode sacar mais do que possui.")
                else:
                    saldo = saldo - saque
                    print(f"Você sacou R$ {saque:.2f}. Seu saldo atual é: R$ {saldo:.2f}")
            else:
                print("Seu saldo está zerado. Não é possível fazer saque.")

        elif opcao == 2:  # DEPOSITAR
            deposito = float(input("Quanto você deseja depositar na sua conta? R$ "))
            saldo = saldo + deposito
            print(f"Você depositou R$ {deposito:.2f}. Seu saldo atual é: R$ {saldo:.2f}")

        elif opcao == 3:  # SAIR
            print(f"Programa encerrado.\nSeu saldo final é: R$ {saldo:.2f}")

        else:
            print("Opção inválida. Tente novamente.")