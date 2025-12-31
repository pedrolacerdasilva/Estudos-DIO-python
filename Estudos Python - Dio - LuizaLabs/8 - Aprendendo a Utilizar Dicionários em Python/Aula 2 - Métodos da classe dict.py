#métodos dict 

#Clear serve para limpar o dicionário: 

contatos = {
	"pedro@gmail.com" : {"nome": "Pedro", "Telefone": "3333-2221"},
	"sarah@gmail.com" : {"nome": "Sarah", "Telefone": "4444-2221"},
	"natasha@gmail.com" : {"nome": "Natasha", "Telefone": "5555-2221"},
	"zulmiro@gmail.com" : {"nome": "Zulmiro", "Telefone": "6666-2221"},
}
print(contatos)

contatos.clear()

print (contatos)

#copy serve para copiar outro dicionário (fácil)
contatos = {
	"pedro@gmail.com" : {"nome": "Pedro", "Telefone": "3333-2221"},
	"sarah@gmail.com" : {"nome": "Sarah", "Telefone": "4444-2221"},
	"natasha@gmail.com" : {"nome": "Natasha", "Telefone": "5555-2221"},
	"zulmiro@gmail.com" : {"nome": "Zulmiro", "Telefone": "6666-2221"},
}

copia = contatos.copy()

print (copia)

# Fromkeys cria espaços nulos no dicionário ou preenche esses espaços com um valor "default"

teste = dict.fromkeys(["nome", "telefone"]) #para valores null(vazios)

print (teste)

teste = dict.fromkeys(["nome", "telefone"], "vazio") #para valores "default"

print (teste)

#Get é uma maneira de acessar valores do dicionário (usando o exemplo de cima)

resultado = contatos.get("chave") # null
print (resultado)

resultado = contatos.get("chave", {}) # vazio
print (resultado)

resultado = contatos.get("natasha@gmail.com", {}) # valor de Natasha
print (resultado)

#itens imprime tuplas

itens = contatos.items()
print (itens)

#keys só imprime as chaves (util para saber quais as chaves que o código tem)

chaves = contatos.keys()
print (chaves)

#pop remove valores

print(copia)
copiapop = copia.pop("natasha@gmail.com",)#vai remover natasha da variável copiapop
print(copiapop)
copiapop = copia.pop("natasha@gmail.com", "Item não existente")# como ele não vai encontrar a Natasha, vai apresentar a mensagoe de erro que você escolheu
print(copiapop)

#popitem faz o mesmo, mas você não declara a chave e ele paga por sequencia

#SetDefault coloca um valor base se não encontrar alguma chave

contatos.setdefault("nome", "John/Jane Doe")
contatos.setdefault("idade", 0)
print(contatos)

#update atualiza a lista com novos valores: 

contatos.update({"Gabriela@gmail.com" : {"nome": "Gabriela", "Telefone": "7777-2221"}})
print(contatos)

#values é o contrário do Keys (ao invés das chaves imprime os valores dentro delas)
valores_dentro = contatos.values()
print(valores_dentro)




