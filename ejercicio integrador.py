
total_cajas = input("Número de cajas a vender: ")
id_producto = input("ID del producto: ")
venta_productos = [[2, 122], [1, 89], [1, 22], [3, 48], [1, 75],[3, 322],[2, 95],[1, 148],[1, 83],[3, 100]]



if int(id_producto) == 1:
  producto = "Maiz Grano"
  precio_caja = 285.55
elif int(id_producto) == 2:
  producto = "Pepino"
  precio_caja = 334.72
elif int(id_producto) == 3:
  producto = "Tomate verde"
  precio_caja = 129.00

total_ventas_dia = 0
for i in venta_productos:
  total_ventas_dia =  total_ventas_dia + i[1]
total_ventas = int(total_ventas_dia) + int(total_cajas)

total_final = 0
if total_ventas < 1500:
  if int(total_cajas) <= 100:
     tota_pagar = float(precio_caja) * float(total_cajas) + 1500 
     descuento = "False"
else:
  tota_pagar = float(precio_caja) * float(total_cajas) 
  descuento = "true"
  total = tota_pagar * .20
  tota_pagar = tota_pagar - total

print("El producto es: " + producto)
print("El precio por caja es: " + str(precio_caja))
print("Aplica descuento del 20%: " + descuento)
print("El costo total a pagar es: " + str(tota_pagar))
