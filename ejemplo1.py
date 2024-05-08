monto_bruto = int(input('Ingrese monto bruto: '))
tasa_interes = 12.5
monto_interes = monto_bruto * tasa_interes / 100
tasa_bonificacion = 5.0
importe_bonificacion = monto_bruto * tasa_bonificacion / 100
monto_neto = (monto_bruto - importe_bonificacion) + monto_interes
print('El monto neto es:',monto_neto)
