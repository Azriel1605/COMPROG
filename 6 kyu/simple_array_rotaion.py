def solve(arr):
    if arr == sorted(arr):
        return "A"
    if arr == sorted(arr, reverse=True):
        return "D"
    big = arr[0]
    pointer = float('-inf')
    for num in arr:
        if num > big:
            pointer = num
            big = num
            
        
        if num < big:
            if num < pointer:
                return 'RD'
            return 'RA'
        
        if big < num:
            return 'RD'
    
    
print(solve([5, 9, 8, 7, 6]))