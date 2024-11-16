def dijkstras(graph, start, end):
    visited = []
    
    tabel = {
        'A': {'shortest': 0, 'previous':'A'},
        'B': {'shortest': 999, 'previous':None},
        'C': {'shortest': 999, 'previous':None},
        'D': {'shortest': 999, 'previous':None},
        'E': {'shortest': 999, 'previous':None},
        'F': {'shortest': 999, 'previous':None}
    }
    
    for key, value in graph.items():
        for target, distance in value.items():
            if target not in visited:
                if distance + tabel[key]['shortest'] < tabel[target]['shortest']:
                    tabel[target]['shortest'] = distance + tabel[key]['shortest']
                    tabel[target]['previous'] = key
                
        visited.append(key)
            
    for key, value in tabel.items():
        print(key, value)
    
    result = [end]
    node = end
    while node != start:
        node = tabel[node]['previous']
        result.append(node)
        
    return result[::-1]
    
path = {
    'A': {'B': 2, 'D': 8},
    'B': {'A': 2, 'D': 5, 'E': 6},
    'D': {'A': 8, 'B': 5, 'E':3, 'F':2},
    'E': {'B':6, 'C':9, 'D':3, 'F':1},
    'F': {'C':3, 'D':2, 'E':1},
    'C': {'E': 9, 'F': 3},
}

print(dijkstras(path, 'A', 'C'))