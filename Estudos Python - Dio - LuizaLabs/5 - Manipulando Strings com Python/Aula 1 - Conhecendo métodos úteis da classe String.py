curso = "  cara de pYtHoN  "

#use upper para deixar tudo maiúsculo:
print(curso.upper())
#use lower para deixar tudo minúsculo:
print(curso.lower())
#use itle para deixar somente a primeira letra maiúscula:
print(curso.title())
#para tirar todos os espaços da string, usa-se strip
print(curso.strip())
#para tirar todos os espaços a esquerda da string, usa-se lstrip
print(curso.lstrip())
#para tirar todos os espaços a direita da string, usa-se rstrip
print(curso.rstrip())
#para centralizar e definir o tamanho da string usa-se o center (o numedo define o tamanho da string e o # serão os simbolos usados para preencher os espaçoe em branco no exemplo)
print(curso.center(50, "#"))
#para colocar simbolos ou outros valores entre os valores da string, usa-se o join:
print("_".join(curso))