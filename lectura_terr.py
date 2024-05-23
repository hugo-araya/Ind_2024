ar = open('terr.txt')
cont = 0
mes_buscado = '05'
linea = ar.readline()
while linea != '':
    linea = linea.rstrip('\n')
    lista = linea.split()
    fecha = lista[0]
    fecha1 = fecha.split('/')
    dia = fecha1[0]
    mes = fecha1[1]
    agno = fecha1[2]
    if mes == mes_buscado:
        cont = cont + 1
    linea = ar.readline()
print('Cantidad de terremotos en el mes',mes_buscado,': ',cont)






