# def dijkstras(graph, start):
#     visited = []
    
#     tabel = {
#         'A': {'shortest': 0, 'previous':'A'},
#         'B': {'shortest': 999, 'previous':None},
#         'C': {'shortest': 999, 'previous':None},
#         'D': {'shortest': 999, 'previous':None},
#         'E': {'shortest': 999, 'previous':None},
#         'F': {'shortest': 999, 'previous':None}
#     }
    
#     for key, value in graph.items():
#         for target, distance in value.items():
#             if target not in visited:
#                 if distance + tabel[key]['shortest'] < tabel[target]['shortest']:
#                     tabel[target]['shortest'] = distance + tabel[key]['shortest']
#                     tabel[target]['previous'] = key
                
#         visited.append(key)
            
#     print(tabel.items())
    
# path = {
#     'A': {'B': 2, 'D': 8},
#     'B': {'A': 2, 'D': 5, 'E': 6},
#     'D': {'A': 8, 'B': 5, 'E':3, 'F':2},
#     'E': {'B':6, 'C':9, 'D':3, 'F':1},
#     'F': {'C':3, 'D':2, 'E':1},
#     'C': {'E': 9, 'F': 3},
# }

# print(dijkstras(path, 'A'))

##########################################################################
def dijkstras(graph, start, end):
    visited = []
    Node_to_check = [start]
    tabel = {}
    
    for letter in graph.keys():
        if letter == start:
            tabel[start] = {'shortest':0, 'previous':start}
        else:
            tabel[letter] = {'shortest':float('inf'), 'previous':None}
    
    def shortest_path(node):
        for char in graph[node]:
            if char not in visited:
                print(char)
            if char not in Node_to_check:
                Node_to_check.append(char)
        visited.append(node)
    
    
    def shortest_path(node):
        for target, distance in graph[node].items():
            if target not in visited:
                if distance + tabel[node]['shortest'] < tabel[target]['shortest']:
                    tabel[node]['shortest'] = distance + tabel[node]['shortest']
                    tabel[node]['prevoius'] = node
            if target not in Node_to_check:
                Node_to_check.append(target)
        visited.append(node)
    
    for i in Node_to_check:
        # print(f'Start = {i}')
        shortest_path(i)
        
        
    for key, value in graph.items(): # START
        for target, distance in value.items(): # NODE
            if target not in visited:
                if distance + tabel[key]['shortest'] < tabel[target]['shortest']:
                    tabel[target]['shortest'] = distance + tabel[key]['shortest']
                    tabel[target]['previous'] = key
                
        visited.append(key)
            
    # print(tabel.items())
    
    result = [end]
    node = end
    print(node)
    for key, value in tabel.items():
        print(key, value)
    
    while node != start:
        # print(node, start)
        node = tabel[node]['previous']
        result.append(node)
    return result[::-1]
    
graph = {
    'A': {'B': 2, 'D': 8},
    'B': {'A': 2, 'D': 5, 'E': 6},
    'D': {'A': 8, 'B': 5, 'E':3, 'F':2},
    'E': {'B':6, 'C':9, 'D':3, 'F':1},
    'F': {'C':3, 'D':2, 'E':1},
    'C': {'E': 9, 'F': 3},
}






print(dijkstras(graph, 'A', 'C'))
