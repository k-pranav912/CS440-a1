# standalone module
# ie. import this to use in other modules

vertex_list = []
neighbors = {}
start = ()
end = ()
grid_max = ()

# Each vertex is represented as a tuple, Vertex:(x,y)
# neighbors: key = Vertex i.e. tuple
#            value = [Vertex] i.e. list of tuples

# indexing starts at 1, and from top right of the grid diagram

# method to generate an adjacency list of vertices and its neighbors
# takes in the path to file (path), a list to store vertices (vertex_list)
# and a dictionary to store neighbors (neighbors = {Vertex:[Vertex]})
# returns 3 tuples, start point, end point, and max grid dimensions
def gen_grid(path, vertex_list, neighbors):
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
            
            if vertex2 not in neighbors[vertex1]:
                neighbors[vertex1].append(vertex2)
            if vertex1 not in neighbors[vertex2]:
                neighbors[vertex2].append(vertex1)

            if vertex3 not in neighbors[vertex1]:
                neighbors[vertex1].append(vertex3)
            if vertex1 not in neighbors[vertex3]:
                neighbors[vertex3].append(vertex1)

            if vertex4 not in neighbors[vertex3]:
                neighbors[vertex3].append(vertex4)
            if vertex3 not in neighbors[vertex4]:
                neighbors[vertex4].append(vertex3)

            if vertex2 not in neighbors[vertex4]:
                neighbors[vertex4].append(vertex2)
            if vertex4 not in neighbors[vertex2]:
                neighbors[vertex2].append(vertex4)

            if (not blocked):
                if vertex4 not in neighbors[vertex1]:
                    neighbors[vertex1].append(vertex4)
                if vertex1 not in neighbors[vertex4]:
                    neighbors[vertex4].append(vertex1)

                if vertex3 not in neighbors[vertex2]:
                    neighbors[vertex2].append(vertex3)
                if vertex2 not in neighbors[vertex3]:
                    neighbors[vertex3].append(vertex2)

            line = file.readline()


    
    return start, end, grid_max

# testing purposes
def main():
    start, end, grid_max = gen_grid("/common/home/sk2048/Desktop/cs440/a1/test/testfile1.txt", vertex_list, neighbors)
    # print(start)
    # print(end)
    # print(grid_max)
    vertex_list.sort()
    print(vertex_list)
    print()
    for key in neighbors:
        print(str(key) + " : " + str(neighbors[key]))
    return

if __name__=="__main__":
    main()