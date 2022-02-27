from cmath import sin


def main():
    opcions = {
        1 : "area",
        2 : "perimetro"
    }
    opcion = input("""
        1 = area
        2 = perimetro
        """)

    if opcion == "area":
        pass
    
    if opcion == "perimetro":

        def perimeter_triangle(e1, e2, e3):
            p = e1 + e2 + e3
            return p

        def find_edges(e1, angle1, angle2):
            angle3 = 180 - (angle1 + angle2)
            e2 = (e1 * float(str(sin(angle2))[2:20])) / float(str(sin(angle1))[2:20])
            e3 = (e1 * float(str(sin(angle3))[2:20])) / float(str(sin(angle1))[2:20])
            return e2, e3

        datos = input("""
        1 = todos los lados
        2 = un lado, su angulo opuesto y otro angulo

        """)

        if datos == "1":
            e1 = float(input("Longitud del lado 1: "))
            e2 = float(input("Longitud del lado 2: "))
            e3 = float(input("Longitud del lado 3: "))

            p = perimeter_triangle(e1, e2, e3)
            print(f"Perimetro = {p}")

        if datos == "2":
            e1 = float(input("Lado 1: "))
            angle1 = float(input("Angulo opuesto: "))
            angle2 = float(input("Angulo 2: "))
            output = find_edges(e1, angle1, angle2)
            e2 = output[0]
            e3 = output[1]
            p = perimeter_triangle(e1, e2, e3)
            print(f"Perimetro = {p}")



if __name__ == "__main__":
    main()