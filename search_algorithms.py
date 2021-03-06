import binary_heap as bh
import math
import grid_gen
import UI

def dummy_heuristic(vertex1, vertex2):
    return 0

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
    temp2 = values[successor][0]
    if temp < temp2:
        values[successor] = (temp, values[successor][1])
        parent[successor] = vertex
        if successor in fringe:
            bh.remove(fringe, successor, values)
        bh.insert(fringe, successor, values)


def a_star(start, end, neighbors, vertex_list, heuristic=heuristic_distance):
    values = {}
    visited = {}
    parent = {}
    fringe = []

    values[start] = (0, heuristic(start, end))
    parent[start] = start
    for vertex in vertex_list:
        visited[vertex] = False

    bh.insert(fringe, start, values)

    while len(fringe) != 0:
        temp_vertex = bh.pop(fringe, values)
        if (temp_vertex == end):
            return True, parent, values
        visited[temp_vertex] = True
        for successor in neighbors[temp_vertex]:
            if not visited[successor]:
                if successor not in fringe:
                    values[successor] = (float("inf"), heuristic(successor, end))
                    parent[successor] = None
                update_vertex(temp_vertex, successor, values, parent, fringe)
    
    
    return False, parent, values

def line_of_sight(vertex1, vertex2, cell_mat):
    x0, y0 = vertex1
    x1, y1 = vertex2
    f = 0
    dY = y1-y0
    dX = x1-x0

    if dY < 0:
        dY = 0-dY
        sY = -1
    else:
        sY = 1

    if dX < 0:
        dX = 0-dX
        sX = -1
    else:
        sX = 1

    if dX >= dY:
        while x0 != x1:
            f += dY
            if f >= dX:
                if cell_mat[y0+((sY-1)//2)][x0 + ((sX-1)//2)]:
                    return False
                y0 += sY
                f -= dX
            if (f != 0) and cell_mat[y0+((sY-1)//2)][x0 + ((sX-1)//2)]:
                return False
            if (dY == 0) and cell_mat[y0][x0 + ((sX-1)//2)] and cell_mat[y0-1][x0 + ((sX-1)//2)]:
                return False
            x0 = x0 + sX
    else:
        while y0 != y1:
            f += dX
            if f >= dY:
                if cell_mat[y0+((sY-1)//2)][x0+((sX-1)//2)]:
                    return False
                x0 += sX
                f -= dY
            if (f != 0) and cell_mat[y0+((sY-1)//2)][x0+((sX-1)//2)]:
                return False
            if (dX == 0) and cell_mat[y0+((sY-1)//2)][x0] and cell_mat[y0+((sY-1)//2)][x0-1]:
                return False
            y0 = y0+sY
    return True

def update_vertex_theta_star(vertex, successor, values, parent, fringe, cell_mat):
    # print(vertex, successor)
    if line_of_sight(parent[vertex], successor, cell_mat):
        # path 2
        # print("path 2")
        if values[parent[vertex]][0] + straight_line_distance(parent[vertex], successor) < values[successor][0]:
            values[successor] = (values[parent[vertex]][0] + straight_line_distance(parent[vertex], successor), values[successor][1])
            parent[successor] = parent[vertex]

            if successor in fringe:
                bh.remove(fringe, successor, values)
            
            bh.insert(fringe, successor, values)
    else:
        # path 1
        # print("path 1")
        if values[vertex][0] + straight_line_distance(vertex, successor) < values[successor][0]:
            values[successor] = (values[vertex][0] + straight_line_distance(vertex, successor), values[successor][1])
            parent[successor] = vertex
            if successor in fringe:
                bh.remove(fringe, successor, values)
            bh.insert(fringe, successor, values)

def theta_star(start, end, neighbors, cell_mat, vertex_list):
    values = {}
    visited = {}
    parent = {}
    fringe = []

    values[start] = (0, straight_line_distance(start, end))
    parent[start] = start

    for vertex in vertex_list:
        visited[vertex] = False

    bh.insert(fringe, start, values)

    while len(fringe) != 0:
        temp_vertex = bh.pop(fringe, values)
        if (temp_vertex == end):
            return True, parent, values
        visited[temp_vertex] = True
        for successor in neighbors[temp_vertex]:
            if not visited[successor]:
                if successor not in fringe:
                    values[successor] = (float("inf"), straight_line_distance(successor, end))
                    parent[successor] = None
                update_vertex_theta_star(temp_vertex, successor, values, parent, fringe, cell_mat)
    
    return False, parent, values