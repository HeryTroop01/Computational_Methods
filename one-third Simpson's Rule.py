def f(x):
    return x**2


def simpson(a, b, n):
    h = (b - a) / n
    x = a
    s = f(a) + f(b)

    if n % 2 == 0:
        for i in range(1, n):
            x = a + i*h
            if i % 2 == 0:
                s += 2 * f(x)
            else:
                s += 4 * f(x)
        return (h/3) * s

    elif n % 3 == 0:
        for i in range(1, n):
            x = a + i*h
            if i % 3 == 0:
                s += 2 * f(x)
            else:
                s += 3 * f(x)
        return (3*h/8) * s

    else:
        return None


a = 0
b = 4
n = 4    

answer = simpson(a, b, n)
print(answer)
