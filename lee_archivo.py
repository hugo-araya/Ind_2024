import matplotlib.pyplot as plt

def leer_datos(archivo):
    ent = open(archivo)
    datos = []
    for linea in ent:
        linea = linea.rstrip('\n')
        datos.append(linea)
    ent.close()
    return datos

def calcula(datos, year):
    casos = []
    suma = 0
    for linea in datos:
        lista = linea.split()
        fecha = lista[0].split('-')
        if fecha[0] == year:
            suma = suma + float(lista[1])
    casos.append(suma)
    return casos

datos = leer_datos('TotalesNacionales.txt')
s2020 = calcula(datos, '2020')
s2021 = calcula(datos, '2021')
s2022 = calcula(datos, '2022')
s2023 = calcula(datos, '2023')
casos = [s2020,s2021,s2022, s2023]
agnos = [2020, 2021, 2022, 2023]
plt.plot(agnos, casos)
plt.show()
