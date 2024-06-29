def check_vowels():
    name = input("Ingresar nombre para detectar vocales: ")
    a = "a" in name.lower()
    e = "e" in name.lower()
    i = "i" in name.lower()
    o = "o" in name.lower()
    u = "u" in name.lower()
    print(f"Contiene a: {a}")
    print(f"Contiene e: {e}")
    print(f"Contiene i: {i}")
    print(f"Contiene o: {o}")
    print(f"Contiene u: {u}")


check_vowels()
