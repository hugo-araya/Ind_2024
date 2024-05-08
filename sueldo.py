nombre = input('Nombre: ')
sueldo_base = int(input('Sueldo base: '))
venta1 = int(input("Venta 1: "))
venta2 = int(input("Venta 2: "))
venta3 = int(input("Venta 3: "))
porcentaje = float(input('Porcentaje: '))
total_venta = venta1 + venta2 + venta3
comision = total_venta * (porcentaje / 100)
sueldo_recibir = sueldo_base + comision
print ('El nombre del empleado es: ', nombre)
print ('Comision: ', comision)
print ('Sueldo a recibir: ', sueldo_recibir)
print ('Con un porcentaje de : ', porcentaje)