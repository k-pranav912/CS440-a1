import binary_heap as bh
import math

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

def heuristic_distance(vertex, end):
    dY = abs(end[1] - vertex[1])
    dX = abs(end[0] - vertex[0])
    
    val1 = math.sqrt(2)*min(dY, dX)
    val2 = max(dY, dX)
    val3 = min(dY, dX)

    return val1 + val2 - val3

def straight_line_distance(vertex1, vertex2):
    dY = abs(vertex2[1] - vertex1[1])
    dX = abs(vertex2[0] - vertex1[0])

    return math.sqrt(math.pow(dY, 2) + math.pow(dX, 2))

def update_vertex(vertex, successor, values, parent, fringe):
    temp = values[vertex][0] + straight_line_distance(vertex, successor)
    if temp < values[successor][1]:
        values[successor][0] = temp
        parent[successor] = vertex
        if successor in fringe:
            bh.remove(fringe, successor, values)
        bh.insert(fringe, successor, values)


def aStar(start, end, neighbors):
    values = {}
    visited = []
    parent = {}
    fringe = []

    values[start] = (0, heuristic_distance(start, end))
    parent[start] = start

    bh.insert(fringe, start, values)

    while len(fringe) != 0:
        temp_vertex = bh.pop(fringe, values)
        if (temp_vertex == end):
            return "path found"
        visited.append(temp_vertex)
        for successor in neighbors[temp_vertex]:
            if successor not in visited:
                if successor not in fringe:
                    values[successor] = (float("inf"), heuristic_distance)
                    parent[successor] = None
                update_vertex(temp_vertex, successor)

def thetaStar():
    pass

def lineOfSight():
    pass

