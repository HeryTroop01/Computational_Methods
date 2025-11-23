

def gauss_siedel(a, b, x, iters):
    n = len(a)
    
    for k in range(iters):
        for i in range(n):
            s1 = 0
            s2 = 0
            
            for j in range(i):
                s1 += a[i][j] * x[j]
            for j in range(i):
                s2 += a[i][j] * x[j] 
                
            x[i] = (b[i] - s1 - s2)/a[i][i]
    return x       

a = [
     [3,5,6],
     [5, 7,8],
     [5,6,7]] 
b= [4,7,8]
x= [0,0,0]

iters = 8
output = gauss_siedel(a, b, x, iters)       
print(output)               
                
