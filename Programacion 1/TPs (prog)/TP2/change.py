# calculates and displays the change on purchase. It prompts the user for the amount spent and the amount given.
# Utilizes basic input/output, data manipulation, and formatting operations.

# noinspection SpellCheckingInspection
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
