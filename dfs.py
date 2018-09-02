def dfs(g,start, end, path=[]):
    path+=[start]
    # print path,start,end
    if start == end:
        return path
    for ch in g[start]:
        if ch not in path:
            path_found = dfs(g,ch,end,path)
            if path_found:
                return path_found
    return []

# def dfs_iterative(g,start,end):
#     path = [start]
#     q = []
#     q.append(start)
#     while q:
#         element = q.pop()
#         if not element.visited:
#             pass

def route(s,d,g, visited=None):
    if visited == None:
        visited = []
    if s == d:
        return True
    for node in g[s]:
        if node not in visited:
            visited.append(node)
            if (route(node,d,g,visited)):
                return True
    return False






graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}



print dfs(graph,'A', 'D')
print route('A','D',graph)
