def check_vowels():
    nombre = input("Ingresar nombre para detectar vocales: ")
    a = "a" in nombre.lower()
    e = "e" in nombre.lower()
    i = "i" in nombre.lower()
    o = "o" in nombre.lower()
    u = "u" in nombre.lower()
    print(f"Contiene a: {a}")
    print(f"Contiene e: {e}")
    print(f"Contiene i: {i}")
    print(f"Contiene o: {o}")
    print(f"Contiene u: {u}")


check_vowels()
