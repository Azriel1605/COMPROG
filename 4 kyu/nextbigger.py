def next_bigger(n):
    string = str(n)
    first = string[0]
    biggest = sorted([x for x in string], reverse=True)
    print(first)
    
    
    loop = [x for x in string]
    loop_removeable = [x for x in string]
    for big in biggest:
        replace = loop_removeable.index(big)
        print(loop_removeable)
        if not replace:
            loop_removeable[replace] = -1
            print(loop_removeable)
            continue
        loop[replace], loop[replace-1] = loop[replace-1], loop[replace]
        if int(first) > int(loop[0]) and replace==1:
            loop_removeable[replace] = -1
            print(loop_removeable)
            continue
        
        result = ''.join(loop)
        if int(result) == n:
            return -1
        return int(result)
    return -1
    
print(next_bigger(414))