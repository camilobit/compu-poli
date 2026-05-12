# def suma (a,b):
#     return a + b

# print(suma(2,3))



# def funcion_suma(a, b):
#     print("La suma es", a + b)

# funcion_suma(3, 5)



# x=2
# y="2"

# if x == y:
#     print("x es igual a y")
# else:
#     print("x no es igual a y")    


# # Capturamos los datos y los convertimos a decimales (float)
# base = float(input("Ingresa la base del triángulo: "))
# altura = float(input("Ingresa la altura del triángulo: "))

# # Realizamos el cálculo
# area = (base * altura) / 2

# # Mostramos el resultado
# print(f"El área del triángulo es: {area}")
def calcular_area():
    print("--- Calculadora de Área de Rectángulos ---")
    try:
        # 1. Captura de datos
        b = float(input("Introduce la base: "))
        h = float(input("Introduce la altura: "))
        
        # 2. Validación y Cálculo
        if b > 0 and h > 0:
            area = (b * h)
            
            # 3. Mostrar dibujo (DENTRO del if para que use b y h)
                        # --- Visualización del Rectángulo ---
            print("\n--- Visualización ---")
            print(f"   {'_' * 15}")           # Techo del rectángulo
            print(f"  |               |")
            print(f"  |               |  Altura: {h}")
            print(f"  |               |")
            print(f"  |_______________|")       # Base del rectángulo
            print(f"     Base: {b}")

            
            # 4. Mostrar resultado final
            print(f"\nResultado: El área es {area:.2f}")
        else:
            print("Error: Las medidas deben ser positivas.")
            
    except ValueError:
        print("Error: Por favor, introduce solo valores numéricos.")

# Llamamos a la función para ejecutar todo
calcular_area()
