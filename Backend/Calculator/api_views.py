from django.http import JsonResponse
from rest_framework.decorators import api_view
from .CalculadoraDjango import Calculadora

calculadora = Calculadora()

@api_view(['POST'])
def calcular(request):
    try:
        expresion = request.data.get('expresion', '')
        
        # Solo permitir números, operadores, paréntesis y espacios
        import re
        if not re.match(r"^[0-9+\-*/().\s^%x]+$", expresion.replace('//', '')):
            raise ValueError("Expresión inválida o contiene caracteres no permitidos.")
        
        # Reemplazar 'x' por '*' y '^' por '**' para que Python los entienda
        expresion_eval = expresion.replace('x', '*').replace('^', '**')

        # Evaluar la expresión de forma segura
        resultado = eval(expresion_eval, {"__builtins__": {}}, {})

        return JsonResponse({
            'resultado': resultado,
            'error': None
        })
    except Exception as e:
        return JsonResponse({
            'resultado': None,
            'error': str(e)
        }, status=400)

@api_view(['GET'])
def opciones(request):
    return JsonResponse({
        'operadores': [
            {'simbolo': '+', 'descripcion': 'Suma'},
            {'simbolo': '-', 'descripcion': 'Resta'},
            {'simbolo': 'x', 'descripcion': 'Multiplicación'},
            {'simbolo': '//', 'descripcion': 'División Entera'},
            {'simbolo': '/', 'descripcion': 'División Real'},
            {'simbolo': '^', 'descripcion': 'Potencia'},
            {'simbolo': '%', 'descripcion': 'Módulo'},
            {'simbolo': 'r', 'descripcion': 'Redondear'},
        ]
    })
