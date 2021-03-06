def get_f_value(vertex, graph_values):
    x,y = graph_values[vertex]
    return x+y

def get_h_value(vertex, graph_values):
    x,y = graph_values[vertex]
    return y

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
    while i != 0 and (get_f_value(list[parent(i)], graph_values) > get_f_value(list[i], graph_values)):
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

    if left < size - 1 and (get_f_value(list[left], graph_values) < get_f_value(list[index], graph_values) or ((get_f_value(list[left], graph_values) == get_f_value(list[index], graph_values) and get_h_value(list[left], graph_values) < get_h_value(list[index], graph_values)))):
        smallest = left
    if right < size - 1 and (get_f_value(list[right], graph_values) < get_f_value(list[smallest], graph_values) or ((get_f_value(list[right], graph_values) == get_f_value(list[smallest], graph_values) and get_h_value(list[right], graph_values) < get_h_value(list[smallest], graph_values)))):
        smallest = right
    if smallest != index:
        list[smallest], list[index] = list[index], list[smallest]
        min_heapify(list, smallest, graph_values)
