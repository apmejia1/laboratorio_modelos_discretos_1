"""
Este programa orienta su funcionamiento a la resolución de una 
operación básica como lo es un número elevado a un exponente.

Autor:
Alexander Mejia

Versión:
VER 1.0
"""
def ingreso():
    """
    Esta función recoge los datos de la base y el exponente
    Parametros
    -----------
        No trecoge ningún parametro
    Retorno
    -----------
        Retorna las variables base y expo
    """
    # input para almacenar la base que ingresa el usuario
    base = int(input("Ingrese la base: "))
    # input para almacenar el exponente que ingresa el usuario
    expo = int(input("Ingrese el exponente: "))
    # retorno de variables base y expo
    return base, expo

def operacion(base, expo):
    """
    Función que se encarga de realizar la operacion de exponentes
    Parametros
    -----------
        Parametros base y expo
    Retorno
    -----------
        Retorna res que es la variable que almacena la operación de exponente
    """
    # variable que aloja el resultado de el exponente
    res = base ** expo
    # imprime la variable res
    print("La respuesta es", res)
 
if __name__ == "__main__":
    # variables base y expo llaman a la función ingreso()
    base, expo = ingreso()
    # variable res que llama a la función operacion con base y expo como parametros
    res = operacion(base, expo)
