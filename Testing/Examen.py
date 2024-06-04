def debug_exercise(a=2):
    b = 5
    if a:
        b += a
        print(f"{a + b}")
    if a == b:
        b *= a
        print(f"{a * b}")
    if a == "5":
        b *= a
        print(f"{a * b}")
    if b % 2 != 0:
        b *= a
        print(f"{a / b}")
    else:
        b += a
        print(f"{a / b}")
    print(a + b)

debug_exercise(5)


