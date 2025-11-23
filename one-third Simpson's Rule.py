def f(x):
    return x**2

def simpson(a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)

    # Simpson 1/3 rule (n must be even)
    if n % 2 == 0:
        for i in range(1, n):
            x = a + i*h
            if i % 2 == 0:
                s += 2 * f(x)
            else:
                s += 4 * f(x)
        return (h / 3) * s

    # Simpson 3/8 rule (n must be divisible by 3)
    elif n % 3 == 0:
        for i in range(1, n):
            x = a + i*h
            if i % 3 == 0:
                s += 2 * f(x)
            else:
                s += 3 * f(x)
        return (3 * h / 8) * s

    else:
        return None   # invalid n value for Simpson's rules

# Inputs
a = 0
b = 4
n = 4

answer = simpson(a, b, n)
print(answer)
