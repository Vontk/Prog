def roots(a, b, c):
    sqrt = (b**2 - 4*a*c)**0.5
    r1 = (-b + sqrt)/(2*a)
    r2 = (-b - sqrt)/(2*a)
    if "j" in str(r1) or "j" in str(r2):
        return "( )"
    if r1 == r2:
        return f'({r1})'
    else:
        return f"({r1}, {r2})"


def value_y(a, b, c, x):
    y = a * x ** 2 + b * x + c
    return y


def to_string(a, b, c):
    if a != 0 and b == 0:
        return f"f(x) = {a} * X^2 + {c}"
    if a == 0 and b != 0:
        return f"f(x) = {b} * X + {c}"
    if a == 0 and b == 0:
        return f"f(x) = {c}"
    return f"f(x) = {a} * X^2 + {b} * X + {c}"


def derivation(a, b, c):
    if a != 0 and b != 0:
        return f"f'(x) = {2*a} * X + {b}"
    elif a != 0 and b == 0:
        return f"f'(x) = {2*a} * X"
    elif a == 0 and b != 0:
        return f"f'(x) = {b}"
    else:
        return f"f'(x) = 0"
