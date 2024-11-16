def canDiv(target, numlist, memo={}):
    if target in memo:
        return memo[target]
    if target < 1:
        return False
    if target == 1:
        return True
    if target % 1 != 0:
        return False
    
    for num in numlist:
        sisa = target / num
        if canDiv(sisa, numlist, memo):
            memo[target] = True
            return True
        
    memo[target] = False
    return False

print(canDiv(11, [2, 3, 4]))