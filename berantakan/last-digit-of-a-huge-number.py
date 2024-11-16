def last_digit(List):
    if len(List) == 0:
        return 1
    if len(List) == 1:
        return List[0]
    
    exponen = List[-1]
    
    for based in reversed(List[:-1]):
        print('-----')
        print(based, exponen)
        exponen = (based ** (exponen%4))
        if exponen == 0:
            exponen == 4
        print(exponen)
        
    return exponen % 10
        
    

print(last_digit([7, 6, 21]))