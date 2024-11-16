def countConstruct(target, wordBank, memo={}):
    if target in memo: return memo[target]
    if target == '': return 1
    total = 0
    
    for word in wordBank:
        try:
            if target.index(word) == 0:
                numway = countConstruct(target[len(word):], wordBank, memo)
                total += numway
        except:
            continue
    memo[target] = total
    return total

print(countConstruct('icecream', ['i', 'c', 'e', 'cream', 'm', 're', 'am', 'ice']))