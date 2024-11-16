def smaller(arr):
    if not arr:
        return []
    
    # Normalize the array by mapping values to their ranks
    sorted_unique = sorted(set(arr))
    rank_map = {value: i + 1 for i, value in enumerate(sorted_unique)}  # Ranks start from 1

    # Initialize BIT with all zeros
    bit = [0] * (len(sorted_unique) + 1)
    
    def update(index, value):
        print('------------')
        while index < len(bit):
            bit[index] += value
            index += index & -index
            print(f'{bit=}')

    def query(index):
        result = 0
        while index > 0:
            result += bit[index]
            index -= index & -index
        return result

    result = []
    for num in reversed(arr):
        rank = rank_map[num]
        # Query how many numbers are smaller than the current number
        result.append(query(rank - 1))
        print(result)
        # Update BIT to include the current number
        update(rank, 1)
    
    # The results are in reverse order, so reverse them back
    return result[::-1]


print(smaller([5, 4, 7, 9, 2, 4, 1, 4, 5, 6]))
