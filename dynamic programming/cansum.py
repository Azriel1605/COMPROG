def canSum(target, number, memo={}):
    if target == 0: return True
    if target < 0: return False
    for i in number:
        sisa = target - i
        if canSum(sisa, number, memo):
            return True
    return False

print(canSum(10, [3, 6, 8]))