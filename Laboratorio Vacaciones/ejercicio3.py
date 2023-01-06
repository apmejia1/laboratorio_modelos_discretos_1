"""
Este programa está destinado a calcular el teorema de pitagoras
Autor:
Alexander Mejia

Versión:
VER 1.0
"""

#importamos la librería math
import math

def validar():
    """
    Función que valida si el triangulo a calcular es un triangulo - rectangulo
    Parametros
    --------------
        No recibe parametros
    Retorna
    --------------
        Retorna la variable q la cual almacena el nómero de opción
    """

    #impresion del menu
    print("----------------MENU----------------")
    print("El triangulo a calcular es de tipo triangulo-rectangulo")
    print("1. Si")
    print("2. No")
    #input que almacena que numero de opcion quiere el usuario
    q = int(input("Ingrese el numero de opcion: "))
    #mientras q este fuera del rango volverpa a pedir la variable q
    while q > 2 or q < 1:
        q = int(input("Opcion NO Valida...Ingrese el número de la opción: "))
    #retorna variable q
    return q

def ingreso():
    """
    Esta función tiene la finalidad de pedir un valor y hacer la operacion de potencia al cuadrado
    Parametros
    --------------
        No recibe parametros
    Retorna
    --------------
        Retorna la variable a_op
    """
    #input que almacena el valor del primer cateto
    a = int(input("Ingrese el valor del primer cateto: "))
    #variable que almacena la operacion de potencia
    a_op = a**2
    #retorna la variable a_op
    return a_op

def operacion(a,b):
    """
    Esta función realiza la operacion de la raiz cuadrada debido a la simplificación de la operacion
    Parametros
    --------------
        Recibe como parametros las variables a y b
    Retorna
    --------------
        Retorna la variable c

    """
    # variable que almacena la operacion
    c = math.sqrt(a+b)
    # retorna c
    return c


if __name__ == '__main__':
    # variable q que llama a la funcion validar()
    q = validar()
    # si q es igual a 1
    if q == 1:
        # a llama a la función ingreso()
        a = ingreso()
        # b llama a la función ingreso()
        b = ingreso()
        # c llamara a la función operacion la cual tiene como parametros a y b
        c = operacion(a,b)
        # imprime la variable c
        print(f"El resultado es: {c:.2f}")
    # caso contrario
    else:
        # imprime 
        print("El triangulo debe ser de tipo triangulo-rectangulo")