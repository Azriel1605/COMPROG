import time
time_start = time.time()

def canConstruct(target, wordBank, memo={}):
    if target in memo: return memo[target]
    if target == '': return True
    
    for word in wordBank:
        try:
            if target.index(word) == 0:
                suffix = target[len(word):]
                if canConstruct(suffix, wordBank, memo):
                    memo[target] = True
                    return True
        except:
            continue
    memo[target] = False
    return False

print(canConstruct('mouseadhakufgkafasjdhkauefgasbakd', ['ou', 'mo', 's', 'se', 'akasfa', 'aduhf', 'akfuhj', 'akhgajk', 'ou', 'mo', 's', 'se', 'akasfa', 'aduhf', 'akfuhj', 'akhgajk', 'ou', 'mo', 's', 'se', 'akasfa', 'aduhf', 'akfuhj', 'akhgajk']))
time_end = time.time()
print(time_end - time_start)
