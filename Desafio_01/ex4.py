def converteMedidas():
  medida = float(input("Digite o valor que quer converter: "))
  convertendoEmMetros = medida / 100

  print(f"{medida} cm são iguais a {convertendoEmMetros} metros")

converteMedidas()