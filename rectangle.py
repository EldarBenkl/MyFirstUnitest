def area(a, b):
    if a < 0 or b < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    return a * b
