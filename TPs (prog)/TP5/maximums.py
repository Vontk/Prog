def max_of_two(x, y):
    if x > y:
        return x
    elif y > x:
        return y
    else:
        return 0


def max_of_three(x, y, z):
    if x > y > z:
        return x
    elif y > z > x:
        return y
    elif z > x > y:
        return z
    else:
        return 0
