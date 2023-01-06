"""
Este programa halla la raíz enesima de cualquier número

Autor:
Alexander Mejia

Versión:
VER 1.0
"""
def ingreso():
    """
    Función que recoge los datos de la base y el radical
    Parametros:
    -----------
        No tiene parametros de entrada
    Retorno:
    -----------
        Retorna la base y radical
    """
    # input que recoge el valor de la variable base
    base = int(input("Ingrese la base de la operación: "))
    # input que recoge el valor de la variable radi
    radi = int(input("Ingrese el radical de la operación: "))
    #retorna base y radi
    return base, radi

def operacion(base, radi):
    """
    Esta función tiene dentro el algoritmo de la raíz
    Parametros:
    -----------
        Recoge como parametros las variables base y radi
    Retorno:
    -----------
        Retorna la variable res
    """
    # variable que alberga la operacion de la raiz
    res = base**(1/radi)
    # imprime la respuesta en pantalla
    print("La razi es: ", res)
if __name__ == '__main__':
    # base y radi llaman a la función ingreso()
    base, radi = ingreso()
    # variable res que llama a la función operacion()
    res = operacion(base, radi)

