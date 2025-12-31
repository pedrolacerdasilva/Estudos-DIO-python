nome = "Pedro Lacerda"
idade = 37
profissao = "Empregado Público"
linguagem = "Python"
saldo = 10000000.32

dados = {"nome": "Pedro Lacerda", "idade": 37}

print("Nome: %s Idade: %d" % (nome,idade))

print("Nome: {} Idade: {}".format (nome,idade))

print("Nome: {1} Idade: {0}".format (nome,idade))

print("Nome: {1} Idade: {0} Nome:{1} {1}".format (nome,idade))

print("Nome: {nome} Idade: {idade}".format (nome=nome,idade=idade))
 
print("Nome: {name} Idade: {age} {name} {name} {age}".format (age=idade, name=nome))

print("Nome: {nome} Idade: {idade}".format (**dados))

print(f"Nome: {nome} Idade: {idade} Saldo {saldo}")

