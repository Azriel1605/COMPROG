import math

def count_divisors(n):
    """Function to count the number of divisors of n."""
    count = 0
    sqrt_n = int(math.sqrt(n))
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            count += 1
            if i != n // i:  # Avoid double-counting the square root
                count += 1
    return count

def find_min_num(num_div):
    """Find the smallest number with exactly num_div divisors."""
    num = 1
    i = 0
    while True:
        if count_divisors(num) == num_div:
            return num
        i+=1
        print(i)
        num += 1

# Test examples
print(find_min_num(10))  # Output: 48
print(find_min_num(12))  # Output: 60
