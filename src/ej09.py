'''Ejercicio 2.2.9¶
Escribir un programa que almacene la cadena de caracteres contraseña
en una variable, pregunte al usuario por la contraseña hasta que 
introduzca la contraseña correcta.'''
def obtenerContraseñaCorrecta():
    '''Devuelve la contraseña correcta.'''
    return "contraseña" 

def solicitarContraseña():
    '''Solicita al usuario que introduzca la contraseña.'''
    return input('Introduce la contraseña: ')

def verificarContraseña(contraseñaCorrecta):
    '''Verifica si la contraseña introducida es correcta.'''
    contraseñaUsuario = solicitarContraseña()
    while contraseñaUsuario != contraseñaCorrecta:
        print("Contraseña incorrecta. Inténtalo de nuevo.")
        contraseñaUsuario = solicitarContraseña()
def salida():
    print('La contraseña es correcta')

def main():
    # Almacenar la contraseña correcta
    contraseñaCorrecta = obtenerContraseñaCorrecta()
    # Verificar la contraseña
    verificarContraseña(contraseñaCorrecta)
    #salida
    salida()

if __name__ == '__main__':
    main()
