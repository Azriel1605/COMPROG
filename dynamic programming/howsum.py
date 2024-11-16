def howSum(target, number, memo={}):
    if target in memo: return memo[target]
    if target == 0: return []
    if target < 0: return None
    for i in number:
        sisa = target - i
        result = howSum(sisa, number, memo)
        if result != None:
            memo[target] = result + [i]
            return memo[target]
        
    memo[target] = None
    return None

print(howSum(10, [2, 3, 4, 5]))