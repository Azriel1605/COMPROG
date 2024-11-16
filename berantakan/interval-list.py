def solution(args):
    sort_list = sorted(args)
    print(sort_list)
    all_interval = []
    seeker = sort_list[0]
    interval = [seeker]
    for i in sort_list[1:]:
        if seeker +1 == i:
            interval.append(i)
        else:
            if len(interval) > 2:
                # print(len(interval), interval)
                all_interval.append(interval)
            else:
                print(len(interval), interval)
                for x in interval:
                    all_interval.append([x])
            interval = [i]
        seeker = i
    if len(interval) > 2:
        all_interval.append(interval)
    else:
        print(len(interval), interval)
        for x in interval:
            all_interval.append([x])
    
    print(all_interval)
    string = ''
    for i in all_interval:
        if len(i) == 1:
            string += f'{i[0]},'
        else:
            string += f'{i[0]}-{i[-1]},'
            
    return string[:-1]

print(solution([-95, -92, -91, -88, -86, -85, -84, -81, -78, -76, -74, -71, -70, -68, -67, -65, -63, -61, -59, -56, -55]))