def f(x, y):
    return x + y

def euler(x0, y0, h, steps):
    x = x0
    y = y0

    for i in range(steps):
        y = y + h * f(x, y)
        x = x + h
        print(f"Step {i+1}: x = {x}, y = {y}")

    return y

# Initial conditions
x0 = 0
y0 = 1
h = 0.1
steps = 5

euler(x0, y0, h, steps)
