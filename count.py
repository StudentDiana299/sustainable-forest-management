
def factorials(n):
    if n == 1:
        return n
    else:
        return n * factorials(n-1)  # <<-- Notice how the function does factorial(n-1) within factorial(n)!
    
factorials(5) == 120

def factorial(n):
    if n == 1:
        return n
    else:
        print("n = ", n, "; now calling factorial(n-1)", sep = "")
        lower_fact = factorial(n-1)
        current_fact = n * lower_fact
        print("n = ",n, "; factorial(n-1) returned ", lower_fact,"; multiplied by n to get ", current_fact, sep = "")
        return  current_fact
factorial(5)

def expo(a,n):
    if n == 0:
        return 1
    else:
        return a* expo (a, n-1)
    
print(expo(2,3))