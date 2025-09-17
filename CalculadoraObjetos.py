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
        C  : Limpiar pantalla
        =  : Mostrar resultado
        salir: Salir
        ------------
        """
        print(opciones)
    
    def identificar_operacion(self, operacion, num1, num2):
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
        elif operacion.lower() == 'c':
            print("\n" * 100)
            return self.resultado
        else:
            raise ValueError("Operación no reconocida")

    def ejecutar(self):
        import re
        
        print("Bienvenido a la calculadora")
        self.mostrar_opciones()
        
        while True:
            try:
                print("Cálculo:")
                entrada = input(":").lower()
                
                if entrada == "salir":
                    print("Gracias por usar la calculadora")
                    break
                    
                # Extrae números y operadores
                tokens = re.findall(r'[\d.]+|//|[-+/^%r=()]|x|c|salir', entrada)
                print(f"Tokens encontrados: {tokens}")


                        
                if len(tokens) >= 3:
                    # Verificar operaciones prioritarias
                    tiene_mult = 'x' in tokens
                    tiene_div = '//' in tokens
                    
                    idx_mult = 0
                    idx_div = 0

                    
                    print(f"Tiene multiplicación: {tiene_mult}, Tiene división entera: {tiene_div}")
                    if tiene_mult or tiene_div:
                        print("Multiplicación o división entera detectada")
                        print("Comienza el cálculo con multiplicación o división")
                        if tiene_mult:
                            idx_mult = tokens.index('x')
                        if tiene_div:
                            idx_div = tokens.index('//')
                        if idx_mult > idx_div:
                            print("División entera primero")
                            resultado = float(tokens[idx_div - 1])
                        elif idx_div > idx_mult:
                            print("Multiplicación primero")
                            resultado = float(tokens[idx_mult - 1])
                        else:
                            resultado = float(tokens[0])
                    # Inicializamos con el primer número
                    resultado = float(tokens[0])
                    
                    # Procesamos los operadores y números en pares
                    for i in range(1, len(tokens)-1, 2):
                        operador = tokens[i]
                        try:
                            num2 = float(tokens[i+1])
                            resultado = self.identificar_operacion(operador, resultado, num2)
                        except ValueError as e:
                            print(f"Error en la operación: {e}")
                            break
                
                    self.resultado = resultado
                    print(f"Resultado: {self.resultado}")
                    
            except (ValueError, IndexError) as e:
                print(f"Error: {str(e)}")
                print("Intente de nuevo")
                
if __name__ == "__main__":
    calc = Calculadora()
    calc.ejecutar()