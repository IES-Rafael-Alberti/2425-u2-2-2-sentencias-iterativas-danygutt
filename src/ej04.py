'''Ejercicio 2.2.4¶
Escribir un programa que pida al usuario un número entero positivo y 
muestre por pantalla la cuenta atrás desde ese número hasta cero separados 
por comas.'''
# Entrada
def pedirNumeroEnteroPositivo()->int:
    '''Pide un número entero y positivo, y comprueba que sea un número positivo'''
    numero = None
    while numero is None:
        try:
            numero = int(input('Introduce un número positivo: '))
            if numero <= 0:
                print('Solo números positivos, por favor.')
                numero = None
        except:
            print('Solo números positivos, por favor.')
    return numero

# Procesamiento
def generarCuentaAtras(numero:int)->str:
    '''Genera una cadena con la cuenta atrás desde el número dado hasta cero'''
    cuenta_atras = ""
    for i in range(numero, -1, -1):
        cuenta_atras += str(i) + ", "
    return cuenta_atras
# Salida
def mostrarCuentaAtras(cuenta_atras:str)->str:
    '''Muestra la cuenta atrás'''
    print(cuenta_atras)

# Programa principal
def main():

    # Entrada
    numero = pedirNumeroEnteroPositivo()
    # Procesamiento
    cuenta_atras = generarCuentaAtras(numero)
    # Salida
    mostrarCuentaAtras(cuenta_atras)
    

if __name__ == '__main__':
    main()