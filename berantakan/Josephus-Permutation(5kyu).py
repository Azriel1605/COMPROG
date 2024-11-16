# they formed a circle and proceeded to kill one man every three,
# until one last man was left (and that it was supposed to kill himself to end the act).


def josephus(items,k):
    #your code here
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
        
        
    
    return dead_person

print(josephus([1,2,3,4,5,6,7], 3))