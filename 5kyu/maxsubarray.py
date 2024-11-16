def subarray(array, maximum=-float('inf')):
    current = 0
    for num in array:
        current += num
        if current > maximum:
            maximum = current