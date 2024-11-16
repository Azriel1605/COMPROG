# Competitive Programming Cheatsheet

# 1. INPUT/OUTPUT
import sys
input = sys.stdin.read
# Example: Reading a list of integers
nums = list(map(int, input().split()))

# Fast I/O
from sys import stdin, stdout
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
stdout.write(" ".join(map(str, arr)) + "\n")

# 2. MATH FUNCTIONS
from math import gcd, lcm, sqrt, ceil, floor, log2, log10
from functools import reduce

# GCD and LCM
g = gcd(12, 15)  # 3
l = lcm(12, 15)  # 60

# Prime check (basic)
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Sieve of Eratosthenes
def sieve(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(sqrt(n)) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [x for x in range(n + 1) if primes[x]]

# 3. SORTING
arr = [5, 3, 2, 8, 1]
arr.sort()  # Ascending
arr.sort(reverse=True)  # Descending

# Custom Sort
arr.sort(key=lambda x: (x % 2, x))  # Sort by even/odd then value

# 4. DATA STRUCTURES
from collections import defaultdict, deque, Counter

# Dictionary with default value
d = defaultdict(int)
d['key'] += 1

# Deque for double-ended queue
dq = deque([1, 2, 3])
dq.append(4)      # Add to the end
dq.appendleft(0)  # Add to the beginning
dq.pop()          # Remove from the end
dq.popleft()      # Remove from the beginning

# Counter for frequency
counter = Counter(arr)

# 5. BINARY SEARCH
from bisect import bisect_left, bisect_right

arr = [1, 2, 4, 4, 5]
# Find the leftmost position to insert 4
pos = bisect_left(arr, 4)
# Find the rightmost position to insert 4
pos = bisect_right(arr, 4)

# 6. GRAPH ALGORITHMS
from heapq import heappush, heappop

# Adjacency list
graph = defaultdict(list)
graph[1].append((2, 5))  # Node 1 to Node 2 with weight 5

# Dijkstra's Algorithm
def dijkstra(start, n):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]  # (distance, node)
    while pq:
        d, u = heappop(pq)
        if d > dist[u]: continue
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heappush(pq, (dist[v], v))
    return dist

# Depth-First Search
def dfs(node, visited, graph):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited, graph)

# Breadth-First Search
def bfs(start, graph):
    visited = [False] * len(graph)
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

# 7. STRING MANIPULATION
s = "hello"
# Reversing
rev = s[::-1]
# Substrings
subs = s[1:4]
# Count frequency of a character
freq = s.count('l')

# 8. MODULAR ARITHMETIC
MOD = 10**9 + 7

# Modular Exponentiation
def mod_exp(base, exp, mod=MOD):
    res = 1
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exp //= 2
    return res

# Modular Inverse (Fermat's Little Theorem)
def mod_inverse(a, mod=MOD):
    return mod_exp(a, mod - 2, mod)

# 9. PERMUTATIONS AND COMBINATIONS
from itertools import permutations, combinations

# Permutations
perm = list(permutations([1, 2, 3]))  # All orderings
# Combinations
comb = list(combinations([1, 2, 3], 2))  # All 2-length subsets

# 10. COMMON TRICKS
# Pairwise XOR to find unique element
arr = [1, 1, 2, 2, 3]
unique = reduce(lambda x, y: x ^ y, arr)  # Result: 3

# Prefix Sum
prefix_sum = [0] * (len(arr) + 1)
for i in range(len(arr)):
    prefix_sum[i + 1] = prefix_sum[i] + arr[i]

# Sliding Window Maximum (Deque)
def max_sliding_window(nums, k):
    dq = deque()
    res = []
    for i in range(len(nums)):
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res
