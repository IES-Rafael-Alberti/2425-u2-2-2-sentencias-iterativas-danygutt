'''Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

*
**
***
****
*****
'''
def entradaAltura():
    '''Solicita un número entero positivo al usuario.'''
    while True:
        try:
            altura = int(input('Introduce un número entero para la altura del triángulo: '))
            if altura > 0:
                return altura
            else:
                print('Por favor, introduce un número entero positivo.')
        except ValueError:
            print('Entrada no válida. Por favor, introduce un número entero.')

def mostrarTriangulo(altura):
    '''Muestra un triángulo rectángulo de altura especificada.'''
    for i in range(1, altura + 1):
        print('*' * i)

def salidaTriangulo(altura):
    '''Muestra un mensaje indicando que se ha generado el triángulo.'''
    print(f'\nTriángulo rectángulo de altura {altura} generado:\n')

#Programa Principal
def main():
    # Entrada
    altura = entradaAltura()
    
    # Salida inicial
    salidaTriangulo(altura)

    # Procesamiento y Salida
    mostrarTriangulo(altura)

if __name__ == '__main__':
    main()

