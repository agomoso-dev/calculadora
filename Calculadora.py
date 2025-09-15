## Calculadora INICIAL
## Autor: Antonio Gómez Osorio
## Fecha: 2025-09-15
## Descripción: Calculadora básica con funciones para cada operación
## Versión: 1.0
import re

''' Definición de funciones para cada operación matemática '''
def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def divisionEntera(num1, num2):
    return num1 // num2

def divisionReal(num1, num2):
    return num1 / num2

def potencia(num1, num2):
    return num1 ** num2

def modulo(num1, num2):
    return num1 % num2

def redondear(num):
    return round(num)

# Muestra las opciones disponibles
def Opciones(calculo):
    print("Calculadora:")
    print("------------")
    print("+")
    print("-")
    print("*")
    print("//")
    print("/")
    print("^")
    print("%")
    print("r")
    print("C")
    print("=")
    print("salir")
    print("------------")
    
# Identifica la operación a realizar
def identificarOperacion(operacion, num1,num2):
    if operacion.find("+")==1:  # SUMA 
        return suma(num1,num2)
    elif operacion.find("-")==1:    # RESTA
        return resta(num1,num2)
    elif operacion.find("*")==1:    # MULTIPLICACIÓN
        return multiplicacion(num1,num2)
    elif operacion.find("//")==1:   # DIVISIÓN ENTERA
        return divisionEntera(num1,num2)
    elif operacion.find("/")==1:    # DIVISIÓN REAL
        return divisionReal(num1,num2)
    elif operacion.find("^")==1:    # POTENCIA
        return potencia(num1,num2)
    elif operacion.find("%")==1:    # MÓDULO
        return modulo(num1,num2)
    elif operacion.find("r")==1:    # REDONDEAR
        return redondear(num1)
    elif operacion.find("c")==1:    # LIMPIAR PANTALLA
        print("\n" * 100)
        print("Calculo:")
        operacion= input(":").lower()
        return identificarOperacion(operacion,num1,num2)
    else:
        print("Operación no reconocida")
        exit()


def salir(operacion):
    print(operacion.index("salir"))
    
    # Si el usuario escribe "salir", salir del programa
    if operacion[0]=="salir" or operacion.index("salir"):
        print("Dijiste salir pues salimos...")
        

'''
-----------------------------------------
-           CALCULADORA BÁSICA          -
-----------------------------------------
'''
while True:
    print("Bienvenido a la calculadora")

    print("Calculo:")

    operacion= input(":").lower()

    # Extrae números y operadores de la entrada del usuario
    operacion= re.findall(r'[\d.]+|[-+*/^%r=()]|//|c|salir', operacion)
    print(operacion)
    if salir(operacion):
        break
    


