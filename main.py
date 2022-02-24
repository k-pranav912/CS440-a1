from turtle import st
from gen_rand_grid import generate_grid
import grid_gen
import search_algorithms
import UI
import time

def generate_random_grids():
    numGrids = 0
    while not (1 <= numGrids <= 50):
        print("Enter the number of grids to generate, up to 50")
        numGrids = int(input())
    
    numRows = 0
    while not (1 <= numRows <= 100):
        print("Enter the number of rows, up to 100")
        numRows = int(input())
    
    numCols = 0
    while not (1 <= numCols <= 50):
        print("Enter the number of columns, up to 50")
        numCols = int(input())

def print_random_grids():

    begin = time.perf_counter()
    f = open("Grids/Time.csv", "w")
    print("=======================")
    
    for i in range(50):
        while True:
            grid_path = "./Grids/Grid" + str(i+1) + ".txt"
            # generate_grid(numRows, numCols, grid_path)
            vertex_list = []
            neighbors = {}
            start, end, grid_max, cell_matrix = grid_gen.gen_grid(grid_path, vertex_list, neighbors)

            if search_algorithms.bfs(start, end, neighbors, vertex_list):
                break

        start_time = time.perf_counter()

        parents = {}
        path = []
        for vertex in vertex_list:
            parents[vertex] = None
        found, parent, values = search_algorithms.a_star(start, end, neighbors, vertex_list)
        if not found:
            print("Not Found")
            return
        else:
            temp = end
            while not temp == start:
               path.append(temp)
               temp = parent[temp]
            path.append(temp)
            path.reverse()
            for vert in path:
                print(vert)

        end_time = time.perf_counter()

        x,y = values[path[-1]]
        f.write("Grid" + str(i+1) + ",A*," + f"{end_time - start_time:0.4f}," + str(x) + "\n")

        # row, col = cell_matrix.shape
        # blocked_cell = []
        # for i in range(1, row-1):
        #     for j in range(1, col-1):
        #         if cell_matrix[i][j] == 1:
        #             blocked_cell.append((i, j))
        # UI.Grid(path,start,end,(100,50),blocked_cell,values).mainloop()

        print("-----------------------")

        start_time = time.perf_counter()

        path = []
        found, parent, values = search_algorithms.theta_star(start, end, neighbors, cell_matrix, vertex_list)
        if not found:
            print("Not Found")
            return
        else:
            temp = end
            while not temp == start:
               path.append(temp)
               temp = parent[temp]
            path.append(temp)
            path.reverse()
            for vert in path:
                print(vert)

        end_time = time.perf_counter()

        x,y = values[path[-1]]
        f.write("Grid" + str(i+1) + ",T*," + f"{end_time - start_time:0.4f}," + str(x) + "\n")
        
        print("=======================")
    ending = time.perf_counter()

    f.write("Total," + f"{ending - begin:0.4f}")

def check_list_equal(list1, list2):
    if len(list1) != len(list2):
        return False

    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    
    return True

def test_t_star():
    path = "/common/home/sk2048/Desktop/cs440/a1/Grids/Grid"

    index = input("Enter grid number: ")
    temp_path = path + index + ".txt"
    vertex_list = []
    neighbors = {}
    start, end, grid_max, cell_matrix = grid_gen.gen_grid(temp_path, vertex_list, neighbors)

    if not search_algorithms.bfs(start, end, neighbors, vertex_list):
        return False

    t_path = []
    found, parent, values = search_algorithms.theta_star(start, end, neighbors, cell_matrix, vertex_list)
    if not found:
        print("Not Found")
        return False
    else:
        temp = end
        while not temp == start:
            t_path.append(temp)
            temp = parent[temp]
        t_path.append(temp)
        t_path.reverse()

    v_path = []
    cell_mat, grid_max, start, end = grid_gen.gen_matrix(temp_path)
    vertex_list, neighbors = grid_gen.visibility_graph(cell_mat, start, end)
    found, parent, values = search_algorithms.a_star(start, end, neighbors, vertex_list, search_algorithms.dummy_heuristic)
    if not found:
        print("Not Found")
        return False
    else:
        temp = end
        while not temp == start:
            v_path.append(temp)
            temp = parent[temp]
        v_path.append(temp)
        v_path.reverse()

    result = check_list_equal(v_path, t_path)

    print("Grid" + index + " : " + str(result))

def main():
    run_UI()
    # print_random_grids()
    # test_t_star()

def run_UI():
    vertex_list = []
    neighbors = {}
    parents = {}
    while (True):
        userinput = input("Enter the full path to the file, or Q to quit: ")
        if userinput == "Q": return
        try:
            start, end, grid_max, cell_matrix = grid_gen.gen_grid(userinput, vertex_list, neighbors)
            grid_path = userinput
        except:
            print("Invalid Path.")
            continue
        if not search_algorithms.bfs(start, end, neighbors, vertex_list):
            print("No path found between the start and goal.")
            continue
        break
    

    while (True):
        userinput = input("Enter A for A* search, T for Theta* search, V for true-minimal path, F to change file, or Q to quit: ")
        for vertex in vertex_list:
            parents[vertex] = None
        path = []

        if userinput == "A":
            found, parent, values = search_algorithms.a_star(start, end, neighbors, vertex_list)

        elif userinput == "T":
            found, parent, values = search_algorithms.theta_star(start, end, neighbors, cell_matrix, vertex_list)

        elif userinput == "V":
            cell_mat, grid_max, start, end = grid_gen.gen_matrix(grid_path)
            vertex_list, neighbors = grid_gen.visibility_graph(cell_mat, start, end)
            found, parent, values = search_algorithms.a_star(start, end, neighbors, vertex_list, search_algorithms.dummy_heuristic)

        elif userinput == "F":
            vertex_list = []
            neighbors = {}
            parents = {}
            while (True):
                userinput = input("Enter the full path to the file, or Q to quit: ")
                if userinput == "Q": return
                try:
                    start, end, grid_max, cell_matrix = grid_gen.gen_grid(userinput, vertex_list, neighbors)
                except:
                    print("Invalid Path.")
                    continue
                if not search_algorithms.bfs(start, end, neighbors, vertex_list):
                    print("No path found between the start and goal.")
                    continue
                break
            continue

        elif userinput == "Q":
            return

        else:
            print("Invalid Input")

        if not found:
            print("Not Found")
            return
        else:
            temp = end
            while not temp == start:
                path.append(temp)
                temp = parent[temp]
            path.append(temp)
            path.reverse()

        row, col = cell_matrix.shape
        blocked_cell = []
        for i in range(1, row-1):
            for j in range(1, col-1):
                if cell_matrix[i][j] == 1:
                    blocked_cell.append((i, j))
        

        UI.Grid(path,start,end,grid_max,blocked_cell,values).mainloop()

if __name__ == "__main__":
    main()
