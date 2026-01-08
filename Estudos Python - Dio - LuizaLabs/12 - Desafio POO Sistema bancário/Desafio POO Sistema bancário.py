# Iniciar a modelagem do sistema bancário POO. Adicionar classes para cliente e as operações bancárias: depósito e saque.
# Atualizar a implementação do sistema bancário, para armazenar os dados de clientes e contas bancárias em objetos ao invés de dicionários.
# O código deve seguir o modelo de classes UML a seguir:Modelo UML de um sistema bancário orientado a objetos composto por Cliente, Conta, Transações e Histórico. A interface Transacao define o método registrar(conta), sendo implementada por Deposito e Saque, ambos com atributo valor. A classe Conta possui saldo, numero, agencia, cliente e um Historico (composição), além dos métodos nova_conta, sacar, depositar e saldo; cada conta mantém um Historico que armazena uma lista de transações via adicionar_transacao. ContaCorrente herda de Conta e adiciona limite e limite_saques. A classe Cliente possui endereco e uma lista de contas, podendo adicionar_conta e realizar_transacao(conta, transacao), orquestrando a execução das transações. PessoaFisica herda de Cliente e acrescenta cpf, nome e data_nascimento. Relacionamentos principais: um cliente pode ter várias contas, cada conta pertence a um cliente, toda conta possui exatamente um histórico, o histórico agrega várias transações, e as transações são executadas conforme o contrato definido pela interface Transacao.

import textwrap
from abc import ABC, abstractmethod


# ==========================================================
# MENU permanece como função, igual ao código base
# ==========================================================
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


# TRANSACAO:criação da interface Transacao conforme UML

class Transacao(ABC):

    @abstractmethod
    def registrar(self, conta):
        pass

# HISTORICO: extrato deixa de ser string e vira objeto

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

# DEPOSITO: função depositar virou classe

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if self.valor <= 0:
            return False

        conta.saldo += self.valor
        conta.historico.adicionar_transacao(self)
        return True

# SAQUE função sacar virou classe

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if self.valor <= 0:
            return False

        if self.valor > conta.saldo:
            return False

        conta.saldo -= self.valor
        conta.historico.adicionar_transacao(self)
        return True


# CLIENTE (NOVO)
# ALTERAÇÃO: usuário deixa de ser dicionário

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        return transacao.registrar(conta)

# PESSOA FISICA: especialização de Cliente

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento



# CONTA: saldo e extrato agora pertencem à conta

class Conta:
    def __init__(self, numero, agencia, cliente):
        self.saldo = 0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero=numero, agencia="0001", cliente=cliente)

    def depositar(self, valor):
        return Deposito(valor).registrar(self)

    def sacar(self, valor):
        return Saque(valor).registrar(self)


# CONTA CORRENTE: herança de Conta

class ContaCorrente(Conta):
    def __init__(self, numero, agencia, cliente, limite=500, limite_saques=3):
        super().__init__(numero, agencia, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

# MAIN

def main():
    AGENCIA = "0001"

    # ALTERAÇÃO: listas agora armazenam objetos
    clientes = []
    contas = []

    while True:
        opcao = menu()

        # NOVO USUÁRIO
        
        if opcao == "nu":
            cpf = input("Informe o CPF (somente número): ")

            # ALTERAÇÃO: busca em objetos ao invés de dicionários
            usuario = next((c for c in clientes if c.cpf == cpf), None)

            if usuario:
                print("Usuário já existe!")
                continue

            nome = input("Informe o nome completo: ")
            data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
            endereco = input("Informe o endereço: ")

            cliente = PessoaFisica(
                nome=nome,
                cpf=cpf,
                data_nascimento=data_nascimento,
                endereco=endereco
            )

            clientes.append(cliente)
            print("Usuário criado com sucesso!")

        
        # NOVA CONTA
        
        elif opcao == "nc":
            cpf = input("Informe o CPF do usuário: ")
            cliente = next((c for c in clientes if c.cpf == cpf), None)

            if not cliente:
                print("Usuário não encontrado.")
                continue

            numero_conta = len(contas) + 1

            conta = ContaCorrente(
                numero=numero_conta,
                agencia=AGENCIA,
                cliente=cliente
            )

            cliente.adicionar_conta(conta)
            contas.append(conta)

            print("Conta criada com sucesso!")

        # DEPOSITO
        
        elif opcao == "d":
            if contas:
                valor = float(input("Informe o valor do depósito: "))
                if contas[0].depositar(valor):
                    print("Depósito realizado com sucesso!")
                else:
                    print("Falha no depósito.")
        
        # SAQUE
        
        elif opcao == "s":
            if contas:
                valor = float(input("Informe o valor do saque: "))
                if contas[0].sacar(valor):
                    print("Saque realizado com sucesso!")
                else:
                    print("Falha no saque.")

        # EXTRATO
        
        elif opcao == "e":
            if contas:
                print("\n================ EXTRATO ================")
                for transacao in contas[0].historico.transacoes:
                    print(f"{type(transacao).__name__}:\tR$ {transacao.valor:.2f}")
                print(f"\nSaldo:\t\tR$ {contas[0].saldo:.2f}")
                print("========================================")
        
        # LISTAR CONTAS
        
        elif opcao == "lc":
            for conta in contas:
                print(
                    f"Agência:\t{conta.agencia}\n"
                    f"C/C:\t\t{conta.numero}\n"
                    f"Titular:\t{conta.cliente.nome}\n"
                    + "-" * 30
                )
        
        # SAIR
        
        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente.")


if __name__ == "__main__":
    main()