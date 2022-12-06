def concat_string(lista):
  caracter = ""
  for i in lista: 
    caracter += str(i)
  return caracter
  
  
  
listado = ["hola", "como", "estas", "todo", "bien"]
print(concat_string(listado))