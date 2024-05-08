# Autor: Hugo Araya Carrasco - el otro
# Fecha: 10 / 04 / 2024
# Esto calcula una liquidacion

afecto = int(input('Monto afecto : $'))
salud = 7 / 100
afp = 12 / 100
leyes = afecto * salud + afecto * afp
liquido = afecto - leyes
print('Liquido:$',liquido)

             