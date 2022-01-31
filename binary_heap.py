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

def insert(list, value):
    list.append(value)

    i = len(list)-1
    while i != 0 and list[parent(i)] > list[i]:
        list[parent(i)], list[i] = list[i], list[parent(i)]

def delete(list, index):
    return

def min_heapify(list, index):
    size = len(list)
    left = left_child(index)
    right = right_child(index)
    smallest = index

    if left < size - 1 and list[left] < list[index]:
        smallest = left
    if right < size - 1 and list[right] < list[index]:
        smallest = right
    if smallest != index:
        list[smallest], list[index] = list[index], list[smallest]
        min_heapify(list, smallest)