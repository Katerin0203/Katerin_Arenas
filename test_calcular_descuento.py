import math

def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Calcular descuento en compras de software")
    print("2. Calcular volumen de una esfera")
    print("3. Salir del programa")

def calcular_descuento(licencias):
    precio_base = 50
    if licencias >= 5:
        return licencias * precio_base * 0.7  # Descuento del 30%
    elif licencias >= 3:
        return licencias * precio_base * 0.8  # Descuento del 20%
    else:
        return licencias * precio_base

def calcular_volumen_esfera(radio):
    return (4 / 3) * math.pi * (radio ** 3)

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1, 2 o 3): ")
        
        if opcion == "1":
            try:
                licencias = int(input("Ingrese el número de licencias a comprar: "))
                if licencias > 0:
                    total = calcular_descuento(licencias)
                    print(f"El costo total con descuento es: ${total:.2f}")
                else:
                    print("El número de licencias debe ser mayor a 0.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        elif opcion == "2":
            try:
                radio = float(input("Ingrese el radio de la esfera: "))
                if radio > 0:
                    volumen = calcular_volumen_esfera(radio)
                    print(f"El volumen de la esfera es: {volumen:.2f}")
                else:
                    print("El radio debe ser mayor a 0.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        elif opcion == "3":
            print("Gracias por usar el programa, nos vemos :). ¡Adiós!")
            break
        
        else:
            print("Opción no válida. Por favor, elija 1, 2 o 3.")

# Ejecución del programa
if __name__ == "__main__":
    main()
