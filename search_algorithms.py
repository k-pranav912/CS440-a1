def bfs(start, end, neighbors, vertex_list):
    if start == end: return True
    queue = []
    visited = {}
    queue.append(start)

    for vertex in vertex_list:
        visited[vertex] = False
    visited[start] = True

    while queue:
        for neighbor in neighbors[queue.pop(0)]:
            if neighbor == end: return True
            if not visited[neighbor]:
                queue.append(neighbor)
            visited[neighbor] = True
    return False

def aStar():
    pass

def thetaStar():
    pass

def lineOfSight():
    pass

