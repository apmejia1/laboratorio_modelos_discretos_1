"""
Programa que pide ingresar su nombre e imprimirlo junto a un saludo

Autor:
Alexander Mejia

Versión:
Ver 1.0
"""
def ingreso():
    """
    Función que pide ingresar el nombre y lo valida comprobando que solo haya letras
    Parametros
    -----------
        No tiene parametros
    Retorno
    -----------
        retorna la variable nombre
    """
    # input que almacena el nombre
    nombre = input("¿Cómo te llamas?: ")
    # mientras el nombre no se conforme de solo letras
    while nombre.isalpha() == False:
        #vuelve a pedir que el nombre sea ingresado
        nombre = input("Solo aceptamos letras...¿Cómo te llamas?: ")
    # retorna la variable nombre
    return nombre

def imprimir(nombre):
    """
    Esta función se encarga de imprimir el nombre
    Parametros
    -----------
        Recoge la variable nombre como parametro
    Retorno
    -----------
        No tiene retorno
    """
    # imprime el saludo con el nombre
    print("Hola,", nombre)
    
if __name__ == "__main__":
    # variable nombre llama a la función ingreso()
    nombre = ingreso()
    # se llama a la función imprimir() que recoge como parametro la variable nombre
    imprimir(nombre)