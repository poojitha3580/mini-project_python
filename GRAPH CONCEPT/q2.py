graphs={
    'A':['S','D'],
    'S':['C','B'],
    'D':['C','B'],
    'C':['S','D'],
    'B':['S','D']
}
def dfs(node,visited=set()):
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
        for n in graphs[node]:
            dfs(n,visited)
def dfs_stack(start):
    visited=set()
    stack=[start]
    while stack:
        node=stack.pop()
        if node not in visited:
            print(node,end=" ")
            visited.add(node)
            stack.extend(graphs[node])
def dfs_path(start,goal,path=[]):
    path=path+[start]
    if start == goal:
        return path
    for n in graphs[start]:
        if n not in path:
            p= dfs_path(n,goal,path)
            if p:
                return
dfs('A')
print()
dfs_stack('A')
print()
print(dfs_path('A','B'))