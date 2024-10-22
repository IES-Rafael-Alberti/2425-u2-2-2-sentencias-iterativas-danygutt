'''Ejercicio 2.2.10¶
Escribir un programa que pida al usuario un número entero 
y muestre por pantalla si es un número primo o no.'''
def solicitarNumero():
    '''Solicita al usuario que introduzca un número entero.'''
    numero=False
    while numero==False:
        try:
            numero = int(input('Introduce un número entero: '))
            return numero
        except ValueError:
            numero = False
            print('Entrada no válida. Por favor, introduce un número entero.')

def esPrimo(numero):
    '''Determina si un número es primo.'''
    if numero in (2, 3, 5, 7):
        return True

    # Comprobar que num sea mayor que 1
    if numero <= 1:
        return False

    # Dividir num por los números del 2 al 9
    for i in range(2, 10):
        if numero % i == 0:  # Si es divisible por i
            return False 

def mostrarResultado(numero, primo):
    '''Muestra el resultado al usuario.'''
    if primo:
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")

def main():
    # Entrada
    numero = solicitarNumero()
    
    # Procesamiento
    primo = esPrimo(numero)
    
    # Salida
    mostrarResultado(numero, primo)

if __name__ == '__main__':
    main()