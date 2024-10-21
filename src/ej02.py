'''
Ejercicio 2.2.2

Escribir un programa que pregunte al usuario su edad y muestre por 
pantalla todos los años que ha cumplido (desde 1 hasta su edad).
'''
#entrada
def pideLaEdad()-> int:
    '''
la función pregunta la edad y comprueba que sea un numero int
    '''
    edad = None
    while edad is None :
        try:
            edad = int(input('¿Cuantos años tienes? '))
            
        except:
            print('Introduza solo numero')
    return edad

#proceso
def edadDeUnoAEdad(edad:int)->int:
    '''
una funcin que cuente desde el 1 hasta
    '''
    return list(range(1,edad+1))
    
#salida
def imprimeLosAñosQueHaCumplido(listaEdad:int)->str:
    print(f'Los años que ha cumplido son: {", ".join(str(año) for año in listaEdad)}')

# Programa principal
def main():

    #entrada
    edad=pideLaEdad()
    #procesamiento
    edad = edadDeUnoAEdad(edad)
    #salida
    imprimeLosAñosQueHaCumplido(edad)

if __name__ == '__main__':
    main()