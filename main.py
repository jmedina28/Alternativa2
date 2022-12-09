from lanzador import lanzar

def main():
    while True:
        try:
            n = int(input("Introduzca el número del ejercicio: "))
            lanzar(n)
            break
        except ValueError:
            print("Introduzca un número entero")

if __name__ == "__main__":
    main()