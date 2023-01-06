"""
Programa que calcula la distancia, velocidad y el tiempo

Autor:
Alexander Mejía

Versión:
VER 1.0
"""

def menu():
    """
    Función que alberga el menú de opciones
    Parametros:
    -----------
        No tiene parametros
    Retorno:
    -----------
        Retorna el valor de la opción
    """
    # impresión del menú
    print("--------------TRANSFORMACIONES--------------")
    print("1. Velocidad")
    print("2. Distancia")
    print("3. Tiempo")
    print("4. Salir")
    # variable que alberga la opción que decide el usuario
    op = int(input("Ingrese la opción que desea: "))
    # mientras la variable op salga del rango del menú
    while op > 4 or op < 1:
        # vuelve a pedir el valor de la opción
        op = int(input("La opción escogida no se encuentra en el menú...Ingrese la opción que desea: "))
    #retorna la opción
    return op

def velocidad():
    """
    Función que alberga la solución para la velocidad
    Parametros:
    -----------
        No tiene parametros
    Retorno:
    -----------
        No tiene retorno
    """
    print("Velocidad")
    # d alberga al valor de distancia
    d = float(input("Ingrese la distancia: "))
    # t alberga al valor del tiempo
    t = float(input("Ingrese el tiempo: "))
    # v albera la operacion de la velocidad
    v = d/t
    #imprime la variable v
    print("Velocidad = ", v)

def distancia():
    """
    Función que alberga la solución para la distancia
    Parametros:
    -----------
        No tiene parametros
    Retorno:
    -----------
        No tiene retorno
    """
    print("Distancia")
    # v alberga al valor de la velocidad
    v = float(input("Ingrese la velocidad: "))
    # t alberga al valor del tiempo
    t = float(input("Ingrese el tiempo: "))
    # d albera la operacion de la distancia
    d = v*t
    #imprime la variable d
    print("Distancia: ", d)

def tiempo():
    """
    Función que alberga la solución para el tiempo
    Parametros:
    -----------
        No tiene parametros
    Retorno:
    -----------
        No tiene retorno
    """
    print("Tiempo")
    # d alberga al valor de la distancia
    d = float(input("Ingrese la distancia: "))
    # v alberga al valor de la velocidad
    v = float(input("Ingrese la velocidad: "))
    # t albera la operacion del tiempo
    t = d/v
    #imprime la variable t
    print("Tiempo: ", t)

if __name__ == '__main__':
    op = menu()

    #si op es igual a 1
    if op == 1:
        # variable v llama a la función velocidad()
        v = velocidad()
    #si op es igual a 2
    if op == 2:
        # variable d llama a la función distancia()
        d = distancia()
    #si op es igual a 3
    if op == 3:
        # variable t llama a la función tiempo()
        t = tiempo()
    #si op es igual a 4
    if op == 4:
        # imprime mensaje
        print("Saliste!!!")