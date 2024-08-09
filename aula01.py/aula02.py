# Faça um programa onde lê a idade de um usuário e verifica se ele tem convite e se pode entrar.
#criar as variaveis: idade e tem_convite 

idade = int(input("Digite sua idade: "))
tem_convite = True  #booleano

if idade >= 18:
  if tem_convite:
    print("O usuário pode entrar")
  else:
    print("O usuário precisa de convite para entrar")
else:
  print("Não pode entrar. É menor de idade.")


