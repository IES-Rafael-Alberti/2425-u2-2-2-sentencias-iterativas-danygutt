'''
Ejercicio 2.2.1

Escribir un programa que pida al usuario una palabra y la muestre por pantalla 
10 veces.
'''
#entrada
def pideUnaPalabra():
    '''Esta funcion le pide la palabra al usuario con un input de tipo str'''
    palabra = None
    while palabra is None or palabra.strip() == "":
        palabra = input('Deme una palabra para imprimirla: ')
        if palabra.strip() == "":
            print('Esta cadena está vacía. Por favor, introduzca una palabra.')
    return palabra
#proceso
def recibePalabraMultiplicaPorDiez(palabra):
    ''' esta devuelve una lista con las 10 palabras'''
    return [palabra]*10  

#salida
def salida(listaDePalabras):
    '''y esta imprime la lista de las 10 mismas palabras'''
    for palabra in listaDePalabras:
        print(palabra)

# Programa principal
def main():

    #entrada
    palabra = pideUnaPalabra()
    #procesamiento
    listaDePalabras = recibePalabraMultiplicaPorDiez(palabra)
    #salida
    salida(listaDePalabras)

if __name__ == '__main__':
    main()