def cadastro(): 
  nome = input("Digite o nome: ")
  idade = int(input("Digite a idade: "))
  telefone = input("Qual o número de celular? ")
  email = input("Digite o e-mail: ")

  print(f'Seu nome é: {nome}\nIdade: {idade} anos\nTelefone: {telefone}\nE-mail: {email}')

cadastro()