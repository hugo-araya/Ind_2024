def f(x):
    y = 2 * x + 1
    return y

def saluda():
    print('Hola')

def saluda_bien(nombre):
    print('Hola '+nombre)

def saluda_mejor(nombre):
    return 'Hola '+nombre

valor = f(f(f(4)))
print(valor)
saluda()
saluda_bien('Hugo')
saludo = saluda_mejor('Hugo')
print(saludo)



