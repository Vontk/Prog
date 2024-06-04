def change():
    expense = float(input("Tu Gasto, recomendado 23.75"))
    money = float(input("Tu Dinero, recomendado 100"))
    vuelto = money - expense
    pesos = int(vuelto)
    centavos = (int((vuelto - pesos) * 100))
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print("")
    print("Vuelto")
    print("")
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)


change()
