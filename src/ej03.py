'''
Ejercicio 2.2.3

Escribir un programa que pida al usuario un número entero positivo y muestre
por pantalla todos los números impares desde 1 hasta ese número
separados por comas.
'''
#entrada
def pedirNumeroEnteroPositivo()->int:
    '''pide un numero entero y positivo, y comprueba que sea un numero positivo'''
    numero=None
    while numero is None:
        try:
            numero = int(input('Introduce un numero positivo: '))
            if numero<= 0:
                print('Solo numero positivos porfavor')
                numero = None
        except:
            print('Solo numero positivos porfavor')
    return numero

#proceso
def generarNumerosImpares(numero:int)->int:
    '''crea una lista de los numero impares desde 1 hasta el numero'''
    impares = ""
    for i in range(1, numero + 1, 2):
        impares += str(i) + ", "
    if impares:  
        impares = impares[:-2]
    return impares
    
#salida
def mostrarNumerosImpares(impares:int,numero:int)->str:
    '''muestra los impares hasta ese numero'''
    print(f'Los numeros impares hasta {numero} son: {impares}')
# Programa principal
def main():

    # Entrada
    numero = pedirNumeroEnteroPositivo()
    # Procesamiento
    impares = generarNumerosImpares(numero)
    # Salida
    mostrarNumerosImpares(impares,numero)

if __name__ == '__main__':
    main()