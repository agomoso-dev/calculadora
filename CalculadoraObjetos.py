## Calculadora AVANZADA
## Autor: Antonio Gómez Osorio
## Github: agomoso-dev
## Fecha: 2025-09-18
## Descripción: Calculadora avanzada usando programación orientada a objetos
## Versión: 1.0
import re
import readline  
import os
class Calculadora:
    def __init__(self):
        self.resultado = 0
        
    def suma(self, num1, num2):
        return num1 + num2
    
    def resta(self, num1, num2):
        return num1 - num2
    
    def multiplicacion(self, num1, num2):
        return num1 * num2
    
    def division_entera(self, num1, num2):
        if num2 == 0:
            raise ValueError("No se puede dividir por cero")
        return num1 // num2
    
    def division_real(self, num1, num2):
        if num2 == 0:
            raise ValueError("No se puede dividir por cero")
        return num1 / num2
    
    def potencia(self, num1, num2):
        return num1 ** num2
    
    def modulo(self, num1, num2):
        if num2 == 0:
            raise ValueError("No se puede calcular módulo con cero")
        return num1 % num2
    
    def redondear(self, num):
        return round(num)
    
    def mostrar_opciones(self):
        opciones = """
        Calculadora:
        ------------
        +  : Suma
        -  : Resta
        x : Multiplicación
        \// : División Entera
        /  : División Real
        ^  : Potencia
        %  : Módulo
        r  : Redondear
        () : Parentesis
        C  : Limpiar pantalla
        ayuda: /ayuda
        salir: /salir
        ------------
        """
        print(opciones)
    
    def identificar_operacion(self, operacion, num1, num2):
        # Mapea las operaciones a sus funciones 
        operadores = {
            '+': self.suma,
            '-': self.resta,
            'x': self.multiplicacion,
            '//': self.division_entera,
            '/': self.division_real,
            '^': self.potencia,
            '%': self.modulo,
            'r': self.redondear
        }
        
        if operacion in operadores:
            if operacion == 'r':
                return operadores[operacion](num1)
            return operadores[operacion](num1, num2)
        else:
            raise ValueError("Operación no reconocida")
        
    def comprobar_prioridad(self, tokens):
        # Verificar operaciones prioritarias
        tiene_mult = 'x' in tokens
        tiene_div_entera = '//' in tokens
        tiene_div_real = '/' in tokens
        
        idx_mult = 0
        idx_div_entera = 0
        idx_div_real = 0
        
        # print(f"Tiene multiplicación: {tiene_mult}, División entera: {tiene_div_entera}, División real: {tiene_div_real}")
        
        if tiene_mult or tiene_div_entera or tiene_div_real:
            # print("div/multi detectada")
            if tiene_mult:
                idx_mult = tokens.index('x')
            if tiene_div_entera:
                idx_div_entera = tokens.index('//')
            if tiene_div_real:
                idx_div_real = tokens.index('/')
                
            # Encontrar el operador con menor índice (primera operación)
            indices = []
            if tiene_mult:
                indices.append(('mult', idx_mult))
            if tiene_div_entera:
                indices.append(('div_entera', idx_div_entera))
            if tiene_div_real:
                indices.append(('div_real', idx_div_real))

            if indices:
                primera_op = min(indices, key=lambda x: x[1])
                
                if primera_op[0] == 'mult':
                    # print("Multiplicación primero")
                    resultado = float(tokens[idx_mult - 1])
                elif primera_op[0] == 'div_entera':
                    # print("División entera primero")
                    resultado = float(tokens[idx_div_entera - 1])
                else:
                    print("División real primero")
                    resultado = float(tokens[idx_div_real - 1])
            else:
                resultado = float(tokens[0])
        else:
            resultado = float(tokens[0])
            
        return resultado
    
    def procesar_expresion(self, tokens):
        i = 1
        while i < len(tokens)-1:
            # Verificamos si es un operador válido
            if tokens[i] in ['x', '/', '//', '+', '-', '^', '%', 'r']:
                try:
                    # Convierte los operandos a números
                    num1 = float(tokens[i-1])
                    operador = tokens[i]
                    num2 = float(tokens[i+1])
                    # Realiza la operación y reemplaza los 3 tokens con el resultado
                    resultado = self.identificar_operacion(operador, num1, num2)
                    tokens[i-1:i+2] = [str(resultado)]
                    # Vuelve al inicio para buscar más operaciones
                    i = 1
                except ValueError:
                    raise ValueError(f"No se puede convertir '{tokens[i-1]}' o '{tokens[i+1]}' a número")
                except IndexError:
                    raise ValueError("Expresión incompleta o mal formada")
            else:
                i += 2

        # Validar que quede un número válido
        try:
            if len(tokens) == 1:
                return float(tokens[0])
            else:
                raise ValueError("Expresión mal formada")
        except ValueError:
            raise ValueError(f"No se puede procesar '{tokens[0]}'")
    
    def ejecutar(self):

        print("Bienvenido a la calculadora \n /// by Antonio /// \n /help para ayuda ")
        self.mostrar_opciones()
        
        while True:
            try:
                print("\n--Cálculo--")
                readline.set_startup_hook(lambda: readline.insert_text(str(self.resultado)))
                entrada = input("- ").lower()
                readline.set_startup_hook() 
                
                if entrada == "/salir":
                    print("Gracias por usar la calculadora")
                    break
                elif entrada == "c":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("\n /ayuda (muestra opciones) \n")
                    self.resultado = 0
                    continue
                elif entrada == "/ayuda":
                    self.mostrar_opciones()
                    continue
                elif not entrada: 
                    continue
                    
                # Extrae números, operadores, paréntesis y comandos
                tokens = re.findall(r'[\d.]+|//|[-+/^%r=()]|x|c', entrada)
                
                # Comprobación de paréntesis
                if tokens.count('(') != tokens.count(')'):
                    raise ValueError("Paréntesis no balanceados")
                    
                # Procesa paréntesis de adentro hacia afuera
                while '(' in tokens:
                    # Encuentra el paréntesis más interno
                    ultimo_abre = len(tokens) - 1 - tokens[::-1].index('(')
                    # print(f"Encuentro el parentesis en la posicion {ultimo_abre}")
                    siguiente_cierra = tokens[ultimo_abre:].index(')') + ultimo_abre
                    # print(f"Encuentro el cierre en la posicion {siguiente_cierra}")
                    # Extrae y procesa la expresión dentro de los paréntesis
                    expresion_interna = tokens[ultimo_abre + 1:siguiente_cierra]
                    resultado_parentesis = self.procesar_expresion(expresion_interna)
                    # print(f"Resultado del parenteis: {resultado_parentesis}")
                    # Reemplaza la expresión entre paréntesis con su resultado
                    tokens[ultimo_abre:siguiente_cierra + 1] = [str(resultado_parentesis)]
                
                # Procesa la expresión resultante
                if len(tokens) >= 1:
                    self.resultado = self.procesar_expresion(tokens)
                    print(f"Resultado: {self.resultado}")
                    
            except (ValueError, IndexError) as e:
                print(f"Error: {str(e)}")
                print("Intente de nuevo")
                
if __name__ == "__main__":
    calc = Calculadora()
    calc.ejecutar()