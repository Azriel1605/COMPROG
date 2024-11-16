def fib(n):
    """Calculates the nth Fibonacci number"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    digit1=0
    digit2=1
    for _ in range(abs(n)-1):
        temp = digit2
        digit2 += digit1
        digit1 = temp
        
    print(digit2)
    if n < 0 and n%2 ==0:
        return -digit2
    else:
        return digit2
    
print(fib(-666937))