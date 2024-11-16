def josephus_survivor(n,k):
    #your code here
    items = [n for n in range(1, n+1)]
    pointer = -1
    dead_person = []
    
    while len(items) != 0:
        pointer += k
        max_index = len(items)
        if pointer >= max_index:
            pointer = pointer % max_index
        # print(f'{pointer=}')
        # print(f'{len(items)=}')
        dead_person.append(items[pointer])
        items.pop(pointer)
        pointer -= 1
        
        
    
    return dead_person[-1]