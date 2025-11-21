from FiguraGeometrica import FiguraGeometrica
from Triangulo import Triangulo
from Circulo import Circulo
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from Cilindro import Cilindro
from Paralelogramo import Paralelogramo
from Rombo import Rombo
def mostrar_menu():
    while True:
        print("Elige la figura a calcular:")
        print("1. Calcular area de un Triangulo")
        print("2. Calcular area de un Circulo")
        print("3. Calcular area de un Cuadrado")
        print("4. Calcular area de un Rectangulo")
        print("5. Calcular area de un Cilindro") 
        print("6. Calcular area de un Paralelogramo")
        print("7. Calcular area de un Rombo")
        print("8. Calcular area de un Trapecio")
        print("9. Salir del menu")

        opcion = input("Digite el numero de su eleccion: ")
        
        if opcion == "1":
           try:
              base = float(input("Base de un Triangulo: "))
              altura = float(input("Altura de un Triangulo: "))
              mi_Triangulo = Triangulo("Triangulo") # Creacion del objeto
              area = mi_Triangulo.area_triangulo(base, altura)
              print(f"Area: {area: .2f}")
           except:
              print("Opción no válida, seleccione un valor válido") 

        elif opcion == "2":
           try:
              radio = float(input("Radio de un Circulo: "))
              mi_circulo = Circulo("Circulo")
              area = mi_circulo.area_circulo(radio)
              print(f"Area: {area: .2f}")
           except:
              print("Opción no válida, seleccione un valor válido") 
        
        elif opcion == "3":
           try:
              base = float(input("Base de un Cuadrado: "))
              altura = float(input("Altura de un Cuadrado: "))
              mi_cuadrado = Cuadrado("Cuadrado")
              area = mi_cuadrado.area_cuadrado(base, altura)
              print(f"Area: {area: .2f}")
           except:
              print("Opción no válida, seleccione un valor válido") 
        
        elif opcion == "4":
           try:
              base = float(input("Base de un Rectangulo: "))
              altura = float(input("Altura de un Rectangulo: "))
              mi_rectangulo = Rectangulo("Rectangulo")
              area = mi_rectangulo.area_ractangulo(base, altura)
              print(f"Area: {area: .2f}")
           except:
              print("Opción no válida, seleccione un valor válido") 
        
        elif opcion == "5":
           try:
              radio = float(input("Radio de un Cilindro: "))
              altura = float(input("Altura de un Cilindro: "))
              mi_Cilindro = Cilindro("Cilindro")

              mi_Cilindro.radio = radio
              mi_Cilindro.altura = altura

              area = mi_Cilindro.area_cilindro()
              print(f"Area: {area: .2f}")
           except:
              print("Opción no válida, seleccione un valor válido")
        
        elif opcion == "6":
           try:
              base = float(input("Base de un Paralelogramo: "))
              altura = float(input("Altura de un Paralelogramo: "))
              mi_paralelogramo = Paralelogramo("Paralelogramo")
              area = mi_paralelogramo.area_paralelogramo(base, altura)
              print(f"Area: {area: .2f}")
           except:
              print("Opción no válida, seleccione un valor válido")

        elif opcion == "7":
             try:
                D = float(input("Diagonal mayor del Rombo: "))
                d = float(input("Diagonal menor del Rombo: "))
                from Rombo import Rombo
                mi_Rombo = Rombo("Rombo")
                area = mi_Rombo.area_rombo(D, d)
                print(f"Area: {area: .2f}")
             except:
               print("Opción no válida, seleccione un valor válido")

        elif opcion == "8":
             try:
                base_mayor = float(input("Base mayor del Trapecio:"))
                base_menor = float(input("Base menor del Trapecio:"))
                altura = float(input("Altura de un Trapecio"))
                from Trapecio import Trapecio
                mi_Trapecio = Trapecio("Trapecio")
                area = mi_Trapecio.area_trapecio(base_mayor, base_menor, altura)
                print(f"Area: {area: .2f}")
             except:
                print("Opción no válida, seleccione un valor válido")
              
        elif opcion == "9":
           print("Gracias por usar el menu")
           break # Termina el bucle y sale del programa

        else:
           print("Opción no válida. Por favor, digite una opción del 1 al 7.")

if __name__ == "__main__":
    mostrar_menu()