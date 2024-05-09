n = int(input('N: '))
suma = 0
i = 1
while i <= n:
    potencia = 1
    j = 1
    while j <= i:
        potencia = potencia * i
        j = j + 1
    suma = suma + potencia
    i = i + 1
print('Suma: ', suma)
