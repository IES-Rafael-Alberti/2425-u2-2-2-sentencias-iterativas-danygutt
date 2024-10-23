'''Ejercicio 2.2.11
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla 
una a una las letras de la palabra introducida empezando por la última.'''
#entrada
def pedirPalabra():
    '''Pide una palabra al usuario'''
    espacios = True
    while espacios:
        palabra = str(input('Introduzca una palabra: '))
        if palabra.strip():
            espacios = False
        else:
            print("Por favor, introduzca una palabra válida (no solo espacios).")
    return palabra
    
def convertirPalabrasEnLista(palabra):
    '''convertimos la palabra en una cadena de caracteres'''
    listaDeCaracteres = list(reversed(palabra))
    return listaDeCaracteres    

def salida(listaDeCaracteres):
    '''imprimimos la cadena de manera inversa'''
    print(' '.join(listaDeCaracteres))

#Programa Principal
def main():
    # Entrada
    palabra = pedirPalabra()
    # Procesamiento
    listaDeCaracteres = convertirPalabrasEnLista(palabra)
    # Salida
    salida(listaDeCaracteres)

if __name__ == '__main__':
    main()