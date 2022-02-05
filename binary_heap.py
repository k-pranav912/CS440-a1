def get_f_value(vertex, graph_values):
    x,y = graph_values[vertex]
    return x+y

def parent(index):
    return (index-1)/2

def left_child(index):
    return (2*index)+1

def right_child(index):
    return (2*index)+2

def min_i(list):
    return list[0]

def extract_min(list):
    if len[list] == 0:
        print("empty heap")
        return None
    
    if len[list] == 1:
        return list.pop(0)
    
    root = list[0]
    list[0] = list[len(list) - 1]
    list.pop(len(list) - 1)
    min_heapify(list, 0)

    return root

def insert(list, value, graph_values):
    list.append(value)

    i = len(list)-1
    while i != 0 and get_f_value(list[parent(i)], graph_values) > get_f_value(list[i], graph_values):
        list[parent(i)], list[i] = list[i], list[parent(i)]

def delete(list, index):
    return

def min_heapify(list, index, graph_values):
    size = len(list)
    left = left_child(index)
    right = right_child(index)
    smallest = index

    if left < size - 1 and get_f_value(list[left], graph_values) < get_f_value(list[index], graph_values):
        smallest = left
    if right < size - 1 and get_f_value(list[right], graph_values) < get_f_value(list[index], graph_values):
        smallest = right
    if smallest != index:
        list[smallest], list[index] = list[index], list[smallest]
        min_heapify(list, smallest)