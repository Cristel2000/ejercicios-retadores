numero_cajas = input("Número de cajas a vender: ")
id_producto = input("Id del producto: ")

if int(id_producto) == 1:
  producto = "Maiz grano"
  precio = 258.55
elif int(id_producto) == 2:
  producto = "Pepino"
  precio = 334.72
elif int(id_producto) == 3:
  producto = "Tomate verde"
  precio = 129.00
else:
  mensaje = "Id no valido"
  print(mensaje)
  

if int(numero_cajas) <= 100:
  costo_total = int(numero_cajas) * precio + 1500
else:
  print("No se puede realizar la venta")



print("El producto es: "+producto)
print("El precio por caja es: "+str(precio))
print("El costo toal a pagar: "+str(costo_total))