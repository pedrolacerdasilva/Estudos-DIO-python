#instruções projeto-desafio:
#Separar Funções de saque depósito ou extrato e criar as funções Cadastrar usuário (cliente) e cadastrar conta bancária (e viculá-la ao cliente).
#Saque deve receber argumentos por "keyword only" (saldo, valor, extrato, limite, numero_saques, limite _saques) deve retornar, pelo menos saldo e extrato.
#Deposito deve receber argumentos por "positional only" (saldo, valor, extrato) deve retornar, pelo menos saldo e extrato.
#Extrato deve receber argumentos por ambos "keyword only" e "positional only" (saldo sendo posicional e extrato sendo nomeado.
#Bônus, criar uma função para listar as contas que um cliente tem (se houver mais de um cpf igual em cliente, bloquear criação)
#Cadastrar usuário (cliente), deve armazenar as informações do mesmo em uma lista, e deve ser composta por: nome, data de nascimento, CPF, e endereço (string com o formato: CEP, logradouro, nro, bairro, cidade/sigla, estado) 
#Cadastrar conta bancária (e viculá-la ao cliente), deve armazenar as informações da mesmo em uma lista e deve ser composta por: agencia, numero da conta e cpf do usuário(cada conta criada pode ter quantos números forem necessários, e a agência tem quatro números (depende do local mas nesse exercício devese usa uma que tenha io número 0001))
#um usuário pode ter diversas contas mas uma conta só pode ter um usuário
#dica: Para vincular um usuário a uma conta, filtre a lista de usuários buscando por cpf para cada usuario na lista

import textwrap


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    limite = saldo * 0.10  
    # informação: o limite de saque agora é calculado dinamicamente
    # como 10% do saldo atual, substituindo o limite fixo anterior

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append(
        {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "endereco": endereco,
        }
    )

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def listar_contas_cliente(contas):
    # informação: função adicionada para atender ao bônus do desafio,
    # permitindo listar apenas as contas vinculadas a um CPF específico

    cpf = input("Informe o CPF do usuário: ")

    contas_cliente = [
        conta for conta in contas if conta["usuario"]["cpf"] == cpf
    ]
    # informação: filtragem das contas usando o CPF do usuário vinculado

    if not contas_cliente:
        print("\n@@@ Nenhuma conta encontrada para este CPF! @@@")
        return

    for conta in contas_cliente:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 0  
    # informação: a variável limite foi mantida apenas para compatibilidade
    # com a assinatura da função sacar, pois agora o limite é calculado internamente

    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
            # informação: o limite passado é ignorado, pois o cálculo
            # de 10% do saldo ocorre dentro da função sacar

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)
            listar_contas_cliente(contas)
            # informação: chamada adicional para permitir listar contas
            # por cliente, conforme bônus do desafio

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
