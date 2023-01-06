"""
Este programa tine la finalidad de calcular el area de un circulo partindo de un radio dado por el usuario

Autor:
Alexander Mejia

Versión:
VER 1.0
"""
#importacion de la librería math
import math

def ingreso():
    """
    La función ingreo se encarga de retornar el valor del radio el cual debe ser ingresado por el usuario
    Parametros
    ----------
        No recibe parametros
    Retorno
    ----------
        Retorna la variable r la cual es un input
    """
    #input que almacena el radio del circulo
    r = float(input("Ingrése el radio de su circulo: "))
    #mientras r sea menor a 0
    while r < 0:
        #pide nuevamente el radio
        r = float(input("El número ingresado no es válido...Ingrése el radio de su circulo: "))
    #retorna variable r
    return r

def operacion(r):
    """
    Esta función hace la operacion de el radio
    Parametros
    ----------
        Recibe la variable r como prametro
    Retorno
    ----------
        retorna la variable area que almacena el resultado de la operación
    """
    #area es igual a PI por r al cuadrado
    area = math.pi * (r**2)
    #retorna la variable area
    return area

if __name__ == "__main__":
    #variable r llama a función ingreso()
    r = ingreso()
    #variable area llama a función operacion() con parametro r
    area = operacion(r)
    #Imprimimos el area
    print("El área del circulo con radio ",r,f" es: {area:.2f}")