def bestSum(target, numbers, memo={}):
    if target in memo: return memo[target]
    if target == 0: return []
    if target < 0: return None
    
    shortest = None
    for num in numbers:
        sisa = target - num
        kombinasi = bestSum(sisa, numbers, memo)
        if kombinasi != None:
            comb = kombinasi + [num]
            if shortest == None or len(comb) < len(shortest):
                shortest = comb
    memo[target] = shortest
    return shortest

print(bestSum(1794, [2, 3, 4, 5]))