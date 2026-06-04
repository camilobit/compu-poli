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


#funcion usando el try, pero investigando es mejor usar un ciclo y dentro de ese ciclo colocar el try paa el manejo de errores

# def calcular_area():
#     print("--- Calculadora de Área de Rectángulos ---")
#     try:
#         # 1. Captura de datos
#         b = float(input("Introduce la base: "))
#         h = float(input("Introduce la altura: "))
        
#         # 2. Validación y Cálculo
#         if b > 0 and h > 0:
#             area = (b * h)
            
#             # 3. Mostrar dibujo (DENTRO del if para que use b y h)
#                         # --- Visualización del Rectángulo ---
#             print("\n--- Visualización ---")
#             print(f"   {'_' * 15}")           # Techo del rectángulo
#             print(f"  |               |")
#             print(f"  |               |  Altura: {h}")
#             print(f"  |               |")
#             print(f"  |_______________|")       # Base del rectángulo
#             print(f"     Base: {b}")

            
#             # 4. Mostrar resultado final
#             print(f"\nResultado: El área es {area:.2f}")
#         else:
#             print("Error: Las medidas deben ser positivas.")
            
#     except ValueError:
#         print("Error: Por favor, introduce solo valores numéricos.")

# # Llamamos a la función para ejecutar todo
# calcular_area()


# def calcular_area():
    
#     print("--- Calculadora de Área de Rectángulos ---")

#     while True:
#         try:
#             # obtener dtos del usuario
#             b = float(input("Introduce la base: "))
#             h = float(input("Introduce la altura: "))

#             # Validación
#             if b <= 0 or h <= 0:
#                 print("Error: Las medidas deben ser positivas.\n")
#                 continue

#             # Cálculo
#             area = b * h

#             # Visualización
#             print("\n--- Visualización ---")
            
#             print(f"   _______________")
#             print(f"  |               |")
#             print(f"  |               |  Altura: {h}")
#             print(f"  |               |")
#             print(f"  |_______________|")
#             print(f"     Base: {b}")

#             # Resultado
#             print(f"\nResultado: El área es {area:.2f}")

#             # Salir del bucle si todo salió bien
#             break

#         except ValueError:
#             print("Error: Debes ingresar solo números.\n")


# # Ejecutar función
# calcular_area()























# una prueba para crear las funciones de la mecanica de fluidos "FÍSICA".
# MECÁNICA DE FLUIDOS







# funcion para la densidad.
# -----------------------------------
# FUNCIONES
# -----------------------------------

def densidad():
    try:
        masa = float(input("Introduce la masa (kg): "))
        volumen = float(input("Introduce el volumen (m³): "))

        if volumen <= 0 or masa <= 0:
            print("Error: Ingrese valores válidos.")
            return

        resultado = masa / volumen

        print(f"\nLa densidad es: {resultado:.2f} kg/m³")

    except ValueError:
        print("Error: Por favor, introduce solo valores numéricos.")


# -----------------------------------

def peso():
    try:
        masa = float(input("Introduce la masa (kg): "))

        if masa <= 0:
            print("Error: Ingrese un valor válido.")
            return

        gravedad = 9.81
        resultado = masa * gravedad

        print(f"\nEl peso es: {resultado:.2f} N")

    except ValueError:
        print("Error: Por favor, introduce solo valores numéricos.")


# -----------------------------------

def peso_especifico():
    try:
        masa = float(input("Introduce la masa (kg): "))
        volumen = float(input("Introduce el volumen (m³): "))

        if volumen <= 0 or masa <= 0:
            print("Error: Ingrese valores válidos.")
            return

        resultado = (masa / volumen) * 9.81

        print(f"\nEl peso específico es: {resultado:.2f} N/m³")

    except ValueError:
        print("Error: Por favor, introduce solo valores numéricos.")


# -----------------------------------

def funcion_bernoulli():
    try:
        presion1 = float(input("Introduce la presión en el punto 1 (Pa): "))
        velocidad1 = float(input("Introduce la velocidad en el punto 1 (m/s): "))
        altura1 = float(input("Introduce la altura en el punto 1 (m): "))

        presion2 = float(input("Introduce la presión en el punto 2 (Pa): "))
        velocidad2 = float(input("Introduce la velocidad en el punto 2 (m/s): "))
        altura2 = float(input("Introduce la altura en el punto 2 (m): "))

        resultado = (
            presion1 + 0.5 * 1000 * velocidad1**2 + 1000 * 9.81 * altura1
        ) - (
            presion2 + 0.5 * 1000 * velocidad2**2 + 1000 * 9.81 * altura2
        )

        print(f"\nEl resultado de Bernoulli es: {resultado:.2f} J")

    except ValueError:
        print("Error: Por favor, introduce solo valores numéricos.")


# -----------------------------------

def funcion_bernoulli_presion():
    try:
        presion1 = float(input("Introduce la presión en el punto 1 (Pa): "))
        velocidad1 = float(input("Introduce la velocidad en el punto 1 (m/s): "))
        altura1 = float(input("Introduce la altura en el punto 1 (m): "))

        velocidad2 = float(input("Introduce la velocidad en el punto 2 (m/s): "))
        altura2 = float(input("Introduce la altura en el punto 2 (m): "))

        resultado = (
            presion1
            + 0.5 * 1000 * velocidad1**2
            + 1000 * 9.81 * altura1
            - (
                0.5 * 1000 * velocidad2**2
                + 1000 * 9.81 * altura2
            )
        )

        print(f"\nLa presión en el punto 2 es: {resultado:.2f} Pa")

    except ValueError:
        print("Error: Por favor, introduce solo valores numéricos.")


# -----------------------------------
# MENÚ PRINCIPAL
# -----------------------------------

while True:

    print("\n==============================")
    print("     CALCULADORA FÍSICA")
    print("==============================")
    print("1. Calcular densidad")
    print("2. Calcular peso")
    print("3. Calcular peso específico")
    print("4. Ecuación de Bernoulli")
    print("5. Calcular presión con Bernoulli")
    print("6. Salir")

    opcion = input("\nSeleccione una opción: ")

    # OPCIONES

    if opcion == "1":
        densidad()

    elif opcion == "2":
        peso()

    elif opcion == "3":
        peso_especifico()

    elif opcion == "4":
        funcion_bernoulli()

    elif opcion == "5":
        funcion_bernoulli_presion()

    elif opcion == "6":
        print("\nPrograma finalizado.")
        break

    else:
        print("\nOpción inválida. Intente nuevamente.")