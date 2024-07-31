def cadastroProduto(): 
  nomeProduto = input("Nome do produto: ")
  codigo = int(input("Codigo do produto: "))
  quantidade = int(input("Qual a quantidade? "))
  preco = float(input("Digite o valor unitário: "))
  valorTotalProduto = quantidade * preco

  print(f'Produto: {nomeProduto}\nCódigo: {codigo} anos\nQuantidade: {quantidade}\nPreco: {preco}\nValor total do produto: {valorTotalProduto}')

cadastroProduto()