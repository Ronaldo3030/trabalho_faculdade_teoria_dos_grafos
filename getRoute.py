def getRoute():
  print("-----------------------------------------------------------")
  getRoute = input("Informe o caminho do arquivo: ")
  print("-----------------------------------------------------------")
  if(getRoute):
    return getRoute
  else:
    print("-----------------------------------------------------------")
    print("Caminho invalido, tente novamente!")
    print("-----------------------------------------------------------")
    getRoute()