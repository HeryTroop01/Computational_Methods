def f(x, y):
    return x + y

def rk(x0, y0, h, steps):
    x = x0
    y = y0

    for i in range(steps):
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)

        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        x = x + h

        print(f"Step {i+1}: x = {x}, y = {y}")

    return y

# Initial conditions
x0 = 0
y0 = 1
h = 0.1
steps = 1

rk(x0, y0, h, steps)
