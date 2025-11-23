# ------------------------------------------------------
# Q1. Check if a number is a palindrome
# ------------------------------------------------------
def check_palindrome(num):
    return num == int(str(num)[::-1])

print("Q1 Palindrome Check:", check_palindrome(121))


# ------------------------------------------------------
# Q2. Sum of first n natural numbers
# ------------------------------------------------------
def sum_natural(n):
    s = 0
    for i in range(1, n+1):
        s += i
    return s

print("Q2 Sum of first n numbers:", sum_natural(10))


# ------------------------------------------------------
# Q3. Check prime number
# ------------------------------------------------------
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print("Q3 Prime Check:", is_prime(17))


# ------------------------------------------------------
# Q4. Find GCD of two numbers
# ------------------------------------------------------
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print("Q4 GCD:", gcd(30, 45))


# ------------------------------------------------------
# Q5. Roots of quadratic equation
# ------------------------------------------------------
import math

def quadratic_roots(a, b, c):
    D = b*b - 4*a*c
    if D > 0:
        r1 = (-b + math.sqrt(D)) / (2*a)
        r2 = (-b - math.sqrt(D)) / (2*a)
        return ("Real & Distinct", r1, r2)
    elif D == 0:
        r = -b / (2*a)
        return ("Real & Equal", r)
    else:
        real = -b / (2*a)
        imag = math.sqrt(-D) / (2*a)
        return ("Complex", real, imag)

print("Q5 Quadratic Roots:", quadratic_roots(1, 4, 4))


# ------------------------------------------------------
# Q6. Sum of all even numbers from 1 to n
# ------------------------------------------------------
def sum_even(n):
    s = 0
    for i in range(2, n+1, 2):
        s += i
    return s

print("Q6 Sum of even numbers:", sum_even(10))


# ------------------------------------------------------
# Q7. Reverse digits of a number
# ------------------------------------------------------
def reverse_number(num):
    rev = 0
    while num > 0:
        rev = rev*10 + num % 10
        num //= 10
    return rev

print("Q7 Reverse Number:", reverse_number(12345))


# ------------------------------------------------------
# Q8. Count how many times a function is called (global variable)
# ------------------------------------------------------
count = 0

def counter_function():
    global count
    count += 1

for _ in range(5):
    counter_function()

print("Q8 Function Call Count:", count)


# ------------------------------------------------------
# Q9. Function modifies a global variable
# ------------------------------------------------------
x = 10

def change_global():
    global x
    x = 20

print("Q9 Before change:", x)
change_global()
print("Q9 After change:", x)


# ------------------------------------------------------
# Q10. Find smallest number in a list
# ------------------------------------------------------
def smallest(lst):
    small = lst[0]
    for num in lst:
        if num < small:
            small = num
    return small

print("Q10 Smallest Element:", smallest([4, 9, 2, 7]))


# ------------------------------------------------------
# Q11. Power using for loop (a^b)
# ------------------------------------------------------
def power(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result

print("Q11 Power:", power(2, 5))


# ------------------------------------------------------
# Q12. Swap two global variables without third variable
# ------------------------------------------------------
A = 5
B = 10

def swap_globals():
    global A, B
    A, B = B, A

print("Q12 Before Swap:", A, B)
swap_globals()
print("Q12 After Swap:", A, B)


# ------------------------------------------------------
# Q13. First n Armstrong numbers
# ------------------------------------------------------
def armstrong_numbers(n):
    result = []
    num = 1
    while len(result) < n:
        s = sum(int(d)**3 for d in str(num))
        if s == num:
            result.append(num)
        num += 1
    return result

print("Q13 Armstrong Numbers:", armstrong_numbers(5))


# ------------------------------------------------------
# Q14. Sum of digits of each number in list
# ------------------------------------------------------
def sum_digits_list(lst):
    results = []
    for num in lst:
        s = 0
        n = num
        while n > 0:
            s += n % 10
            n //= 10
        results.append((num, s))
    return results

print("Q14 Sum of Digits in List:", sum_digits_list([12, 305, 89]))
