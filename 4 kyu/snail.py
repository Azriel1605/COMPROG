def snail(snail_map):
    result = []
    while snail_map:
        # Garis Atas
        result += snail_map[0]
        snail_map.pop(0)
        temp = []
        for index, i in enumerate(snail_map[:-1]):
            result.append(i[-1])
            snail_map[index].pop(-1)
            temp.append(i[0])
            snail_map[index].pop(0)
        if not snail_map:
            break
        result += snail_map[-1][::-1]
        snail_map.pop(-1)
        result += temp[::-1]

    return result
# print(snail([[1,2,3, 4],
#          [5, 6, 7, 8],
#          [9, 10, 11, 12],
#          [13, 14, 15, 16]]))
        