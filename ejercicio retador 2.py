municipios = []
habitantes = []
total_habitantes = 0
for i in range(3):
  municipio = input("Ingresa el nombre del municipio: ")
  municipios.append(municipio)
  habitante = input("Ingresa el numero de habitantes: ")
  habitantes.append(habitante)
  total_habitantes += int(habitante)


print("El total de habitantes es: " +str(total_habitantes))

promedio_habitantes = total_habitantes/3
print("El promedio de habitantes es: "+ str(promedio_habitantes))

