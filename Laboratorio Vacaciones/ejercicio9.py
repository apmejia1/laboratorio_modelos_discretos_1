"""
Programa que pide la base y la altura de un triangulo y calcula su área

Autor:
Alexander Mejia

Versión:
VER 1.0
"""
def ingreso():
    """
    Función que contiene los ingresos de datos de la base y de la altura
    Parametros:
    -----------
        No tiene parametros
    Retorno:
    -----------
        Retorna las variables b y h
    """
    # variable b almacena la base del triangulo ingresada por el usuario
    b = float(input("Ingrese la base del triangulo: "))
    # variable h almacena la altura del triangulo ingresada por el usuario
    h = float(input("Ingrese la altura del triangulo: "))
    # retorna b y h
    return b, h

def area(b, h):
    """
    Esta funcion tiene dentro la operación del área de un triangulo}
    Parametros:
    -----------
        Toma como parametros b y h
    Retorno:
    -----------
        Retorna el resultado de la operacion
    """
    # variable area contiene el resultado de cálculo del área de un triangulo
    area = (b*h)/2
    # retorna la variable area
    return area

if __name__ == '__main__':
    # b y h llaman a la función ingreso
    b, h = ingreso()
    # area llama a la función area() con parametros b y h
    area = area(b, h)
    #imprime lo que contiene la variable area
    print("El área es ", area)
