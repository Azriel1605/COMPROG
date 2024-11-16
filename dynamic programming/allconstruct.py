def allConstruct(target, wordbank, memo={}):
    if target in memo: return memo[target]
    if target == '': return [[]]
    
    result = []
    
    for word in wordbank:
        try:
            if target.index(word) == 0:
                suffix = target[len(word):]
                suffixWays = allConstruct(suffix, wordbank, memo)
                targetWays = list(map(lambda x: [word, *x], suffixWays))
                result.append(*targetWays)
        except:
            continue
        
    memo[target] = result
    return result

print(allConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))