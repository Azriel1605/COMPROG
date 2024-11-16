def canSum(target, numlist, memo={}):
    if target in memo: return memo[target]
    if target == 0: return True
    if target < 0: return False
    
    for num in numlist:
        sisa = target - num
        if canSum(sisa, numlist, memo):
            memo[target] = True
            return True
    
    memo[target] = False
    return False

print(canSum(11, [3]))