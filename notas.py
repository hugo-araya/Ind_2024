nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
examen = float(input('Examen: '))
trabajo = float(input('Trabajo: '))
promedio = (nota1 + nota2 + nota3)/3
final = promedio * 0.55 + examen * 0.3 + trabajo * 0.15
print('Nota final: ', final)
