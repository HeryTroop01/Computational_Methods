# Data points
x = [1, 2, 3, 4]
y = [2, 3, 5, 4]

n = len(x)

# Summations
sum_x = sum(x)
sum_y = sum(y)
sum_x2 = sum(i * i for i in x)
sum_xy = sum(x[i] * y[i] for i in range(n))

# Regression coefficients
b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
a = (sum_y - b * sum_x) / n

# Output
print("a =", a)
print("b =", b)
