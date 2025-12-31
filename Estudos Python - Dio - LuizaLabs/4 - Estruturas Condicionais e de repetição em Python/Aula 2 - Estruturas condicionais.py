MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Informe a sua idade:"))
if idade >= MAIOR_IDADE:
	print ("Maior de idade, pode tirar a CNH")
elif idade >= IDADE_ESPECIAL:
	print ("Pode fazer aulas teóricas, mas não pode fazer aulas praticas")
else:
	print ("Menor de idade, não pode tirar a CNH")

#if aninhado
conta_normal = True
saldo =  2000
saque =  2500
cheque_especial =450
conta_universitaria = False

if conta_normal:
	if saldo >= saque:
		print("Saque realizado com sucesso")
	elif saldo <= (saldo + cheque_especial): 
		print("Saque realizado com uso de cheque especial")
	else:
		print("Saldo insuficiente!")
elif conta_universitaria:
	if saldo >= saque:
		print ("Saque realizaado com sucesso!")
	else:
		print("Saldo insuficiente!")