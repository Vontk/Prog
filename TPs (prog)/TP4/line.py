def line():
    ca = float(input("Ingrese el coeficiente A"))
    cb = float(input("Ingrese el coeficiente B"))
    x1 = float(input("Ingrese el punto X1"))
    x2 = float(input("Ingrese el punto X2"))
    import math
    y1 = (x1 * ca + cb)
    y2 = (x2 * ca + cb)
    diferencia_y = y2 - y1
    diferencia_x = x2 - x1
    distancia = math.sqrt(diferencia_x ** 2 + diferencia_y ** 2)
    print(f"El coeficiente A de su ecuación de la recta es: {ca}")
    print(f"El coeficiente B de su ecuación de la recta es: {cb}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {x1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {x2}")
    print("")
    print("Para la siguiente ecuación:")
    print(f"	Y = {ca}X + {cb}")
    print("")
    print("Dados los siguientes puntos:")
    print(f"	P1 ({x1}, {y1})")
    print(f"	P2 ({x2}, {y2})")
    print("")
    print(f"La distancia entre ellos es:{distancia}")
