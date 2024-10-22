'''Ejercicio 2.2.5
Escribir un programa que pregunte al usuario una cantidad a invertir, 
el interés anual y el número de años, y muestre por pantalla el capital
obtenido en la inversión cada año que dura la inversión.

# Formula para calcular El capital tras un año.
amount *= 1 + interest / 100
# En donde:
# - amount: Cantidad a invertir
# - interest: Interes porcentual anual 
'''
def datosDeInversion():
    '''Pregunta cuánto quiere invertir y se asegura de que sea un float.'''
    inversion = None
    while inversion is None:
        try:
            inversion = float(input('Cantidad a invertir: '))
            if inversion <= 0:
                print('Solo números positivos, por favor.')
                inversion = None
        except ValueError:
            print('Solo números positivos, por favor.')
    
    interesAnual = None
    while interesAnual is None:
        try:
            interesAnual = float(input('Interés anual (en %): '))
            if interesAnual <= 0:
                print('Solo números positivos, por favor.')
                interesAnual = None
        except ValueError:
            print('Solo números positivos, por favor.')

    añosDeInversion = None            
    while añosDeInversion is None:
        try:
            añosDeInversion = int(input('Número de años: '))
            if añosDeInversion <= 0:
                print('Solo números positivos, por favor.')
                añosDeInversion = None
        except ValueError:
            print('Solo números positivos, por favor.')

    return inversion, interesAnual, añosDeInversion

def calculoDeInversion(inversion, interesAnual, añosDeInversion):
    '''Calcula el capital obtenido cada año.'''
    capital = []
    amount = inversion
    for año in range(1, añosDeInversion + 1):
        amount *= (1 + interesAnual / 100)
        capital.append((año, amount))
    return capital

def salidaDeLaInversion(capital):
    '''Muestra el capital obtenido cada año.'''
    print("\nCapital obtenido cada año:")
    for año, amount in capital:
        print(f"Año {año}: {amount:.2f}")

def main():
    # Entrada
    inversion, interesAnual, añosDeInversion = datosDeInversion()
    
    # Procesamiento
    capital = calculoDeInversion(inversion, interesAnual, añosDeInversion)
    
    # Salida
    salidaDeLaInversion(capital)

if __name__ == '__main__':
    main()
