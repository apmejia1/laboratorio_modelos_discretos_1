"""
Este programa realiza una operación de fracción donde el numerador está elevado al exponente y el numerador es un número normal

Autor:
Alexander Mejia

Versión: 
VER 1.0
"""
def ingreso():
    """
    Esta función contiene dentro la petición de que el usario ingrese los valor de las variables:
    - x para el numerador
    - z para el exponente del numerador
    - den para el denominador
    Parametros
    --------------
        No tiene parametros
    Retorna
    --------------
        Retorna las variables x, z, den
    """
    #input para almacenar el numerador
    x = int(input("Ingrese el númerador: "))
    #input para almacenar el exponente del numerador
    z = int(input("Ingrese el exponente del númerador: "))
    #input para almacenar el denominador
    den = int(input("Ingrese el denominador: "))
    #retorna x, z, den
    return x,z,den

def operator(x,z,den):
    """
    Esta función contiene dentro de si la operacion
    Parametros
    --------------
        Recibe como parametros x, z, den
    Retorna
    --------------
        Retorna la variable y
    """
    #y contiene la operación
    y = (x**z)/den
    #retorna la variable y
    return y

if __name__ == "__main__":
    #x, z, den contienen la función ingreso()
    x,z,den = ingreso()
    #y llama a la función operator con x, z, den como parametros
    y = operator(x,z,den)
    #imprime la variable y
    print("El resultado es: y = ", y)