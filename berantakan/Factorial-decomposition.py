def decomp(n):
    #your code here
    prime = {x:1 for x in range(2, n + 1) if all(x % p != 0 for p in range(2, int(x**0.5) + 1))}
    
    for key, value in prime.items():
        print(key)
        
        num = n
        while num % key == 0:
            print(num)
            num = num / key
            prime[key] += 1
            
    return prime
    
    
print(decomp(12))