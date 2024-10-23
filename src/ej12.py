'''Ejercicio 2.2.12
Escribir un programa en el que se pregunte al usuario por una frase y una letra,
y muestre por pantalla el número de veces que aparece la letra en la frase.'''

#Entrada
def pedirFraseYLetra():
    frase = str(input('Ingrese una frase: '))
    letra = str(input('Ingresa una letra: '))
    return frase, letra

#Proceso
def contarLetrasEnFrase(frase,letra):
    return frase.count(letra)

#Salida
def salida(letra,contador):
    print(f'La letra "{letra}" aparece {contador} veces en la frase.')

#Primer Programa    
def main():
    # Entrada
    frase, letra = pedirFraseYLetra()
    
    # Proceso
    contador = contarLetrasEnFrase(frase, letra)
    
    # Salida
    salida(letra, contador)

if __name__ == '__main__':
    main()