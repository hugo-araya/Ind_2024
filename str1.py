cadena = "Hola Mundo"
largo = len(cadena)
i = 0
ok = False
letra = 'm'
while i < 10:
    if cadena[i] == letra:
        ok = True
    i = i + 1
if ok == True:
    print('La letra <' + letra+ '> ' + 'Si esta')
else:
    print('La letra <' + letra + '> ' + 'No esta')   
