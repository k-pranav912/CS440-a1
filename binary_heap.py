def get_f_value(vertex, graph_values):
    x,y = graph_values[vertex]
    return x+y

def parent(index):
    return (index-1)//2

def left_child(index):
    return (2*index)+1

def right_child(index):
    return (2*index)+2

def min_i(list):
    return list[0]

def pop(list, graph_values):
    if len(list) == 0:
        print("empty heap")
        return None
    
    if len(list) == 1:
        return list.pop(0)
    
    root = list[0]
    list[0] = list[len(list) - 1]
    list.pop(len(list) - 1)
    min_heapify(list, 0, graph_values)

    return root

def insert(list, value, graph_values):
    list.append(value)

    i = len(list)-1
    while i != 0 and get_f_value(list[parent(i)], graph_values) > get_f_value(list[i], graph_values):
        list[parent(i)], list[i] = list[i], list[parent(i)]
        i = parent(i)


def remove(list, value, graph_values):
    index = list.index(value)

    while index != 0:
        list[index], list[parent(index)] = list[parent(index)], list[index]
        index = parent(index)
    
    pop(list, graph_values)
    
    return

def min_heapify(list, index, graph_values):
    size = len(list)
    left = left_child(index)
    right = right_child(index)
    smallest = index

    if left < size - 1 and get_f_value(list[left], graph_values) < get_f_value(list[index], graph_values):
        smallest = left
    if right < size - 1 and get_f_value(list[right], graph_values) < get_f_value(list[smallest], graph_values):
        smallest = right
    if smallest != index:
        list[smallest], list[index] = list[index], list[smallest]
        min_heapify(list, smallest, graph_values)

# testing
def main():
    graph_vals = {1:(1,0), 2:(2,0), 3:(3,0), 4:(4,0), 5:(5,0), 6:{6,0}, 7:{7,0}, 8:{8,0}}
    heap = []
    print("heap: " + str(heap))
    insert(heap, 8, graph_vals)
    insert(heap, 7, graph_vals)
    insert(heap, 6, graph_vals)
    insert(heap, 5, graph_vals)
    insert(heap, 4, graph_vals)
    insert(heap, 3, graph_vals)
    insert(heap, 2, graph_vals)
    insert(heap, 1, graph_vals)
    print(heap)
    remove(heap, 2, graph_vals)
    print(heap)
    remove(heap, 5, graph_vals)
    print(heap)
    return

if __name__ == "__main__":
    main()