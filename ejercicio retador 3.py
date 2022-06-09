cemento =input("Numero de costales de cemento (kg): ")
yeso = input("Numero de costales de yeso(kg): ")

total_cemento = int(cemento) * 40
total_yeso = int(yeso)*30
peso_total = (total_cemento)+(total_yeso)

print("El peso total en kg es: "+str(peso_total))

if peso_total>1624 and peso_total <3254:
  resultado = True;
  print("¿Se puede realizar el envio?: " +str(resultado))
else:
  resultado = False
  print("¿Se puede realizar el envio?: " + str(resultado))