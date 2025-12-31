from datetime import date   # ← CORREÇÃO AQUI

def salvar_novo_carro():
    ano_hoje = date.today().year
    carros = []

    opcao_novo_carro = -1  # inicializa a variável

    while opcao_novo_carro != 0:
        opcao_novo_carro = int(input(
            "[1] Inserir\n"
            "[2] Imprimir salvos\n"
            "[0] Sair\n"
            ": "
        ))

        if opcao_novo_carro == 1:
            marca = input("Favor informar a marca do carro: ")
            modelo = input("Favor informar o modelo do carro: ")
            ano = int(input("Favor informar o ano de produção do carro: "))

            if ano < 1886 or ano > ano_hoje:
                print(
                    f"Erro: não existe carro antes do Benz Patent-Motorwagen, fabricado em 1886 de 1886 nem após {ano_hoje}, ,você está tentando me enganar!!"
                )
                continue

            placa_letra = input("Favor informar as 3 primeiras letras da placa: ")
            placa_numero = input("Favor informar os 4 últimos números da placa: ")

            placa = f"{placa_letra.upper()}-{placa_numero}"

            carros.append((marca, modelo, ano, placa))

            print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

        elif opcao_novo_carro == 2:
            print("Lista de carros:")
            for carro in carros:
                print(f"{carro[0]}/{carro[1]}/{carro[2]}/{carro[3]}")

        elif opcao_novo_carro == 0:
            print("Saindo...")

        else:
            print("Não existe essa opção.")
salvar_novo_carro()