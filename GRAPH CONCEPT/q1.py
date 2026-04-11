from collections import deque
graph={
    'A':['B','D','E'],
    'B':['A','C','E'],
    'C':['B','G'],
    'D':['A','F'],
    'E':['A','B','F'],
    'F':['D','E','G'],
    'G':['C','F']
}
def bfs(start):
    visited=set()
    queue=deque()
    visited.add(start)
    queue.append(start)
    while queue:
        node=queue.popleft()
        print(node,end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
bfs('A')