from cmath import sin


def main():
    opcions = {
        "1" : "area",
        "2" : "perimetro"
    }
    opcion = opcions[input("""
        1 = area
        2 = perimetro

        """)]

    if opcion == "area":

        def area_triangle_edges(e1, e2, e3):
            s = (e1 + e2 + e3) / 2
            h = (2 / e1) * ((s * (s - e1) * (s - e2) * (s - e3)) ** 0.5)
            a = (e1 * h) / 2
            return a


        def find_edges(e1, angle1, angle2):
            angle3 = 180 - (angle1 + angle2)
            e2 = (e1 * float(str(sin(angle2))[2:20])) / float(str(sin(angle1))[2:20])
            e3 = (e1 * float(str(sin(angle3))[2:20])) / float(str(sin(angle1))[2:20])
            return e2, e3

        def area_triangle(e1, h):
            a = e1 * h / 2
            return a


        datos = input("""
        1 = todos los lados
        2 = un lado, su angulo opuesto y otro angulo
        3 = base y altura

        """)

        if datos == "1":
            e1 = float(input("Longitud del lado 1: "))
            e2 = float(input("Longitud del lado 2: "))
            e3 = float(input("Longitud del lado 3: "))

            a = area_triangle_edges(e1, e2, e3)
            print(f"Area = {a}")

        elif datos == "2":
            e1 = float(input("Lado 1: "))
            angle1 = float(input("Angulo opuesto: "))
            angle2 = float(input("Angulo 2: "))
            output = find_edges(e1, angle1, angle2)
            e2 = output[0]
            e3 = output[1]
            a = area_triangle_edges(e1, e2, e3)
            print(f"Area = {a}")

        else:
            e1 = float(input("Base: "))
            h = float(input("Altura: "))
            a = area_triangle(e1, h)
            print(f"Area = {a}")

    
    if opcion == "perimetro":
        pass



if __name__ == "__main__":
    main()