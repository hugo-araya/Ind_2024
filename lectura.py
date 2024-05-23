ar = open('datos.txt')
linea = ar.readline()
while linea != '':
    linea = linea.rstrip('\n')
    lista = linea.split()
    print(lista[0])
    linea = ar.readline()

