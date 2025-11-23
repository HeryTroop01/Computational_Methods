def gauss_seidel(a, b, x, iters):
    n = len(a)
    
    for k in range(iters):
        for i in range(n):
            s1 = sum(a[i][j] * x[j] for j in range(i))          # old + new values
            s2 = sum(a[i][j] * x[j] for j in range(i + 1, n))   # old values only
            
            x[i] = (b[i] - s1 - s2) / a[i][i]
    
    return x

# Input
a = [
     [3, 5, 6],
     [5, 7, 8],
     [5, 6, 7]
]
b = [4, 7, 8]
x = [0, 0, 0]

iters = 8
output = gauss_seidel(a, b, x, iters)
print(output)
