# # Memoize
# dp = {}

def min_ignore_none(a, b):
    if a == None:
        return b
    if b == None:
        return a
    return min(a, b)

# def minimum_coins(target, coins):
#     if target in dp:
#         return dp[target]
    
#     if target == 0:
#         answer = 0
    
#     else:
#         answer = None
#         for coin in coins:
#             subproblem = target - coin
#             if subproblem < 0:
#                 continue
            
#             answer = min_ignore_none(answer, minimum_coins(subproblem, coins) + 1)
    
#     dp[target] = answer
#     return answer
    

# print(minimum_coins(100000, [1, 4, 5]))

# Button Up solution

def minimum_coins(target, coins):
    dp = {}
    
    dp[0] = 0
    for i in range(1, target+1):
        for coin in coins:
            subproblem = i - coin
            if subproblem < 0:
                continue
            dp[i] = min_ignore_none(dp.get(i), dp.get(subproblem) + 1)
    
    return dp[target]
    
print(minimum_coins(9999999999, [1, 4, 5]))
