"""
Este problema plantea el cálculo del sueldo segun la cantidad de horas trabajadas y el coste que cobra por hora

Autor:
Alexander Mejia

Version:
VER 1.0
"""
def menu():
    """
    Esta función nos muestra un menú de 3 opciones las cuales están enlazadas con el cálculo de sueldo
    Parametros
    ----------
        No tiene parametros de entrada
    Retorna
    ----------
        Retorna el valor de la opción
    """
    #Impresion del MENU
    print("--------------MENU--------------")
    print("1. Diario")
    print("2. Mensual")
    print("3. Salir")
    #imput que recibe la opcion que desea elegir
    opcion = int(input("Ingrese el número de la opción: "))
    #validacion del imput, si sale del rango de opciones 
    while opcion > 3 or opcion < 1:
        #vuelve a pedir que se ingrese el valor de la opción
        opcion = int(input("Opcion NO Valida...Ingrese el número de la opción: "))
    #retorna opcion
    return opcion

def op1():
    """
    La funcion va direccionada a la opcion 1 donde selecciona la operacion del cálculo diario.
    Este cálculo se realiza según la variable costo y num 
    Parametros
    ----------
        No tiene parametros de entrada
    Retorna
    ----------
        Retorna el valor de la variable total
    """
    #imprime en pantalla
    print("---------------OPCION 1---------------")
    #input que almacena el numero de horas trabajadas
    num = float(input("Ingrese el número de horas trabajadas: "))
    #input que almacena el costo por hora
    costo = float(input("Costo de hora: $"))
    #total alberga dentro la operacion
    total = num * costo
    #retorna total
    return total

def op2():
    """
    La funcion va direccionada a la opcion 2 donde selecciona la operacion del cálculo mensual.
    Este cálculo se realiza según la variable costo y num multiplicado para los días que se trabajaron
    Parametros
    ----------
        No tiene parametros de entrada
    Retorna
    ----------
        Retorna el valor de la variable total
    """
    #imprime en pantalla
    print("---------------OPCION 2---------------")
    #input que almacena el numero de horas trabajadas
    num = float(input("Ingrese el número de horas trabajadas: "))
    #input que almacena el costo por hora
    costo = float(input("Costo de hora: $"))
    #input que almacena la cantidad de días trabajados
    dias = float(input("Cantidad de días trabajados: "))
    #total alberga la operacion
    total = (num * costo) * dias
    #retorna variable total
    return total

if __name__ == "__main__":
    #variable opcion llama a la función menu()
    opcion = menu()
    #si opcion es igual a 1
    if opcion == 1:
        #total es igual a función op1()
        total = op1()
        #imprimimos el total
        print("El total diario es: $", total)
    #si opcion es igual a 2
    elif opcion == 2:
        #total es igual a op2()
        total = op2()
        #imprimimos el total
        print("El total mensual es: $", total)
    #si opcion es igual a 3
    elif opcion == 3:
        #impresion
        print("---------------OPCION 3---------------")
        print("GRACIAS POR USARNOS")


