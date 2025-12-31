#Funções também são conhecidas como blocos de código
#def é a palavra chan=ve para definição de funções em Python
def exibir_mensagem():
	print("Olá mundo!!!\n")

def exibir_mensagem_2(nome):
	print(f"Seja bem vindo {nome}!\n")

def exibir_mensagem_3(nome="Anônimo"):
	print(f"Seja bem vindo {nome}!\n")

exibir_mensagem()
exibir_mensagem_2(nome="Pedrão") #se o nome não for definido nesta opção, o debug dará erro
exibir_mensagem_3()#na 3, como o nome dafault foi definido como anônimo, ele simplesmente chamará a variável na função de anonimo.
exibir_mensagem_3(nome="Chappie")#se você definir o nome, ele vai chamá-lo

def calcular_total(numeros):
    return sum(numeros)

def retorna_sucessor_e_antecessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

tabela_num = []

for i in range(3):
    num_for = float(input(f"Digite o {i+1}º número: "))
    tabela_num.append(num_for)

# 1️⃣ Imprime o total direto da função
print("Total:", calcular_total(tabela_num))

# 2️⃣ Imprime antecessor e sucessor da soma usando a função dentro da função
print(
    "Antecessor e Sucessor da soma:",
    retorna_sucessor_e_antecessor(
        calcular_total(tabela_num)
    )
)


