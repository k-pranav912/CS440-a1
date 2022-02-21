# standalone module
# ie. import this to use in other modules
import numpy as np

cell_matrix= []
vertex_list = []
neighbors = {}
start = ()
end = ()
grid_max = ()

def gen_matrix(path):
    with open(path)as file:
        line = file.readline()
        temp = line.split()
        start = (int(temp[0]), int(temp[1]))

        line = file.readline()
        temp = line.split()
        end = (int(temp[0]), int(temp[1]))

        line = file.readline()
        temp = line.split()
        grid_max = (int(temp[0]), int(temp[1]))

        matrix = np.zeros((grid_max[1]+2, grid_max[0]+2), dtype=np.int64)
        matrix[0,:] = 1
        matrix[:,0] = 1
        matrix[-1,:] = 1
        matrix[:,-1] = 1

        line = file.readline()
        while line:
            temp = line.split()
            matrix[int(temp[1])][int(temp[0])] = int(temp[2])
            line = file.readline()
        
    return matrix, grid_max, start, end


# Each vertex is represented as a tuple, Vertex:(x, y)
# neighbors: key = Vertex i.e. tuple
#            value = [Vertex] i.e. list of tuples

# indexing starts at 1, and from top left of the grid diagram

# method to generate an adjacency list of vertices and its neighbors
# takes in the path to file (path), a list to store vertices (vertex_list)
# and a dictionary to store neighbors (neighbors = {Vertex:[Vertex]})
# returns 3 tuples, start point, end point, and max grid dimensions
def gen_grid(path, vertex_list, neighbors):

    cell_mat, grid_max, start, end = gen_matrix(path)
    with open(path) as file:
        line = file.readline()
        temp = line.split()
        start = (int(temp[0]), int(temp[1]))

        line = file.readline()
        temp = line.split()
        end = (int(temp[0]), int(temp[1]))

        line = file.readline()
        temp = line.split()
        grid_max = (int(temp[0]), int(temp[1]))

        line = file.readline()
        while line:
            temp = line.split()
            blocked = bool(int(temp[2]))
            vertex1 = (int(temp[0]), int(temp[1])) # top left
            vertex2 = (vertex1[0] + 1, vertex1[1]) # top right
            vertex3 = (vertex1[0], vertex1[1] + 1) # bottom left
            vertex4 = (vertex1[0] + 1, vertex1[1] + 1) # bottom right

            if (vertex1 not in vertex_list):
                vertex_list.append(vertex1)
                neighbors[vertex1] = []
            if (vertex2 not in vertex_list):
                vertex_list.append(vertex2)
                neighbors[vertex2] = []
            if (vertex3 not in vertex_list):
                vertex_list.append(vertex3)
                neighbors[vertex3] = []
            if (vertex4 not in vertex_list):
                vertex_list.append(vertex4)
                neighbors[vertex4] = []
            
            # top edge
            if not (cell_mat[vertex1[1]][vertex1[0]] == 1 and cell_mat[vertex1[1]-1][vertex1[0]] == 1):
                if vertex2 not in neighbors[vertex1]:
                    neighbors[vertex1].append(vertex2)
                if vertex1 not in neighbors[vertex2]:
                    neighbors[vertex2].append(vertex1)

            # left edge
            if not (cell_mat[vertex1[1]][vertex1[0]] == 1 and cell_mat[vertex1[1]][vertex1[0]-1] == 1):
                if vertex3 not in neighbors[vertex1]:
                    neighbors[vertex1].append(vertex3)
                if vertex1 not in neighbors[vertex3]:
                    neighbors[vertex3].append(vertex1)

            #bottom edge
            if not (cell_mat[vertex3[1]][vertex3[0]] == 1 and cell_mat[vertex3[1]-1][vertex3[0]] == 1):
                if vertex4 not in neighbors[vertex3]:
                    neighbors[vertex3].append(vertex4)
                if vertex3 not in neighbors[vertex4]:
                    neighbors[vertex4].append(vertex3)

            #right edge
            if not (cell_mat[vertex2[1]][vertex2[0]] == 1 and cell_mat[vertex2[1]][vertex2[0]-1] == 1):
                if vertex2 not in neighbors[vertex4]:
                    neighbors[vertex4].append(vertex2)
                if vertex4 not in neighbors[vertex2]:
                    neighbors[vertex2].append(vertex4)

            if (not blocked):
                #top-left bottom-right diagonal
                if vertex4 not in neighbors[vertex1]:
                    neighbors[vertex1].append(vertex4)
                if vertex1 not in neighbors[vertex4]:
                    neighbors[vertex4].append(vertex1)

                #top-right bottom-left diagonal
                if vertex3 not in neighbors[vertex2]:
                    neighbors[vertex2].append(vertex3)
                if vertex2 not in neighbors[vertex3]:
                    neighbors[vertex3].append(vertex2)

            line = file.readline()

    return start, end, grid_max, cell_mat

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

def visibility_graph(cell_mat, start, end):
    print("start: " + str(start))
    print("end: " + str(end))
    print(cell_mat)
    vertex_list = []
    neighbors = {}
    neighbors[start] = []
    neighbors[end] = []
    vertex_list.append(start)
    vertex_list.append(end)


    max_rows, max_cols = cell_mat.shape

    print("max rows: " + str(max_rows))
    print("max_cols: " + str(max_cols))

    for row in range(1,max_rows-1):
        for col in range(1, max_cols-1):
            print("index(row, col): " + str(row) + ", " + str(col))
            if cell_mat[row][col] == 1:
                print(True)
                vertex1 = (col, row) # top left
                vertex2 = (col+1, row) # top right
                vertex3 = (col, row+1) # bottom left
                vertex4 = (col+1, row+1) # bottom right
                print(vertex1, vertex2, vertex3, vertex4)

                try:
                    temp = neighbors[vertex1]
                except KeyError:
                    neighbors[vertex1] = []
                    vertex_list.append(vertex1)
                
                try:
                    temp = neighbors[vertex2]
                except KeyError:
                    neighbors[vertex2] = []
                    vertex_list.append(vertex2)

                try:
                    temp = neighbors[vertex3]
                except KeyError:
                    neighbors[vertex3] = []
                    vertex_list.append(vertex3)

                try:
                    temp = neighbors[vertex4]
                except KeyError:
                    neighbors[vertex4] = []
                    vertex_list.append(vertex4)
    
    print(vertex_list)
    
    for source in vertex_list:
        for target in vertex_list:
            if source != target:
                print(source, target, end=" ")
                if line_of_sight(source, target, cell_mat):
                    print("yay")
                    neighbors[source].append(target)
                else:
                    print()
                
    
    return vertex_list, neighbors

def main():
    path = "/common/home/sk2048/Desktop/cs440/a1/Grids/grid_test_1.txt"
    cell_mat, grid_max, start, end = gen_matrix(path)
    vertex_list, neighbors = visibility_graph(cell_mat, start, end)
    print("vertices")
    print(vertex_list)
    print("neighbors")
    for element in neighbors:
        print(str(element) + ": " + str(neighbors[element]))
    return

if __name__ == "__main__":
    main()
