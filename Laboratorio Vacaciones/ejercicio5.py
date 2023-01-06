"""
Programa que tiene como objetivo transformar varias unidades de medida

Autor:
Alexander Mejia

Versión:
VER 1.9
"""
def ingreso():
    """
    Esta funion contiene ek input que almacena la opcion del menú
    Parametros
    --------------
        No contiene parametros
    Retorna
    --------------
        Retorna la variable operacion
    """
    #imprime el menú
    print("--------------TRANSFORMACIONES--------------")
    print("1. libras")
    print("2. kilogramos")
    print("3. gramos")
    print("4. Salir")
    # input que almacena la opcion que desea realizar
    operacion = int(input("Ingrese la opción que desea realizar: "))
    # mientras el valor de operacion no esté entre el rango seguirá pidiendo ingresar un valor en opcion
    while operacion > 4 or operacion < 1:
        operacion = int(input("El numero no está disponilbe según el menú...Ingrese la opción que desea realizar: "))
    # retorna operacion
    return operacion

def valor():
    """
    Esta función pide al usuario y valida la cantidad que desea transformar
    Parametros
    --------------
        No recibe parametros
    Retorna
    --------------
        Retorna la variable val
    """
    # input que almacena el valor a transformar
    val = float(input("Ingrese el valor que desea transformar: "))
    #mientras el valor no se encuentre en el rango seguira pidiendo un valor valido
    while val < 0:
        val = float(input("No existen valores negativos...Ingrese el valor que desea transformar: "))
    #retorna val
    return val

def libras():
    """
    Esta función hace la transformación de libras
    Parametros
    --------------
        No recibe parametros
    Retorna
    --------------
        Retorna las variables l_op1,l_op2
    """
    print("---------------Operacion 1---------------")
    # variable l llama a funcion valor()
    l = valor()
    # variable que realiza la operacion de libras a kilogramos
    l_op1 = (l*0.4535)
    # variable que realiza la operacion de libras a gramos
    l_op2 = (l*453.592)
    # retorna las variables
    return l_op1,l_op2

def kilos():
    """
    Esta función hace la transformación de kilogramos
    Parametros
    --------------
        No recibe parametros
    Retorna
    --------------
        Retorna las variables k_op1,k_op2
    """
    print("---------------Operacion 2---------------")
    k = valor()
    #variable que realiza la transformacion de kilogramos a libras
    k_op1 = (k*2.2046)
    #variable que realiza la transformacion de kilogramos a  gramos
    k_op2 = (k*1000)
    #retorna las variables
    return k_op1,k_op2

def gramos():
    """
    Esta función hace la transformación de gramos
    Parametros
    --------------
        No recibe parametros
    Retorna
    --------------
        Retorna las variables g_op1,g_op2
    """
    print("---------------Operacion 2---------------")
    # variable que llama a la funcion valor()
    g = valor()
    #variable que realiza la transformacion de gramos a kilogramos
    g_op1 = (g*0.001)
    #variable que realiza la transformacion de gramos a libras
    g_op2 = (g*0.002204)
    #retorna las variables
    return g_op1,g_op2

if __name__ == "__main__":
    # variable que llama la funcion ingreso()
    operacion = ingreso()
    # si operacion es igual a 1
    if operacion == 1:
        # variables llaman a la funcion libras()
        l_op1,l_op2 = libras()
        #impresion de resultados
        print("--kilogramos: ", l_op1)
        print("--gramos: ", l_op2)
    # si operacion es igual a 2
    elif operacion == 2:
        # variables que llaman a la funcion kilos()
        k_op1,k_op2 = kilos()
        # impresion de resultados
        print("--libras: ", k_op1)
        print("--gramos: ", k_op2)

    # si operacion es igual a 3
    elif operacion == 3:
        # variables que llaman a funcion gramos
        g_op1,g_op2 = gramos()
        # imprimimos los resultados
        print("--kilogramos: ", g_op1)
        print("--gramos: ", g_op2)
    # si operacion es igual a 4
    elif operacion == 4:
        # impresion
        print("Saliendo")