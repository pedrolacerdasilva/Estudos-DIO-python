#tupla é uma lista que se torna imutável
tupla = ("p", "y", "t", "h", "o", "n",)

print(tupla[2:])  # ("t", "h", "o", "n")
print(tupla[:2])  # ("p", "y")
print(tupla[1:3])  # ("y", "t")
print(tupla[0:3:2])  # ("p", "t")
print(tupla[::])  # ("p", "y", "t", "h", "o", "n")
print(tupla[::-1])  # ("n", "o", "h", "t", "y", "p")

#erro quando se tenta alterar uma tupla

tup_teste = (1, 3)
print(tup_teste)
tup_teste[0] = 2 #aqui ocorre o erro pois tenta-se trocar o valor imutável 1 por 2

#enumerar e iterar seguem as mesmas regras das listas