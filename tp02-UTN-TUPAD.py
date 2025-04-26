'''
# tecnicatura universitaria en programacion UTN
# MATEMATICA I
#Práctico 2: Trabajo integrador matematica1-programacion1
#Alumnos

GRUPO 2
ALUMNOS: Bruno Pighin, Jazmin Herrera, Aldo Manfredi, Alan Jofre, Florencia Mauna

## EJERCICIO_ 
4. Generador de Tabla de Verdad:

Cree un programa que genere la tabla de verdad para una expresión booleana
sencilla, como "A AND B".
Extensión: Permitan al usuario elegir entre distintas operaciones lógicas.


REFERENCIA https://youtu.be/8c23ZnFM8d4?si=0oheD2r6Ix2b5ZIK
'''

booleanos = [True, False]

def tabla_or():
    # Esta función se encarga de realizar la Tabla "Or".
    # Devuelve Falso si ambos son Falsos.
    print("TABLA DE VERDAD CON OR")
    print('P\tQ\tP o Q')
    for x in booleanos:
        for y in booleanos:
            print(f'{x}\t{y}\t{x or y}') # Iteraciones: 1ra: True True // 2da: True False // 3er: False True // 4ta: False False


def tabla_and():
    # Esta función se encarga de realizar la Tabla "And".
    # Devuelve Verdadero si ambos son Verdaderos.
    print("\nTABLA DE VERDAD CON AND")
    print('P\tQ\tP y Q')
    for x in booleanos:
        for y in booleanos:
            print(f'{x}\t{y}\t{x and y}') # Iteriaciones: 1ra: True True // 2da: True False // 3er: False True // 4ta: False False


def tabla_not():
    # Esta función se encarga de realizar la Tabla "Not".
    # Devuelve el valor opuesto al ingresado.
    print("TABLA DE VERDAD CON NOT")
    print('P\tNO P')
    for x in booleanos:
        print(f'{x}\t{not x}') # Iteraciones: 1ra: True // 2da: False

def inicio():

  # Esta función genera la tabla de verdad de las distintas funciones lógicas.
    print("GENERADOR DE TABLA DE VERDAD ")
    print("1 - Tabla de verdad de OR")
    print("2 - Tabla de verdad de AND")
    print("3 - Tabla de verdad de NOT")
    print("0 - Salir")

  # Se le solicita al usuario que ingrese un número de las opciones.
  # El ciclo se repite mientras se ingresen valores válidos.
    while True:
        inp = input("Ingrese la opción que desea: ")
        if inp == "0":
            break
        if inp == "1":
            tabla_or()
        elif inp == "2":
            tabla_and()
        elif inp == "3":
            tabla_not()
        else:
            print("Entrada invalida .. escriba una opcion correcta.. !!") # Si se ingresa un valor inválido, devuelve este mensaje.
            #pass

inicio()
